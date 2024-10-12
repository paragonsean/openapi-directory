from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.application import Application
from openapi_server.models.application_request import ApplicationRequest
from openapi_server.models.paged_list_response import PagedListResponse
from openapi_server.models.tier import Tier
from openapi_server.models.tier_list_response import TierListResponse
from openapi_server.models.tier_request import TierRequest
from openapi_server import util


async def add_application(request: web.Request, body) -> web.Response:
    """Create an application

    Application is a group of tiers. A tier is a group of virtual machines based on membership criteria. Tiers are bound to single application. An application name is unique and should not conflict with another application name.

    :param body: 
    :type body: dict | bytes

    """
    body = ApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def add_tier(request: web.Request, id, body) -> web.Response:
    """Create tier in application

    Create a tier of an application by with specified membership criteria. The membership criteria id defined in terms of virtual machines or ip addresses/subnet. Please refer to API Guide on how to construct membership criteria.

    :param id: entity id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TierRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application(request: web.Request, id) -> web.Response:
    """Delete an application

    Deleting an application deletes all the tiers of the application along with the application

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def delete_tier(request: web.Request, id, tier_id) -> web.Response:
    """Delete tier

    Delete tier of an application

    :param id: entity id
    :type id: str
    :param tier_id: 
    :type tier_id: str

    """
    return web.Response(status=200)


async def get_application(request: web.Request, id) -> web.Response:
    """Show application details

    Show application details

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def get_application_tier(request: web.Request, id, tier_id) -> web.Response:
    """Show tier details

    Show tier details

    :param id: entity id
    :type id: str
    :param tier_id: 
    :type tier_id: str

    """
    return web.Response(status=200)


async def get_tier(request: web.Request, tier_id, authorization) -> web.Response:
    """Show tier details

    Show tier details

    :param tier_id: 
    :type tier_id: str
    :param authorization: Authorization Header
    :type authorization: str

    """
    return web.Response(status=200)


async def list_application_tiers(request: web.Request, id) -> web.Response:
    """List tiers of an application

    List tiers of an application

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def list_applications(request: web.Request, size=None, cursor=None, start_time=None, end_time=None) -> web.Response:
    """List applications

    List applications

    :param size: page size of results
    :type size: 
    :param cursor: cursor from previous response
    :type cursor: str
    :param start_time: start time for query in epoch seconds
    :type start_time: 
    :param end_time: end time for query in epoch seconds
    :type end_time: 

    """
    return web.Response(status=200)
