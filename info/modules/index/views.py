from . import index_blue


@index_blue.route('/')
def index():
    return 'Index Page'
