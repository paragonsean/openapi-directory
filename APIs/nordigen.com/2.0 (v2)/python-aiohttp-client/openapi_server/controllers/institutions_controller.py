from typing import List, Dict
from aiohttp import web

from openapi_server.models.integration import Integration
from openapi_server.models.integration_retrieve import IntegrationRetrieve
from openapi_server import util


async def retrieve_all_supported_institutions_in_a_given_country(request: web.Request, country=None, payments_enabled=None) -> web.Response:
    """retrieve_all_supported_institutions_in_a_given_country

    List all available institutions

    :param country: ISO 3166 two-character country code
    :type country: str
    :param payments_enabled: Boolean value, indicating if payments are enabled
    :type payments_enabled: str

    """
    return web.Response(status=200)


async def retrieve_institution(request: web.Request, id) -> web.Response:
    """retrieve_institution

    Get details about a specific Institution

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
