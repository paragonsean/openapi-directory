from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_firmware_upgrades_staged_group_request import CreateNetworkFirmwareUpgradesStagedGroupRequest
from openapi_server.models.create_organization_adaptive_policy_group_request import CreateOrganizationAdaptivePolicyGroupRequest
from openapi_server.models.create_organization_policy_objects_group_request import CreateOrganizationPolicyObjectsGroupRequest
from openapi_server.models.get_network_firmware_upgrades_staged_groups200_response_inner import GetNetworkFirmwareUpgradesStagedGroups200ResponseInner
from openapi_server.models.update_organization_adaptive_policy_group_request import UpdateOrganizationAdaptivePolicyGroupRequest
from openapi_server.models.update_organization_policy_objects_group_request import UpdateOrganizationPolicyObjectsGroupRequest
from openapi_server import util


async def create_network_firmware_upgrades_staged_group_3(request: web.Request, network_id, body) -> web.Response:
    """Create a Staged Upgrade Group for a network

    Create a Staged Upgrade Group for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFirmwareUpgradesStagedGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_adaptive_policy_group_2(request: web.Request, organization_id, body) -> web.Response:
    """Creates a new adaptive policy group

    Creates a new adaptive policy group

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAdaptivePolicyGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_policy_objects_group_2(request: web.Request, organization_id, body) -> web.Response:
    """Creates a new Policy Object Group.

    Creates a new Policy Object Group.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationPolicyObjectsGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_firmware_upgrades_staged_group_3(request: web.Request, network_id, group_id) -> web.Response:
    """Delete a Staged Upgrade Group

    Delete a Staged Upgrade Group

    :param network_id: 
    :type network_id: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def delete_organization_adaptive_policy_group_2(request: web.Request, organization_id, id) -> web.Response:
    """Deletes the specified adaptive policy group and any associated policies and references

    Deletes the specified adaptive policy group and any associated policies and references

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_organization_policy_objects_group_2(request: web.Request, organization_id, policy_object_group_id) -> web.Response:
    """Deletes a Policy Object Group.

    Deletes a Policy Object Group.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_group_id: 
    :type policy_object_group_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades_staged_group_3(request: web.Request, network_id, group_id) -> web.Response:
    """Get a Staged Upgrade Group from a network

    Get a Staged Upgrade Group from a network

    :param network_id: 
    :type network_id: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades_staged_groups_3(request: web.Request, network_id) -> web.Response:
    """List of Staged Upgrade Groups in a network

    List of Staged Upgrade Groups in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_group_2(request: web.Request, organization_id, id) -> web.Response:
    """Returns an adaptive policy group

    Returns an adaptive policy group

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_groups_2(request: web.Request, organization_id) -> web.Response:
    """List adaptive policy groups in a organization

    List adaptive policy groups in a organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_policy_objects_group_2(request: web.Request, organization_id, policy_object_group_id) -> web.Response:
    """Shows details of a Policy Object Group.

    Shows details of a Policy Object Group.

    :param organization_id: 
    :type organization_id: str
    :param policy_object_group_id: 
    :type policy_object_group_id: str

    """
    return web.Response(status=200)


async def get_organization_policy_objects_groups_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def update_network_firmware_upgrades_staged_group_3(request: web.Request, network_id, group_id, body) -> web.Response:
    """Update a Staged Upgrade Group for a network

    Update a Staged Upgrade Group for a network

    :param network_id: 
    :type network_id: str
    :param group_id: 
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFirmwareUpgradesStagedGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_adaptive_policy_group_2(request: web.Request, organization_id, id, body=None) -> web.Response:
    """Updates an adaptive policy group

    Updates an adaptive policy group. If updating \&quot;Infrastructure\&quot;, only the SGT is allowed. Cannot update \&quot;Unknown\&quot;.

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdaptivePolicyGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_policy_objects_group_2(request: web.Request, organization_id, policy_object_group_id, body=None) -> web.Response:
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
