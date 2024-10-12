from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_type_model import AccountTypeModel
from openapi_server.models.account_types_model import AccountTypesModel
from openapi_server import util


async def account_types_get_by_country(request: web.Request, country) -> web.Response:
    """account_types_get_by_country

    Description: This operation retrieves all Account Types for the specified country.&lt;br /&gt;                Purpose: Provides access to the Account Types including id and type description.

    :param country: The country used to filter Account Types
    :type country: str

    """
    return web.Response(status=200)


async def account_types_get_by_id(request: web.Request, id) -> web.Response:
    """account_types_get_by_id

    Description: This operation retrieves all Account Types for the specified id.&lt;br /&gt;                Purpose: Provides access to the Account Types including id and type description.

    :param id: The ID of Account Type used to retreive the Account Type information
    :type id: int

    """
    return web.Response(status=200)
