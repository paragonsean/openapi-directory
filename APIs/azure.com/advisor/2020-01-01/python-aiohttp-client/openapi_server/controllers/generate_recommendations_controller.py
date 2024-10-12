from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def recommendations_generate(request: web.Request, subscription_id, api_version) -> web.Response:
    """recommendations_generate

    Initiates the recommendation generation or computation process for a subscription. This operation is asynchronous. The generated recommendations are stored in a cache in the Advisor service.

    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def recommendations_get_generate_status(request: web.Request, subscription_id, operation_id, api_version) -> web.Response:
    """recommendations_get_generate_status

    Retrieves the status of the recommendation computation or generation process. Invoke this API after calling the generation recommendation. The URI of this API is returned in the Location field of the response header.

    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param operation_id: The operation ID, which can be found from the Location field in the generate recommendation response header.
    :type operation_id: str
    :type operation_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
