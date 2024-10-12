from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_hal_response import UserHalResponse
from openapi_server.models.users_hal_response import UsersHalResponse
from openapi_server.models.validation_errors_response import ValidationErrorsResponse
from openapi_server import util


async def user_ctrl_get_user_by_id(request: web.Request, account_id, user_id) -> web.Response:
    """Get user data by account ID and user ID

    

    :param account_id: The Vonage Business Cloud account ID
    :type account_id: str
    :param user_id: The Vonage Business Cloud user ID
    :type user_id: 

    """
    return web.Response(status=200)


async def user_ctrl_get_users(request: web.Request, account_id, page_size=None, page=None, first_name=None, last_name=None, login_name=None, email=None) -> web.Response:
    """Get account users data by account ID

    

    :param account_id: The Vonage Business Cloud account ID
    :type account_id: str
    :param page_size: Number of records per page
    :type page_size: 
    :param page: Current page number
    :type page: 
    :param first_name: Filter by first name
    :type first_name: str
    :param last_name: Filter by last name
    :type last_name: str
    :param login_name: Filter by login name
    :type login_name: str
    :param email: Filter by email address
    :type email: str

    """
    return web.Response(status=200)
