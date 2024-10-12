from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_policy_object_request import CreateOrganizationPolicyObjectRequest
from openapi_server.models.create_organization_policy_objects_group_request import CreateOrganizationPolicyObjectsGroupRequest
from openapi_server.models.update_organization_policy_object_request import UpdateOrganizationPolicyObjectRequest
from openapi_server.models.update_organization_policy_objects_group_request import UpdateOrganizationPolicyObjectsGroupRequest
from openapi_server import util


async def create_organization_policy_object_1(request: web.Request, organization_id, body) -> web.Response:
    """Creates a new Policy Object.

    Creates a new Policy Object.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationPolicyObjectRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_policy_objects_group_1(request: web.Request, organization_id, body) -> web.Response:
    """Creates a new Policy Object Group.

    Creates a new Policy Object Group.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationPolicyObjectsGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_policy_object_1(request: web.Request, organization_id, policy_object_id) -> web.Response:
    """Deletes a Policy Object.

    Deletes a Policy Object.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_id: 
    :type policy_object_id: str

    """
    return web.Response(status=200)


async def delete_organization_policy_objects_group_1(request: web.Request, organization_id, policy_object_group_id) -> web.Response:
    """Deletes a Policy Object Group.

    Deletes a Policy Object Group.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_group_id: 
    :type policy_object_group_id: str

    """
    return web.Response(status=200)


async def get_organization_policy_object_1(request: web.Request, organization_id, policy_object_id) -> web.Response:
    """Shows details of a Policy Object.

    Shows details of a Policy Object.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_id: 
    :type policy_object_id: str

    """
    return web.Response(status=200)


async def get_organization_policy_objects_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Lists Policy Objects belonging to the organization.

    Lists Policy Objects belonging to the organization.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 10 - 5000. Default is 5000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_policy_objects_group_1(request: web.Request, organization_id, policy_object_group_id) -> web.Response:
    """Shows details of a Policy Object Group.

    Shows details of a Policy Object Group.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_group_id: 
    :type policy_object_group_id: str

    """
    return web.Response(status=200)


async def get_organization_policy_objects_groups_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Lists Policy Object Groups belonging to the organization.

    Lists Policy Object Groups belonging to the organization.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def update_organization_policy_object_1(request: web.Request, organization_id, policy_object_id, body=None) -> web.Response:
    """Updates a Policy Object.

    Updates a Policy Object.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_id: 
    :type policy_object_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationPolicyObjectRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_policy_objects_group_1(request: web.Request, organization_id, policy_object_group_id, body=None) -> web.Response:
    """Updates a Policy Object Group.

    Updates a Policy Object Group.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_group_id: 
    :type policy_object_group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationPolicyObjectsGroupRequest.from_dict(body)
    return web.Response(status=200)
