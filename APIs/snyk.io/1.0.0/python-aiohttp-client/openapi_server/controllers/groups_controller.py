from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_a_member_to_an_organization_within_a_group_request import AddAMemberToAnOrganizationWithinAGroupRequest
from openapi_server.models.delete_tag_from_group200_response import DeleteTagFromGroup200Response
from openapi_server.models.delete_tag_from_group_request import DeleteTagFromGroupRequest
from openapi_server.models.list_all_tags_in_a_group200_response import ListAllTagsInAGroup200Response
from openapi_server.models.view_group_settings200_response import ViewGroupSettings200Response
from openapi_server import util


async def add_a_member_to_an_organization_within_a_group(request: web.Request, group_id, org_id, body=None) -> web.Response:
    """Add a member to an organization within a group

    

    :param group_id: The group ID. The &#x60;API_KEY&#x60; must have access admin to this group.
    :type group_id: str
    :param org_id: The organization ID we want to add the member to. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddAMemberToAnOrganizationWithinAGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_tag_from_group(request: web.Request, group_id, body=None) -> web.Response:
    """Delete tag from group

    

    :param group_id: The group ID. The &#x60;API_KEY&#x60; must have access admin to this group.
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteTagFromGroupRequest.from_dict(body)
    return web.Response(status=200)


async def list_all_members_in_a_group(request: web.Request, group_id) -> web.Response:
    """List all members in a group

    

    :param group_id: The group ID. The &#x60;API_KEY&#x60; must have access admin to this group.
    :type group_id: str

    """
    return web.Response(status=200)


async def list_all_organizations_in_a_group(request: web.Request, group_id, per_page=None, page=None, name=None) -> web.Response:
    """List all organizations in a group

    

    :param group_id: The group ID. The &#x60;API_KEY&#x60; must have READ access to this group and LIST organizations access in this group.
    :type group_id: str
    :param per_page: The number of results to return (maximum is 100).
    :type per_page: 
    :param page: For pagination - offset (from which to start returning results).
    :type page: 
    :param name: Only organizations that have a name that **starts with** this value (case insensitive) will be returned.
    :type name: str

    """
    return web.Response(status=200)


async def list_all_roles_in_a_group(request: web.Request, group_id) -> web.Response:
    """List all roles in a group

    

    :param group_id: The group ID. The &#x60;API_KEY&#x60; must have READ access to this group.
    :type group_id: str

    """
    return web.Response(status=200)


async def list_all_tags_in_a_group(request: web.Request, group_id, per_page=None, page=None) -> web.Response:
    """List all tags in a group

    

    :param group_id: The group ID. The &#x60;API_KEY&#x60; must have access admin to this group.
    :type group_id: str
    :param per_page: The number of results to return (the default is 1000).
    :type per_page: 
    :param page: The offset from which to start returning results from.
    :type page: 

    """
    return web.Response(status=200)


async def update_group_settings(request: web.Request, group_id) -> web.Response:
    """Update group settings

    

    :param group_id: Automatically added
    :type group_id: str

    """
    return web.Response(status=200)


async def view_group_settings(request: web.Request, group_id) -> web.Response:
    """View group settings

    

    :param group_id: The group ID. The &#x60;API_KEY&#x60; must have admin access to this group.
    :type group_id: str

    """
    return web.Response(status=200)
