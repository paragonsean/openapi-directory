from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def logs_app_id_drains_get_0(request: web.Request, app_id) -> web.Response:
    """logs_app_id_drains_get_0

    Fetch the logs drains for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def logs_app_id_drains_id_or_url_delete_0(request: web.Request, app_id) -> web.Response:
    """logs_app_id_drains_id_or_url_delete_0

    Delete the logs drain by id or url for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def logs_app_id_drains_id_or_url_get_0(request: web.Request, app_id) -> web.Response:
    """logs_app_id_drains_id_or_url_get_0

    Fetch the logs drain by id or url for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def logs_app_id_drains_post_0(request: web.Request, app_id) -> web.Response:
    """logs_app_id_drains_post_0

    Add a log drain for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def logs_app_id_get_0(request: web.Request, app_id, limit=None, order=None, after=None, before=None, filter=None, deployment_id=None) -> web.Response:
    """logs_app_id_get_0

    Fetch the logs for a given application

    :param app_id: Application Id
    :type app_id: str
    :param limit: Number of lines to return
    :type limit: int
    :param order: Logs order
    :type order: str
    :param after: Lowest bound for logs date, ISO 8601
    :type after: str
    :param before: Highest bounds for logs date, ISO 8601
    :type before: str
    :param filter: A pattern to filter with
    :type filter: str
    :param deployment_id: Only fetch logs emitted by this deployment
    :type deployment_id: str

    """
    after = util.deserialize_datetime(after)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def logs_app_id_sse_get_0(request: web.Request, app_id) -> web.Response:
    """logs_app_id_sse_get_0

    Retrieve logs as they come through a sse connection. To have authorization, you have to add &#x60;authorization&#x3D;oAuthAuthorizationString&#x60; as query param.

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def logs_drains_drain_id_put_0(request: web.Request, drain_id) -> web.Response:
    """logs_drains_drain_id_put_0

    Fetch all the logs drains (ccadmin dedicated route)

    :param drain_id: Automatically added
    :type drain_id: str

    """
    return web.Response(status=200)


async def logs_drains_get_0(request: web.Request, ) -> web.Response:
    """logs_drains_get_0

    Fetch all the logs drains (ccadmin dedicated route)


    """
    return web.Response(status=200)


async def logs_logs_chunked_app_id_get_0(request: web.Request, app_id, download=None) -> web.Response:
    """logs_logs_chunked_app_id_get_0

    Retrieve logs as they come through a chunked, never-ending response

    :param app_id: Application Id
    :type app_id: str
    :param download: Tell the user-agent to download the body as a file
    :type download: bool

    """
    return web.Response(status=200)


async def logs_logs_socket_app_id_get_0(request: web.Request, app_id, since=None, filter=None, deployment_id=None) -> web.Response:
    """logs_logs_socket_app_id_get_0

    Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

    :param app_id: Application Id
    :type app_id: str
    :param since: Only fetch logs newer than this (ISO-8601 formatted) date
    :type since: str
    :param filter: A pattern to filter with
    :type filter: str
    :param deployment_id: Only fetch logs emitted by this deployment
    :type deployment_id: str

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def v3_logs_app_id_drains_get_0(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_drains_get_0

    Fetch the logs drains for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_drains_id_or_url_delete_0(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_drains_id_or_url_delete_0

    Delete the logs drain by id or url for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_drains_id_or_url_get_0(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_drains_id_or_url_get_0

    Fetch the logs drain by id or url for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_drains_post_0(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_drains_post_0

    Add a log drain for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_get_0(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_get_0

    Fetch the logs for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_logs_chunked_get_0(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_logs_chunked_get_0

    Retrieve logs as they come through a chunked, never-ending response

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_logs_socket_get_0(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_logs_socket_get_0

    Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)
