from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_ui_openwindow_newmail_new_mail import PostUiOpenwindowNewmailNewMail
from openapi_server.models.post_ui_openwindow_newmail_unprocessable_entity import PostUiOpenwindowNewmailUnprocessableEntity
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def post_ui_autopilot_waypoint(request: web.Request, add_to_beginning, clear_other_waypoints, destination_id, datasource=None, token=None) -> web.Response:
    """Set Autopilot Waypoint

    Set a solar system as autopilot waypoint  --- Alternate route: &#x60;/dev/ui/autopilot/waypoint/&#x60;  Alternate route: &#x60;/v2/ui/autopilot/waypoint/&#x60; 

    :param add_to_beginning: Whether this solar system should be added to the beginning of all waypoints
    :type add_to_beginning: bool
    :param clear_other_waypoints: Whether clean other waypoints beforing adding this one
    :type clear_other_waypoints: bool
    :param destination_id: The destination to travel to, can be solar system, station or structure&#39;s id
    :type destination_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def post_ui_openwindow_contract(request: web.Request, contract_id, datasource=None, token=None) -> web.Response:
    """Open Contract Window

    Open the contract window inside the client  --- Alternate route: &#x60;/dev/ui/openwindow/contract/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/contract/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/contract/&#x60; 

    :param contract_id: The contract to open
    :type contract_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def post_ui_openwindow_information(request: web.Request, target_id, datasource=None, token=None) -> web.Response:
    """Open Information Window

    Open the information window for a character, corporation or alliance inside the client  --- Alternate route: &#x60;/dev/ui/openwindow/information/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/information/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/information/&#x60; 

    :param target_id: The target to open
    :type target_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def post_ui_openwindow_marketdetails(request: web.Request, type_id, datasource=None, token=None) -> web.Response:
    """Open Market Details

    Open the market details window for a specific typeID inside the client  --- Alternate route: &#x60;/dev/ui/openwindow/marketdetails/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/marketdetails/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/marketdetails/&#x60; 

    :param type_id: The item type to open in market window
    :type type_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def post_ui_openwindow_newmail(request: web.Request, new_mail, datasource=None, token=None) -> web.Response:
    """Open New Mail Window

    Open the New Mail window, according to settings from the request if applicable  --- Alternate route: &#x60;/dev/ui/openwindow/newmail/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/newmail/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/newmail/&#x60; 

    :param new_mail: The details of mail to create
    :type new_mail: dict | bytes
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    new_mail = PostUiOpenwindowNewmailNewMail.from_dict(new_mail)
    return web.Response(status=200)
