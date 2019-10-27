from sanic import Sanic
from sanic import response
from sanic.exceptions import abort

app = Sanic(__name__)


@app.route("/search")
async def test(request):
    if 'text' not in request.args:
        abort(400)
    return response.json({"test": True})