from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world1(request):
    """to make this works.. change
            config.add_route('view', '/view/')
     with: config.add_route('view', '/view/{info}')
      and config.add_view(hello_world1
      with: config.add_view(hello_world2
    """
    return Response('Hello %(info)s !' % request.matchdict)

def hello_world2(request):
    # Some parameters from a request such as /?name=something
    url = request.url
    name = request.params.get('name', 'No Name Provided')

    body = 'URL %s with name: %s' % (url, name)
    return Response(
        content_type="text/plain",
        body=body
    )


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('view', '/view/')
        config.add_view(hello_world2, route_name='view')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()