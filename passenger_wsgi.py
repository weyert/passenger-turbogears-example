  
import sys
sys.path.append('/Users/weyertdeboer/Development/Sites/Wiki-20')
sys.stdout = sys.stderr

import os
os.environ['PYTHON_EGG_CACHE'] = '/Library/Python/2.5/site-packages'

import atexit
import cherrypy
import cherrypy._cpwsgi
import turbogears

turbogears.update_config(configfile="dev.cfg", modulename="wiki20.config")
turbogears.config.update({'global': {'server.environment': 'production'}})
turbogears.config.update({'global': {'autoreload.on': False}})
turbogears.config.update({'global': {'server.log_to_screen': False}})

import wiki20.controllers

cherrypy.root = wiki20.controllers.Root()

if cherrypy.server.state == 0:
    atexit.register(cherrypy.server.stop)
    cherrypy.server.start(init_only=True, server_class=None)

application = cherrypy._cpwsgi.wsgiApp