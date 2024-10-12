from typing import List, Dict
from aiohttp import web

from openapi_server.models.end_user_route_hal_response import EndUserRouteHalResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.validation_errors_response import ValidationErrorsResponse
from openapi_server import util


async def extension_ctrl_get_account_extension_by_id(request: web.Request, account_id, extension_number) -> web.Response:
    """Get extension data by account ID and extension number

    

    :param account_id: The Vonage Business Cloud account ID
    :type account_id: str
    :param extension_number: The extension number
    :type extension_number: 

    """
    return web.Response(status=200)


async def extension_ctrl_get_account_extensions(request: web.Request, account_id, page_size=None, page=None, location_id=None, phone_number=None, login_name=None, email=None) -> web.Response:
    """Get account extensions data by account ID

    

    :param account_id: The Vonage Business Cloud account ID
    :type account_id: str
    :param page_size: Number of records per page
    :type page_size: 
    :param page: Current page number
    :type page: 
    :param location_id: Filter by location id
    :type location_id: 
    :param phone_number: Filter by phone number
    :type phone_number: str
    :param login_name: Filter by login name
    :type login_name: str
    :param email: Filter by email address
    :type email: str

    """
    return web.Response(status=200)
