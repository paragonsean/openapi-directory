from typing import List, Dict
from aiohttp import web

from openapi_server.models.behavior_entity import BehaviorEntity
from openapi_server.models.status_entity import StatusEntity
from openapi_server import util


async def behavior_list_for_path(request: web.Request, path, cursor=None, per_page=None, sort_by=None, filter=None, filter_prefix=None, recursive=None, behavior=None) -> web.Response:
    """List Behaviors by path

    List Behaviors by path

    :param path: Path to operate on.
    :type path: str
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[behavior]&#x3D;desc&#x60;). Valid fields are &#x60;behavior&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;behavior&#x60;.
    :type filter: dict | bytes
    :param filter_prefix: If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;behavior&#x60;.
    :type filter_prefix: dict | bytes
    :param recursive: Show behaviors above this path?
    :type recursive: str
    :param behavior: DEPRECATED: If set only shows folder behaviors matching this behavior type. Use &#x60;filter[behavior]&#x60; instead.
    :type behavior: str

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_prefix = .from_dict(filter_prefix)
    return web.Response(status=200)


async def delete_behaviors_id(request: web.Request, id) -> web.Response:
    """Delete Behavior

    Delete Behavior

    :param id: Behavior ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_behaviors(request: web.Request, cursor=None, per_page=None, sort_by=None, behavior=None, filter=None, filter_prefix=None) -> web.Response:
    """List Behaviors

    List Behaviors

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[behavior]&#x3D;desc&#x60;). Valid fields are &#x60;behavior&#x60;.
    :type sort_by: dict | bytes
    :param behavior: If set, return records where the specified field is equal to the supplied value.
    :type behavior: str
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;behavior&#x60;.
    :type filter: dict | bytes
    :param filter_prefix: If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;behavior&#x60;.
    :type filter_prefix: dict | bytes

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_prefix = .from_dict(filter_prefix)
    return web.Response(status=200)


async def get_behaviors_id(request: web.Request, id) -> web.Response:
    """Show Behavior

    Show Behavior

    :param id: Behavior ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_behaviors_id(request: web.Request, id, attachment_delete=None, attachment_file=None, behavior=None, description=None, name=None, path=None, value=None) -> web.Response:
    """Update Behavior

    Update Behavior

    :param id: Behavior ID.
    :type id: int
    :param attachment_delete: If true, will delete the file stored in attachment
    :type attachment_delete: bool
    :param attachment_file: Certain behaviors may require a file, for instance, the \\\&quot;watermark\\\&quot; behavior requires a watermark image
    :type attachment_file: str
    :param behavior: Behavior type.
    :type behavior: str
    :param description: Description for this behavior.
    :type description: str
    :param name: Name for this behavior.
    :type name: str
    :param path: Folder behaviors path.
    :type path: str
    :param value: The value of the folder behavior.  Can be a integer, array, or hash depending on the type of folder behavior. See The Behavior Types section for example values for each type of behavior.
    :type value: str

    """
    return web.Response(status=200)


async def post_behaviors(request: web.Request, behavior, path, attachment_file=None, description=None, name=None, value=None) -> web.Response:
    """Create Behavior

    Create Behavior

    :param behavior: Behavior type.
    :type behavior: str
    :param path: Folder behaviors path.
    :type path: str
    :param attachment_file: Certain behaviors may require a file, for instance, the \\\&quot;watermark\\\&quot; behavior requires a watermark image
    :type attachment_file: str
    :param description: Description for this behavior.
    :type description: str
    :param name: Name for this behavior.
    :type name: str
    :param value: The value of the folder behavior.  Can be a integer, array, or hash depending on the type of folder behavior. See The Behavior Types section for example values for each type of behavior.
    :type value: str

    """
    return web.Response(status=200)


async def post_behaviors_webhook_test(request: web.Request, url, action=None, body=None, encoding=None, headers=None, method=None) -> web.Response:
    """Test webhook.

    Test webhook.

    :param url: URL for testing the webhook.
    :type url: str
    :param action: action for test body
    :type action: str
    :param body: Additional body parameters.
    :type body: dict | bytes
    :param encoding: HTTP encoding method.  Can be JSON, XML, or RAW (form data).
    :type encoding: str
    :param headers: Additional request headers.
    :type headers: dict | bytes
    :param method: HTTP method(GET or POST).
    :type method: str

    """
    body = object.from_dict(body)
    headers = object.from_dict(headers)
    return web.Response(status=200)
