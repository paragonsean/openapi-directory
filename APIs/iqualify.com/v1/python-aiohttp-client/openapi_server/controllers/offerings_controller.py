from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.offering import Offering
from openapi_server.models.offering_metadata_response import OfferingMetadataResponse
from openapi_server.models.offering_required import OfferingRequired
from openapi_server.models.portfolio_activations import PortfolioActivations
from openapi_server import util


async def offerings_current_get(request: web.Request, ) -> web.Response:
    """Find active offerings

    Responds with active offerings for your organisation.


    """
    return web.Response(status=200)


async def offerings_future_get(request: web.Request, ) -> web.Response:
    """Find scheduled offerings

    Responds with scheduled offerings for your organisation. Scheduled offerings have a start date after today&#39;s date (inclusive).


    """
    return web.Response(status=200)


async def offerings_get(request: web.Request, ) -> web.Response:
    """Find current, past and future offerings

    Responds with all offerings for your organisation.


    """
    return web.Response(status=200)


async def offerings_info_text_pattern_get(request: web.Request, text_pattern) -> web.Response:
    """Find offerings where info field matches the specified textPattern

    Find offerings where info field matches the specified text pattern.

    :param text_pattern: Text pattern to search for (minimum of 3 characters length).
    :type text_pattern: str

    """
    return web.Response(status=200)


async def offerings_offering_id_get(request: web.Request, offering_id) -> web.Response:
    """Find offering by ID

    Responds with an offering matching the offeringId.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_patch(request: web.Request, offering_id, body) -> web.Response:
    """Update offering

    Updates the offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Offering.from_dict(body)
    return web.Response(status=200)


async def offerings_past_get(request: web.Request, ) -> web.Response:
    """Find past offerings

    Responds with past offerings for your organisation.


    """
    return web.Response(status=200)


async def offerings_post(request: web.Request, body) -> web.Response:
    """Create offering

    Creates a new offering.

    :param body: 
    :type body: dict | bytes

    """
    body = OfferingRequired.from_dict(body)
    return web.Response(status=200)


async def offerings_summary_get(request: web.Request, top=None, orderby=None, filter=None) -> web.Response:
    """Offerings summary

    Responds with a summary of all offerings for your organisation.

    :param top: Returns only the first n results.
    :type top: str
    :param orderby: Sorts the results.
    :type orderby: str
    :param filter: Filters the results, based on a Boolean condition.
    :type filter: str

    """
    return web.Response(status=200)
