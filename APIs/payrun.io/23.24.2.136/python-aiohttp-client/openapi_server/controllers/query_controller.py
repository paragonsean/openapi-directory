from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.query import Query
from openapi_server import util


async def get_query_response(request: web.Request, authorization, api_version, body) -> web.Response:
    """Get the query result

    Get the results for the specified query

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The query object to be executed against the application data.
    :type body: dict | bytes

    """
    body = Query.from_dict(body)
    return web.Response(status=200)
