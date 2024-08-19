from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_group200_response import CreateGroup200Response
from openapi_server.models.create_group_category200_response import CreateGroupCategory200Response
from openapi_server.models.delete_group200_response import DeleteGroup200Response
from openapi_server.models.delete_group_category200_response import DeleteGroupCategory200Response
from openapi_server.models.get_group_category_details200_response import GetGroupCategoryDetails200Response
from openapi_server.models.get_group_tree200_response import GetGroupTree200Response
from openapi_server.models.group_category import GroupCategory
from openapi_server.models.group_category_update import GroupCategoryUpdate
from openapi_server.models.group_details200_response import GroupDetails200Response
from openapi_server.models.group_new import GroupNew
from openapi_server.models.group_update import GroupUpdate
from openapi_server.models.list_groups200_response import ListGroups200Response
from openapi_server.models.reload_group200_response import ReloadGroup200Response
from openapi_server.models.update_group200_response import UpdateGroup200Response
from openapi_server.models.update_group_category200_response import UpdateGroupCategory200Response
from openapi_server import util


async def create_group(request: web.Request, body=None) -> web.Response:
    """Create a group

    Create a new group based in provided parameters

    :param body: 
    :type body: dict | bytes

    """
    body = GroupNew.from_dict(body)
    return web.Response(status=200)


async def create_group_category(request: web.Request, body) -> web.Response:
    """Create a group category

    Create a new group category

    :param body: 
    :type body: dict | bytes

    """
    body = GroupCategory.from_dict(body)
    return web.Response(status=200)


async def delete_group(request: web.Request, group_id) -> web.Response:
    """Delete a group

    Update detailed information about a group

    :param group_id: Id of the group
    :type group_id: str
    :type group_id: str

    """
    return web.Response(status=200)


async def delete_group_category(request: web.Request, group_category_id) -> web.Response:
    """Delete group category

    Delete a group category. It must have no child groups and no children categories.

    :param group_category_id: 
    :type group_category_id: str
    :type group_category_id: str

    """
    return web.Response(status=200)


async def get_group_category_details(request: web.Request, group_category_id) -> web.Response:
    """Get group category details

    Get detailed information about a group category

    :param group_category_id: 
    :type group_category_id: str
    :type group_category_id: str

    """
    return web.Response(status=200)


async def get_group_tree(request: web.Request, ) -> web.Response:
    """Get groups tree

    Get all available groups and their categories in a tree


    """
    return web.Response(status=200)


async def group_details(request: web.Request, group_id) -> web.Response:
    """Get group details

    Get detailed information about a group

    :param group_id: Id of the group
    :type group_id: str
    :type group_id: str

    """
    return web.Response(status=200)


async def list_groups(request: web.Request, ) -> web.Response:
    """List all groups

    List all groups


    """
    return web.Response(status=200)


async def reload_group(request: web.Request, group_id) -> web.Response:
    """Reload a group

    Recompute the content of a group

    :param group_id: Id of the group
    :type group_id: str
    :type group_id: str

    """
    return web.Response(status=200)


async def update_group(request: web.Request, group_id, body) -> web.Response:
    """Update group details

    Update detailed information about a group

    :param group_id: Id of the group
    :type group_id: str
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GroupUpdate.from_dict(body)
    return web.Response(status=200)


async def update_group_category(request: web.Request, group_category_id, body) -> web.Response:
    """Update group category details

    Update detailed information about a group category

    :param group_category_id: 
    :type group_category_id: str
    :type group_category_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GroupCategoryUpdate.from_dict(body)
    return web.Response(status=200)
