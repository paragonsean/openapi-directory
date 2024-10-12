from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.tag_details import TagDetails
from openapi_server.models.tag_value import TagValue
from openapi_server.models.tags_list_result import TagsListResult
from openapi_server.models.tags_patch_resource import TagsPatchResource
from openapi_server.models.tags_resource import TagsResource
from openapi_server import util


async def tags_create_or_update(request: web.Request, tag_name, api_version, subscription_id) -> web.Response:
    """Creates a predefined tag name.

    This operation allows adding a name to the list of predefined tag names for the given subscription. A tag name can have a maximum of 512 characters and is case-insensitive. Tag names cannot have the following prefixes which are reserved for Azure use: &#39;microsoft&#39;, &#39;azure&#39;, &#39;windows&#39;.

    :param tag_name: The name of the tag to create.
    :type tag_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tags_create_or_update_at_scope(request: web.Request, scope, api_version, parameters) -> web.Response:
    """Creates or updates the entire set of tags on a resource or subscription.

    This operation allows adding or replacing the entire set of tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags.

    :param scope: The resource scope.
    :type scope: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: 
    :type parameters: dict | bytes

    """
    parameters = TagsResource.from_dict(parameters)
    return web.Response(status=200)


async def tags_create_or_update_value(request: web.Request, tag_name, tag_value, api_version, subscription_id) -> web.Response:
    """Creates a predefined value for a predefined tag name.

    This operation allows adding a value to the list of predefined values for an existing predefined tag name. A tag value can have a maximum of 256 characters.

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
    """Deletes a predefined tag name.

    This operation allows deleting a name from the list of predefined tag names for the given subscription. The name being deleted must not be in use as a tag name for any resource. All predefined values for the given name must have already been deleted.

    :param tag_name: The name of the tag.
    :type tag_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tags_delete_at_scope(request: web.Request, scope, api_version) -> web.Response:
    """Deletes the entire set of tags on a resource or subscription.

    

    :param scope: The resource scope.
    :type scope: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def tags_delete_value(request: web.Request, tag_name, tag_value, api_version, subscription_id) -> web.Response:
    """Deletes a predefined tag value for a predefined tag name.

    This operation allows deleting a value from the list of predefined values for an existing predefined tag name. The value being deleted must not be in use as a tag value for the given tag name for any resource.

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


async def tags_get_at_scope(request: web.Request, scope, api_version) -> web.Response:
    """Gets the entire set of tags on a resource or subscription.

    

    :param scope: The resource scope.
    :type scope: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def tags_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """Gets a summary of tag usage under the subscription.

    This operation performs a union of predefined tags, resource tags, resource group tags and subscription tags, and returns a summary of usage for each tag name and value under the given subscription. In case of a large number of tags, this operation may return a previously cached result.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tags_update_at_scope(request: web.Request, scope, api_version, parameters) -> web.Response:
    """Selectively updates the set of tags on a resource or subscription.

    This operation allows replacing, merging or selectively deleting tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags at the end of the operation. The &#39;replace&#39; option replaces the entire set of existing tags with a new set. The &#39;merge&#39; option allows adding tags with new names and updating the values of tags with existing names. The &#39;delete&#39; option allows selectively deleting tags based on given names or name/value pairs.

    :param scope: The resource scope.
    :type scope: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: 
    :type parameters: dict | bytes

    """
    parameters = TagsPatchResource.from_dict(parameters)
    return web.Response(status=200)
