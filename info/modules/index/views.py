from . import index_blue
from info import redis_store


@index_blue.route('/')
def index():
    redis_store.set("language", "python")
    return 'Index Page'
