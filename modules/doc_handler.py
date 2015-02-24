import webapp2
import json
import template_renderer
import logging

from google.appengine.api import channel
from google.appengine.api import users
from google.appengine.ext import ndb
from document import Document
from user import User

# Sends a message to all users on a given document
# Doesn't send a text update to the user who initiated the update
# 
def broadcast_to_all(doc, user_id, doc_id):
    message_notext = json.dumps({
        'online': doc.online.values(),
    })
    message = json.dumps({
        'text': doc.text,
        'online': doc.online.values(),
    })
    for key in doc.online:
        if key != user_id:
            channel.send_message(doc_id + '_' + key, message)
        else:
            channel.send_message(doc_id + '_' + key, message_notext)

# handles a request for the wall page
class DocHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        # Check that the user is signed in, if not, redirect
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return

        # Ensure that there is a corresponding datastore entry
        user_id = user.user_id()
        iter = User.query(User.user_id == user_id).iter()
        if not iter.has_next():
            User(user_id = user_id, nickname = user.nickname()).put()

        # Get the document, creates a new one if one isn't specified
        doc_id = self.request.get('doc_id')
        if not doc_id:
            doc = Document(text = '', online = {})
            doc_id = str(doc.put().id())
            self.redirect('/?doc_id=' + doc_id)
            return
        else:
            doc_key = ndb.Key(Document, int(doc_id))
            doc = doc_key.get()

        # Create the channel token
        token = channel.create_channel(doc_id + '_' + user_id)
        self.response.write(template_renderer.render('doc.html', {
            'user': user,
            'online': doc.online.values(),
            'text': doc.text,
            'token': token,
            'doc_id': doc_id,
        }))

# Update the document
class UpdateHandler(webapp2.RequestHandler):
    def post(self):
        # Get the document
        doc_id = self.request.get('doc_id')
        doc_key = ndb.Key(Document, int(doc_id))
        doc = doc_key.get()

        # Get the text
        text = self.request.get('text')

        # Get the logged in user
        user = users.get_current_user()

        # If its a valid user and document, update the text and broadcast
        if doc and user:
            doc.text = text
            doc.put()
            broadcast_to_all(doc, user.user_id(), doc_id)


# Called when a user connects to a document
class ConnectHandler(webapp2.RequestHandler):
    def post(self):
        client_id = self.request.get('from')
        parts = client_id.split('_')
        doc_id = parts[0]
        user_id = parts[1]

        iter = User.query(User.user_id == user_id).iter()
        if not iter.has_next():
            return
        user = iter.next()

        if user:
            doc_key = ndb.Key(Document, int(doc_id))
            doc = doc_key.get()
            doc.online[user_id] = user.nickname
            doc.put()
            broadcast_to_all(doc, user_id, doc_id)


# Called when a user disconnects from a document
class DisconnectHandler(webapp2.RequestHandler):
    def post(self):
        client_id = self.request.get('from')
        parts = client_id.split('_')
        doc_id = parts[0]
        user_id = parts[1]
        doc_key = ndb.Key(Document, int(doc_id))
        doc = doc_key.get()
        del doc.online[user_id]
        doc.put()
        broadcast_to_all(doc, user_id, doc_id)
