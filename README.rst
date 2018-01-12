What
====

A server for use with `TiddlyWeb <http://tiddlyweb.com>`_.

The base install of TiddlyWeb can be run with ``wsgiref`` simple
server but that server is slow and has some issues with encoding
of request URIs. This server uses the wsgiserver, `Cheroot
<https://github.com/cherrypy/cheroot>`_, which comes from the `CherryPy
<http://www.cherrypy.org>`_ project. It provides a faster and more
WSGI and HTTP compliant server.

This code is tested with Python 2.7 and 3.5.

Use
===

In an already existing `instance
<https://tank.peermore.com/tanks/tiddlyweb/instance>`_ adjust
``tiddlywebconfig.py`` to include:::

    'wsgi_server': 'tiddlywebplugins.cherrypy'
