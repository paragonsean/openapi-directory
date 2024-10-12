from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_tag_definition import ResourceTagDefinition
from openapi_server.models.resource_tag_delete_response import ResourceTagDeleteResponse
from openapi_server.models.resource_tag_detail import ResourceTagDetail
from openapi_server.models.resource_tag_get_response import ResourceTagGetResponse
from openapi_server.models.resource_tag_update import ResourceTagUpdate
from openapi_server import util


async def create_user_defined_tag(request: web.Request, body) -> web.Response:
    """Create a user-defined resource tag for tagging cloud compute resources

    Create a user-defined resource tag for tagging cloud compute resources created by CloudOn and CloutOut. 

    :param body: The definition of a new user-defined resource tag to be created. 
    :type body: dict | bytes

    """
    body = ResourceTagDefinition.from_dict(body)
    return web.Response(status=200)


async def delete_user_defined_tag(request: web.Request, id) -> web.Response:
    """Delete a user-defined resource tag

    Delete a user-defined resource tag.

    :param id: ID of the user-defined resource tag.
    :type id: str

    """
    return web.Response(status=200)


async def delete_user_defined_tag_bulk(request: web.Request, ids) -> web.Response:
    """Delete a list of user-defined resource tags

    Delete a list of user-defined resource tags in one delete operation. 

    :param ids: An array of IDs of the user-defined resource tags to be deleted. Any non-existent ID in the array will be ignored. 
    :type ids: List[str]

    """
    return web.Response(status=200)


async def get_user_defined_tag(request: web.Request, id) -> web.Response:
    """Get user-defined tag

    Retrieve details of a user-defined resource tag.

    :param id: ID of the user-defined resource tag.
    :type id: str

    """
    return web.Response(status=200)


async def query_user_defined_tag(request: web.Request, key=None, scope_ref_id=None) -> web.Response:
    """Get user-defined resource tags

    Get user-defined resource tags for the cloud compute resources created by CloudOn and CloudOut. 

    :param key: Filter results by resource tag.
    :type key: str
    :param scope_ref_id: Filter results by archival location id.
    :type scope_ref_id: str

    """
    return web.Response(status=200)


async def update_user_defined_tag(request: web.Request, id, body) -> web.Response:
    """Update the value of a user-defined resource tag

    Update the value of a user-defined resource tag. 

    :param id: ID of the user-defined resource tag.
    :type id: str
    :param body: Properties to update.
    :type body: dict | bytes

    """
    body = ResourceTagUpdate.from_dict(body)
    return web.Response(status=200)
