from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def view_test(request):
    """defines the return view"""
    return Response('<h1>Hola From Pyramid!</h1>')

"""main function definition"""
if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('root', '/')                   #adding route
        config.add_view(view_test, route_name='root')   #define route block
        app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 6543, app)
    server.serve_forever()