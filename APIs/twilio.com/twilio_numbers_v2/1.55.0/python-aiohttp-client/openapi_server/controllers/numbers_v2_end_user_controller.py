from typing import List, Dict
from aiohttp import web

from openapi_server.models.end_user_enum_type import EndUserEnumType
from openapi_server.models.list_end_user_response import ListEndUserResponse
from openapi_server.models.numbers_v2_regulatory_compliance_end_user import NumbersV2RegulatoryComplianceEndUser
from openapi_server import util


async def create_end_user(request: web.Request, friendly_name, type, attributes=None) -> web.Response:
    """create_end_user

    Create a new End User.

    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str
    :param type: 
    :type type: str
    :param attributes: The set of parameters that are the attributes of the End User resource which are derived End User Types.
    :type attributes: dict | bytes

    """
    attributes = object.from_dict(attributes)
    return web.Response(status=200)


async def delete_end_user(request: web.Request, sid) -> web.Response:
    """delete_end_user

    Delete a specific End User.

    :param sid: The unique string created by Twilio to identify the End User resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_end_user(request: web.Request, sid) -> web.Response:
    """fetch_end_user

    Fetch specific End User Instance.

    :param sid: The unique string created by Twilio to identify the End User resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_end_user(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_end_user

    Retrieve a list of all End User for an account.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_end_user(request: web.Request, sid, attributes=None, friendly_name=None) -> web.Response:
    """update_end_user

    Update an existing End User.

    :param sid: The unique string created by Twilio to identify the End User resource.
    :type sid: str
    :param attributes: The set of parameters that are the attributes of the End User resource which are derived End User Types.
    :type attributes: dict | bytes
    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str

    """
    attributes = object.from_dict(attributes)
    return web.Response(status=200)
