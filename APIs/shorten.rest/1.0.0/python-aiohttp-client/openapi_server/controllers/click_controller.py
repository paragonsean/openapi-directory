from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_clicks_model import GetClicksModel
from openapi_server import util


async def get_clicks(request: web.Request, continue_from=None, limit=None) -> web.Response:
    """Get clicks

    Retrieve the raw click data for your account. Clicks are retrieved by creation date in descending order.    If there are more results than the limit for the request the response will return you a value in lastId property you can specify it in the continueFrom query parameter to get the next batch of records.

    :param continue_from: An ID returned by a previous query to continue clicks retrieval (see lastId in response)
    :type continue_from: str
    :param limit: Number of results to return per request
    :type limit: int

    """
    return web.Response(status=200)
