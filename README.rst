What
====

A server for use with `TiddlyWeb <http://tiddlyweb.com>`_.

The base install of TiddlyWeb can be run with ``wsgiref`` simple
server but that server is slow and has some issues with encoding
of request URIs. This server uses the wsgiserver from the `CherryPy
<http://www.cherrypy.org>`_ project to provide a faster and more
compliant server.

This code is tested with Python 2.7 and 3.3.

Use
===

In an already existing `instance
<http://tiddlyweb.tiddlyspace.com/instance>`_ adjust
``tiddlywebconfig.py`` to include:::

    'wsgi_server': 'tiddlywebplugins.cherrypy'
