from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.facility import Facility
from openapi_server import util


async def facilities_list(request: web.Request, id=None, capability_media_type=None, capability_speed=None, capability_speed__lt=None, capability_speed__lte=None, capability_speed__gt=None, capability_speed__gte=None, organisation_name=None, metro_area=None, metro_area_network=None, address_country=None, address_locality=None, postal_code=None) -> web.Response:
    """facilities_list

    Get a (filtered) list of &#x60;facilities&#x60;.

    :param id: Filter by id
    :type id: List[str]
    :param capability_media_type: Filter by capability_media_type
    :type capability_media_type: str
    :param capability_speed: Filter by capability_speed
    :type capability_speed: int
    :param capability_speed__lt: Filter by capability_speed__lt
    :type capability_speed__lt: int
    :param capability_speed__lte: Filter by capability_speed__lte
    :type capability_speed__lte: int
    :param capability_speed__gt: Filter by capability_speed__gt
    :type capability_speed__gt: int
    :param capability_speed__gte: Filter by capability_speed__gte
    :type capability_speed__gte: int
    :param organisation_name: Filter by organisation_name
    :type organisation_name: str
    :param metro_area: Filter by metro_area
    :type metro_area: str
    :param metro_area_network: Filter by metro_area_network
    :type metro_area_network: str
    :param address_country: Filter by address_country
    :type address_country: str
    :param address_locality: Filter by address_locality
    :type address_locality: str
    :param postal_code: Filter by postal_code
    :type postal_code: str

    """
    return web.Response(status=200)


async def facilities_read(request: web.Request, id) -> web.Response:
    """facilities_read

    Retrieve a facility by id

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)
