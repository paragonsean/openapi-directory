from typing import List, Dict
from aiohttp import web

from openapi_server.models.country_specifications import CountrySpecifications
from openapi_server.models.discoverable_participant import DiscoverableParticipant
from openapi_server.models.discovered_participant import DiscoveredParticipant
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def discovery_exists(request: web.Request, body) -> web.Response:
    """Discover Network Participant Existence

    Discover if a network participant exists.

    :param body: The participant to check
    :type body: dict | bytes

    """
    body = DiscoverableParticipant.from_dict(body)
    return web.Response(status=200)


async def discovery_identifiers(request: web.Request, ) -> web.Response:
    """Discover Country Identifiers ** EXPERIMENTAL

    Discover the identifiers used in each country, for routing, for legal identification as well as for tax identification purposes. We are currently testing this endpoint with selected Customers. If you would like to participate, please contact us.


    """
    return web.Response(status=200)


async def discovery_receives(request: web.Request, body) -> web.Response:
    """Disover Network Participant

    Discover a network participant and capabilities.

    :param body: The participant to check
    :type body: dict | bytes

    """
    body = DiscoverableParticipant.from_dict(body)
    return web.Response(status=200)
