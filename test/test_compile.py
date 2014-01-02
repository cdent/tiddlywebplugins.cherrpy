


def test_compile():
    try:
        import tiddlywebplugins.cherrypy
        assert True
    except ImportError as exc:
        assert False, exc
