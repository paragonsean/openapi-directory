from typing import List, Dict
from aiohttp import web

from openapi_server.models.asc_location import AscLocation
from openapi_server.models.asc_location_list import AscLocationList
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def locations_get(request: web.Request, api_version, subscription_id, asc_location) -> web.Response:
    """locations_get

    Details of a specific location

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
    :type asc_location: str

    """
    return web.Response(status=200)


async def locations_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """locations_list

    The location of the responsible ASC of the specific subscription (home region). For each subscription there is only one responsible location. The location in the response should be used to read or write other resources in ASC according to their ID.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)
