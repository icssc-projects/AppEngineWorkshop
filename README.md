# AppEngineWorkshop

This is the completed source code for the AppEngine workshop.
It features the usage of several AppEngine api's and is a working python web server.

The web app is a very light (and less powerful) Google Doc-like application. Users, once logged in, a new document
will be created for the user. Every logged in user on the same document will be able to see each other
and can edit the text area at the same time. Some limitations are the inefficient means of sending document updates and
the corresponding "glitch" that updates to the document can make simultaneouse edits (and your cursor) jump. For the sake
of time, these won't be addressed during the workshop; however, it may be an interesting (and pretty challenging) exercise to
try to fix these problems on your own.

It uses the Users Api to log in users, the DataStore Api to store user and document data, and the Channel Api to support
live updates on documents.
