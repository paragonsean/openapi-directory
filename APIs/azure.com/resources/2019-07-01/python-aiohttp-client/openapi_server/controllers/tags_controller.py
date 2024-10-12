from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.tag_details import TagDetails
from openapi_server.models.tag_value import TagValue
from openapi_server.models.tags_list_result import TagsListResult
from openapi_server import util


async def tags_create_or_update(request: web.Request, tag_name, api_version, subscription_id) -> web.Response:
    """Creates a tag in the subscription.

    The tag name can have a maximum of 512 characters and is case insensitive. Tag names created by Azure have prefixes of microsoft, azure, or windows. You cannot create tags with one of these prefixes.

    :param tag_name: The name of the tag to create.
    :type tag_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tags_create_or_update_value(request: web.Request, tag_name, tag_value, api_version, subscription_id) -> web.Response:
    """tags_create_or_update_value

    Creates a tag value. The name of the tag must already exist.

    :param tag_name: The name of the tag.
    :type tag_name: str
    :param tag_value: The value of the tag to create.
    :type tag_value: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tags_delete(request: web.Request, tag_name, api_version, subscription_id) -> web.Response:
    """Deletes a tag from the subscription.

    You must remove all values from a resource tag before you can delete it.

    :param tag_name: The name of the tag.
    :type tag_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tags_delete_value(request: web.Request, tag_name, tag_value, api_version, subscription_id) -> web.Response:
    """tags_delete_value

    Deletes a tag value.

    :param tag_name: The name of the tag.
    :type tag_name: str
    :param tag_value: The value of the tag to delete.
    :type tag_value: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tags_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """tags_list

    Gets the names and values of all resource tags that are defined in a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)
