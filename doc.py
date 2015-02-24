from modules.doc_handler import DocHandler
from modules.doc_handler import ConnectHandler
from modules.doc_handler import DisconnectHandler
from modules.doc_handler import UpdateHandler

import webapp2

application = webapp2.WSGIApplication([
    ('/', DocHandler),
    ('/_ah/channel/connected/', ConnectHandler),
    ('/_ah/channel/disconnected/', DisconnectHandler),
    ('/update', UpdateHandler),
], debug=True)
