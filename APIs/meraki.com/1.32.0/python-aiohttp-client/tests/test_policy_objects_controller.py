# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_policy_object_request import CreateOrganizationPolicyObjectRequest
from openapi_server.models.create_organization_policy_objects_group_request import CreateOrganizationPolicyObjectsGroupRequest
from openapi_server.models.update_organization_policy_object_request import UpdateOrganizationPolicyObjectRequest
from openapi_server.models.update_organization_policy_objects_group_request import UpdateOrganizationPolicyObjectsGroupRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_policy_object_1(client):
    """Test case for create_organization_policy_object_1

    Creates a new Policy Object.
    """
    body = openapi_server.CreateOrganizationPolicyObjectRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/policyObjects'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_policy_objects_group_1(client):
    """Test case for create_organization_policy_objects_group_1

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

async def test_delete_organization_policy_object_1(client):
    """Test case for delete_organization_policy_object_1

    Deletes a Policy Object.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/policyObjects/{policy_object_id}'.format(organization_id='organization_id_example', policy_object_id='policy_object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_policy_objects_group_1(client):
    """Test case for delete_organization_policy_objects_group_1

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

async def test_get_organization_policy_object_1(client):
    """Test case for get_organization_policy_object_1

    Shows details of a Policy Object.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/policyObjects/{policy_object_id}'.format(organization_id='organization_id_example', policy_object_id='policy_object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_policy_objects_1(client):
    """Test case for get_organization_policy_objects_1

    Lists Policy Objects belonging to the organization.
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
        path='/api/v1/organizations/{organization_id}/policyObjects'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_policy_objects_group_1(client):
    """Test case for get_organization_policy_objects_group_1

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

async def test_get_organization_policy_objects_groups_1(client):
    """Test case for get_organization_policy_objects_groups_1

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

async def test_update_organization_policy_object_1(client):
    """Test case for update_organization_policy_object_1

    Updates a Policy Object.
    """
    body = openapi_server.UpdateOrganizationPolicyObjectRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/policyObjects/{policy_object_id}'.format(organization_id='organization_id_example', policy_object_id='policy_object_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_policy_objects_group_1(client):
    """Test case for update_organization_policy_objects_group_1

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

