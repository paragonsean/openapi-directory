from typing import List, Dict
from aiohttp import web

from openapi_server.models.sentry_impact_risk_object import SentryImpactRiskObject
from openapi_server.models.sentry_object_paging_dto import SentryObjectPagingDto
from openapi_server import util


async def retrieve_sentry_risk_data(request: web.Request, is_active=None, page=None, size=None) -> web.Response:
    """Retrieve Sentry (Impact Risk ) Near Earth Objects

    Retrieves Near Earth Objects listed in the NASA sentry data set

    :param is_active: show current list of Sentry objects, or show removed Sentry objects
    :type is_active: bool
    :param page: page
    :type page: int
    :param size: size
    :type size: int

    """
    return web.Response(status=200)


async def retrieve_sentry_risk_data_by_id(request: web.Request, asteroid_id) -> web.Response:
    """Retrieve Sentry (Impact Risk ) Near Earth Objectby ID 

    Retrieves Sentry Near Earth Object by ID

    :param asteroid_id: ID of NearEarth object.  ID can be SPK_ID, Asteroid des (designation) or Sentry ID
    :type asteroid_id: str

    """
    return web.Response(status=200)
