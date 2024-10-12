from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_item_assignment_response import ListItemAssignmentResponse
from openapi_server.models.numbers_v2_regulatory_compliance_bundle_item_assignment import NumbersV2RegulatoryComplianceBundleItemAssignment
from openapi_server import util


async def create_item_assignment(request: web.Request, bundle_sid, object_sid) -> web.Response:
    """create_item_assignment

    Create a new Assigned Item.

    :param bundle_sid: The unique string that we created to identify the Bundle resource.
    :type bundle_sid: str
    :param object_sid: The SID of an object bag that holds information of the different items.
    :type object_sid: str

    """
    return web.Response(status=200)


async def delete_item_assignment(request: web.Request, bundle_sid, sid) -> web.Response:
    """delete_item_assignment

    Remove an Assignment Item Instance.

    :param bundle_sid: The unique string that we created to identify the Bundle resource.
    :type bundle_sid: str
    :param sid: The unique string that we created to identify the Identity resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_item_assignment(request: web.Request, bundle_sid, sid) -> web.Response:
    """fetch_item_assignment

    Fetch specific Assigned Item Instance.

    :param bundle_sid: The unique string that we created to identify the Bundle resource.
    :type bundle_sid: str
    :param sid: The unique string that we created to identify the Identity resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_item_assignment(request: web.Request, bundle_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_item_assignment

    Retrieve a list of all Assigned Items for an account.

    :param bundle_sid: The unique string that we created to identify the Bundle resource.
    :type bundle_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
