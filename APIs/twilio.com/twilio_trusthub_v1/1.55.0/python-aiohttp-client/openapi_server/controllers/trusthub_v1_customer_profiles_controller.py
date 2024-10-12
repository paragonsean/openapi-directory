from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_profile_enum_status import CustomerProfileEnumStatus
from openapi_server.models.list_customer_profile_response import ListCustomerProfileResponse
from openapi_server.models.trusthub_v1_customer_profile import TrusthubV1CustomerProfile
from openapi_server import util


async def create_customer_profile(request: web.Request, email, friendly_name, policy_sid, status_callback=None) -> web.Response:
    """create_customer_profile

    Create a new Customer-Profile.

    :param email: The email address that will receive updates when the Customer-Profile resource changes status.
    :type email: str
    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str
    :param policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
    :type policy_sid: str
    :param status_callback: The URL we call to inform your application of status changes.
    :type status_callback: str

    """
    return web.Response(status=200)


async def delete_customer_profile(request: web.Request, sid) -> web.Response:
    """delete_customer_profile

    Delete a specific Customer-Profile.

    :param sid: The unique string that we created to identify the Customer-Profile resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_customer_profile(request: web.Request, sid) -> web.Response:
    """fetch_customer_profile

    Fetch a specific Customer-Profile instance.

    :param sid: The unique string that we created to identify the Customer-Profile resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_customer_profile(request: web.Request, status=None, friendly_name=None, policy_sid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_customer_profile

    Retrieve a list of all Customer-Profiles for an account.

    :param status: The verification status of the Customer-Profile resource.
    :type status: str
    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str
    :param policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
    :type policy_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_customer_profile(request: web.Request, sid, email=None, friendly_name=None, status=None, status_callback=None) -> web.Response:
    """update_customer_profile

    Updates a Customer-Profile in an account.

    :param sid: The unique string that we created to identify the Customer-Profile resource.
    :type sid: str
    :param email: The email address that will receive updates when the Customer-Profile resource changes status.
    :type email: str
    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str
    :param status: 
    :type status: str
    :param status_callback: The URL we call to inform your application of status changes.
    :type status_callback: str

    """
    return web.Response(status=200)
