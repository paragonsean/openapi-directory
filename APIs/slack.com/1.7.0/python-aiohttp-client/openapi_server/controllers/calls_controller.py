from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def calls_add(request: web.Request, token, external_unique_id, join_url, created_by=None, date_start=None, desktop_app_join_url=None, external_display_id=None, title=None, users=None) -> web.Response:
    """calls_add

    Registers a new Call.

    :param token: Authentication token. Requires scope: &#x60;calls:write&#x60;
    :type token: str
    :param external_unique_id: An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from that service.
    :type external_unique_id: str
    :param join_url: The URL required for a client to join the Call.
    :type join_url: str
    :param created_by: The valid Slack user ID of the user who created this Call. When this method is called with a user token, the &#x60;created_by&#x60; field is optional and defaults to the authed user of the token. Otherwise, the field is required.
    :type created_by: str
    :param date_start: Call start time in UTC UNIX timestamp format
    :type date_start: int
    :param desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.
    :type desktop_app_join_url: str
    :param external_display_id: An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied, this ID will be displayed in the Call object.
    :type external_display_id: str
    :param title: The name of the Call.
    :type title: str
    :param users: The list of users to register as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
    :type users: str

    """
    return web.Response(status=200)


async def calls_end(request: web.Request, token, id, duration=None) -> web.Response:
    """calls_end

    Ends a Call.

    :param token: Authentication token. Requires scope: &#x60;calls:write&#x60;
    :type token: str
    :param id: &#x60;id&#x60; returned when registering the call using the [&#x60;calls.add&#x60;](/methods/calls.add) method.
    :type id: str
    :param duration: Call duration in seconds
    :type duration: int

    """
    return web.Response(status=200)


async def calls_info(request: web.Request, token, id) -> web.Response:
    """calls_info

    Returns information about a Call.

    :param token: Authentication token. Requires scope: &#x60;calls:read&#x60;
    :type token: str
    :param id: &#x60;id&#x60; of the Call returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method.
    :type id: str

    """
    return web.Response(status=200)


async def calls_participants_add_0(request: web.Request, token, id, users) -> web.Response:
    """calls_participants_add_0

    Registers new participants added to a Call.

    :param token: Authentication token. Requires scope: &#x60;calls:write&#x60;
    :type token: str
    :param id: &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method.
    :type id: str
    :param users: The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
    :type users: str

    """
    return web.Response(status=200)


async def calls_participants_remove_0(request: web.Request, token, id, users) -> web.Response:
    """calls_participants_remove_0

    Registers participants removed from a Call.

    :param token: Authentication token. Requires scope: &#x60;calls:write&#x60;
    :type token: str
    :param id: &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method.
    :type id: str
    :param users: The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
    :type users: str

    """
    return web.Response(status=200)


async def calls_update(request: web.Request, token, id, desktop_app_join_url=None, join_url=None, title=None) -> web.Response:
    """calls_update

    Updates information about a Call.

    :param token: Authentication token. Requires scope: &#x60;calls:write&#x60;
    :type token: str
    :param id: &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method.
    :type id: str
    :param desktop_app_join_url: When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.
    :type desktop_app_join_url: str
    :param join_url: The URL required for a client to join the Call.
    :type join_url: str
    :param title: The name of the Call.
    :type title: str

    """
    return web.Response(status=200)
