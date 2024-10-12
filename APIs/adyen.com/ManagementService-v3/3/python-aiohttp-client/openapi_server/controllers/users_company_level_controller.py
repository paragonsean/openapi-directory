from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_user import CompanyUser
from openapi_server.models.create_company_user_request import CreateCompanyUserRequest
from openapi_server.models.create_company_user_response import CreateCompanyUserResponse
from openapi_server.models.list_company_users_response import ListCompanyUsersResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.update_company_user_request import UpdateCompanyUserRequest
from openapi_server import util


async def get_companies_company_id_users(request: web.Request, company_id, page_number=None, page_size=None, username=None) -> web.Response:
    """Get a list of users

    Returns the list of users for the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param page_number: The number of the page to return.
    :type page_number: int
    :param page_size: The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page.
    :type page_size: int
    :param username: The partial or complete username to select all users that match.
    :type username: str

    """
    return web.Response(status=200)


async def get_companies_company_id_users_user_id(request: web.Request, company_id, user_id) -> web.Response:
    """Get user details

    Returns user details for the &#x60;userId&#x60; and the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param user_id: The unique identifier of the user.
    :type user_id: str

    """
    return web.Response(status=200)


async def patch_companies_company_id_users_user_id(request: web.Request, company_id, user_id, body=None) -> web.Response:
    """Update user details

    Updates user details for the &#x60;userId&#x60; and the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param user_id: The unique identifier of the user.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateCompanyUserRequest.from_dict(body)
    return web.Response(status=200)


async def post_companies_company_id_users(request: web.Request, company_id, body=None) -> web.Response:
    """Create a new user

    Creates the user for the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCompanyUserRequest.from_dict(body)
    return web.Response(status=200)
