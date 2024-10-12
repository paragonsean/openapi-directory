from typing import List, Dict
from aiohttp import web

from openapi_server.models.tag_details import TagDetails
from openapi_server.models.tag_value import TagValue
from openapi_server.models.tags_list_result import TagsListResult
from openapi_server import util


async def tags_create_or_update(request: web.Request, tag_name, api_version, subscription_id) -> web.Response:
    """tags_create_or_update

    Create a subscription resource tag.

    :param tag_name: The name of the tag.
    :type tag_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tags_create_or_update_value(request: web.Request, tag_name, tag_value, api_version, subscription_id) -> web.Response:
    """tags_create_or_update_value

    Create a subscription resource tag value.

    :param tag_name: The name of the tag.
    :type tag_name: str
    :param tag_value: The value of the tag.
    :type tag_value: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tags_delete(request: web.Request, tag_name, api_version, subscription_id) -> web.Response:
    """tags_delete

    Delete a subscription resource tag.

    :param tag_name: The name of the tag.
    :type tag_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tags_delete_value(request: web.Request, tag_name, tag_value, api_version, subscription_id) -> web.Response:
    """tags_delete_value

    Delete a subscription resource tag value.

    :param tag_name: The name of the tag.
    :type tag_name: str
    :param tag_value: The value of the tag.
    :type tag_value: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tags_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """tags_list

    Get a list of subscription resource tags.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)
