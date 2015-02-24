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

The layout of the project is as follows

* .gitignore - Used to tell git which files to not include (compiled python files) Not relevant or needed for AppEngine
* README.md - The current file you are reading, not relevant or needed for AppEngine
* app.yaml - The configuration file that tells AppEngine how to configure your project
* doc.py - The python script to run when your app starts, it contains the path mapping from url paths ('/', or '/update') to 
your python code
* run.bat - A windows script used to start up the server, not needed for AppEngine, but is useful
* update.bat - A windows script used to load your app to AppEngine, not needed for AppEngine, but is useful
* modules/ - The directory containing the majority of our python code, it is configured as a module so it can be imported
  * \_\_init\_\_.py - A place holder file for the modules directory that tells python that this directory is a module
  * doc_handler.py - The code for handling all client requests
  * document.py - The data model used for a document
  * template_renderer.py - Used to make rendering templates easier
  * user.py - The data model used for a user
* static/ - The folder used to contain all static files. Files like audio, images, javascript, and css will be stored here.
  * js/doc.js - The javascript file used to set up and control the channel api on the client side.
* templates/ - The folder that contains all the template files. Template files are html files that contain special sections
where data can be inserted by the python server.
  * doc.html - The Jinja template file for the one and only page of the web app.

