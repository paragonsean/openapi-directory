from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_merchant_user_request import CreateMerchantUserRequest
from openapi_server.models.create_user_response import CreateUserResponse
from openapi_server.models.list_merchant_users_response import ListMerchantUsersResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.update_merchant_user_request import UpdateMerchantUserRequest
from openapi_server.models.user import User
from openapi_server import util


async def get_merchants_merchant_id_users(request: web.Request, merchant_id, page_number=None, page_size=None, username=None) -> web.Response:
    """Get a list of users

    Returns a list of users associated with the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

    :param merchant_id: Unique identifier of the merchant.
    :type merchant_id: str
    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page.
    :type page_size: int
    :param username: The partial or complete username to select all users that match.
    :type username: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_users_user_id(request: web.Request, merchant_id, user_id) -> web.Response:
    """Get user details

    Returns user details for the &#x60;userId&#x60; and the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

    :param merchant_id: Unique identifier of the merchant.
    :type merchant_id: str
    :param user_id: Unique identifier of the user.
    :type user_id: str

    """
    return web.Response(status=200)


async def patch_merchants_merchant_id_users_user_id(request: web.Request, merchant_id, user_id, body=None) -> web.Response:
    """Update a user

    Updates user details for the &#x60;userId&#x60; and the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

    :param merchant_id: Unique identifier of the merchant.
    :type merchant_id: str
    :param user_id: Unique identifier of the user.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateMerchantUserRequest.from_dict(body)
    return web.Response(status=200)


async def post_merchants_merchant_id_users(request: web.Request, merchant_id, body=None) -> web.Response:
    """Create a new user

    Creates a user for the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

    :param merchant_id: Unique identifier of the merchant.
    :type merchant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateMerchantUserRequest.from_dict(body)
    return web.Response(status=200)
