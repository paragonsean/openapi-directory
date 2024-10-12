# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_firmware_upgrades_staged_group_request import CreateNetworkFirmwareUpgradesStagedGroupRequest
from openapi_server.models.create_organization_adaptive_policy_group_request import CreateOrganizationAdaptivePolicyGroupRequest
from openapi_server.models.create_organization_policy_objects_group_request import CreateOrganizationPolicyObjectsGroupRequest
from openapi_server.models.get_network_firmware_upgrades_staged_groups200_response_inner import GetNetworkFirmwareUpgradesStagedGroups200ResponseInner
from openapi_server.models.update_organization_adaptive_policy_group_request import UpdateOrganizationAdaptivePolicyGroupRequest
from openapi_server.models.update_organization_policy_objects_group_request import UpdateOrganizationPolicyObjectsGroupRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_firmware_upgrades_staged_group_3(client):
    """Test case for create_network_firmware_upgrades_staged_group_3

    Create a Staged Upgrade Group for a network
    """
    body = openapi_server.CreateNetworkFirmwareUpgradesStagedGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_adaptive_policy_group_2(client):
    """Test case for create_organization_adaptive_policy_group_2

    Creates a new adaptive policy group
    """
    body = openapi_server.CreateOrganizationAdaptivePolicyGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/groups'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_policy_objects_group_2(client):
    """Test case for create_organization_policy_objects_group_2

    Creates a new Policy Object Group.
    """
    body = openapi_server.CreateOrganizationPolicyObjectsGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/policyObjects/groups'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_firmware_upgrades_staged_group_3(client):
    """Test case for delete_network_firmware_upgrades_staged_group_3

    Delete a Staged Upgrade Group
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}'.format(network_id='network_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_adaptive_policy_group_2(client):
    """Test case for delete_organization_adaptive_policy_group_2

    Deletes the specified adaptive policy group and any associated policies and references
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/groups/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_policy_objects_group_2(client):
    """Test case for delete_organization_policy_objects_group_2

    Deletes a Policy Object Group.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}'.format(organization_id='organization_id_example', policy_object_group_id='policy_object_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_firmware_upgrades_staged_group_3(client):
    """Test case for get_network_firmware_upgrades_staged_group_3

    Get a Staged Upgrade Group from a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}'.format(network_id='network_id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_firmware_upgrades_staged_groups_3(client):
    """Test case for get_network_firmware_upgrades_staged_groups_3

    List of Staged Upgrade Groups in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_group_2(client):
    """Test case for get_organization_adaptive_policy_group_2

    Returns an adaptive policy group
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/groups/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_groups_2(client):
    """Test case for get_organization_adaptive_policy_groups_2

    List adaptive policy groups in a organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/groups'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_policy_objects_group_2(client):
    """Test case for get_organization_policy_objects_group_2

    Shows details of a Policy Object Group.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}'.format(organization_id='organization_id_example', policy_object_group_id='policy_object_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_policy_objects_groups_2(client):
    """Test case for get_organization_policy_objects_groups_2

    Lists Policy Object Groups belonging to the organization.
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/policyObjects/groups'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_firmware_upgrades_staged_group_3(client):
    """Test case for update_network_firmware_upgrades_staged_group_3

    Update a Staged Upgrade Group for a network
    """
    body = openapi_server.CreateNetworkFirmwareUpgradesStagedGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/staged/groups/{group_id}'.format(network_id='network_id_example', group_id='group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_adaptive_policy_group_2(client):
    """Test case for update_organization_adaptive_policy_group_2

    Updates an adaptive policy group
    """
    body = openapi_server.UpdateOrganizationAdaptivePolicyGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/groups/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_policy_objects_group_2(client):
    """Test case for update_organization_policy_objects_group_2

    Updates a Policy Object Group.
    """
    body = openapi_server.UpdateOrganizationPolicyObjectsGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/policyObjects/groups/{policy_object_group_id}'.format(organization_id='organization_id_example', policy_object_group_id='policy_object_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

