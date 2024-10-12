from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_dialing_permissions_hrs_prefixes_response import ListDialingPermissionsHrsPrefixesResponse
from openapi_server import util


async def list_dialing_permissions_hrs_prefixes(request: web.Request, iso_code, page_size=None, page=None, page_token=None) -> web.Response:
    """list_dialing_permissions_hrs_prefixes

    Fetch the high-risk special services prefixes from the country resource corresponding to the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

    :param iso_code: The [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to identify the country permissions from which high-risk special service number prefixes are fetched
    :type iso_code: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
