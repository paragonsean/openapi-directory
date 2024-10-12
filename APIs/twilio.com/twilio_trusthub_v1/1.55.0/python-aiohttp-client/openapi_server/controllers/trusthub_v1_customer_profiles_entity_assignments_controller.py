from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_customer_profile_entity_assignment_response import ListCustomerProfileEntityAssignmentResponse
from openapi_server.models.trusthub_v1_customer_profile_customer_profile_entity_assignment import TrusthubV1CustomerProfileCustomerProfileEntityAssignment
from openapi_server import util


async def create_customer_profile_entity_assignment(request: web.Request, customer_profile_sid, object_sid) -> web.Response:
    """create_customer_profile_entity_assignment

    Create a new Assigned Item.

    :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
    :type customer_profile_sid: str
    :param object_sid: The SID of an object bag that holds information of the different items.
    :type object_sid: str

    """
    return web.Response(status=200)


async def delete_customer_profile_entity_assignment(request: web.Request, customer_profile_sid, sid) -> web.Response:
    """delete_customer_profile_entity_assignment

    Remove an Assignment Item Instance.

    :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
    :type customer_profile_sid: str
    :param sid: The unique string that we created to identify the Identity resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_customer_profile_entity_assignment(request: web.Request, customer_profile_sid, sid) -> web.Response:
    """fetch_customer_profile_entity_assignment

    Fetch specific Assigned Item Instance.

    :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
    :type customer_profile_sid: str
    :param sid: The unique string that we created to identify the Identity resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_customer_profile_entity_assignment(request: web.Request, customer_profile_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_customer_profile_entity_assignment

    Retrieve a list of all Assigned Items for an account.

    :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
    :type customer_profile_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
