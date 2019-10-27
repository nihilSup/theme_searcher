import logging

from sanic import Sanic, response
from sanic.exceptions import abort

from .searcher import Searcher

app = Sanic(__name__)


@app.listener('before_server_start')
async def init_searcher(app, loop):
    # Searcher is built here to ensure fast module import
    logging.info('Building search indexes')
    searcher = Searcher({
        'новости': ['деревья на Садовом кольце', 'добрый автобус',
                    'выставка IT-технологий'],
        'кухня': ['рецепт борща', 'яблочный пирог', 'тайская кухня'],
        'товары': ['Дети капитана Гранта', 'зимние шины', 'Тайская кухня'],
    })
    logging.info('Finished')

    # I can implement searcher asynchronously but decided to separate 
    # implementation details and business rules. So I need async wrapper
    async def search(text):
        return searcher(text)

    app.search = search


@app.route("/search")
async def test(request):
    try:
        text = request.args['text']
    except KeyError:
        abort(400)
    else:
        res = await app.search(text[0])
        return response.json(res)
