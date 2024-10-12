from typing import List, Dict
from aiohttp import web

from openapi_server.models.capability_information import CapabilityInformation
from openapi_server import util


async def locations_get_capability(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """locations_get_capability

    Gets subscription-level properties and limits for Data Lake Store specified by resource location.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The resource location without whitespace.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
