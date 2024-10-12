# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_adaptive_policy_acl_request import CreateOrganizationAdaptivePolicyAclRequest
from openapi_server.models.create_organization_adaptive_policy_group_request import CreateOrganizationAdaptivePolicyGroupRequest
from openapi_server.models.create_organization_adaptive_policy_policy_request import CreateOrganizationAdaptivePolicyPolicyRequest
from openapi_server.models.get_organization_adaptive_policy_overview200_response import GetOrganizationAdaptivePolicyOverview200Response
from openapi_server.models.update_organization_adaptive_policy_acl_request import UpdateOrganizationAdaptivePolicyAclRequest
from openapi_server.models.update_organization_adaptive_policy_group_request import UpdateOrganizationAdaptivePolicyGroupRequest
from openapi_server.models.update_organization_adaptive_policy_policy_request import UpdateOrganizationAdaptivePolicyPolicyRequest
from openapi_server.models.update_organization_adaptive_policy_settings_request import UpdateOrganizationAdaptivePolicySettingsRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_adaptive_policy_acl_1(client):
    """Test case for create_organization_adaptive_policy_acl_1

    Creates new adaptive policy ACL
    """
    body = openapi_server.CreateOrganizationAdaptivePolicyAclRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/acls'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_adaptive_policy_group_1(client):
    """Test case for create_organization_adaptive_policy_group_1

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

async def test_create_organization_adaptive_policy_policy_1(client):
    """Test case for create_organization_adaptive_policy_policy_1

    Add an Adaptive Policy
    """
    body = openapi_server.CreateOrganizationAdaptivePolicyPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_adaptive_policy_acl_1(client):
    """Test case for delete_organization_adaptive_policy_acl_1

    Deletes the specified adaptive policy ACL
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}'.format(organization_id='organization_id_example', acl_id='acl_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_adaptive_policy_group_1(client):
    """Test case for delete_organization_adaptive_policy_group_1

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

async def test_delete_organization_adaptive_policy_policy_1(client):
    """Test case for delete_organization_adaptive_policy_policy_1

    Delete an Adaptive Policy
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_acl_1(client):
    """Test case for get_organization_adaptive_policy_acl_1

    Returns the adaptive policy ACL information
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}'.format(organization_id='organization_id_example', acl_id='acl_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_acls_1(client):
    """Test case for get_organization_adaptive_policy_acls_1

    List adaptive policy ACLs in a organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/acls'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_group_1(client):
    """Test case for get_organization_adaptive_policy_group_1

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

async def test_get_organization_adaptive_policy_groups_1(client):
    """Test case for get_organization_adaptive_policy_groups_1

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

async def test_get_organization_adaptive_policy_overview_1(client):
    """Test case for get_organization_adaptive_policy_overview_1

    Returns adaptive policy aggregate statistics for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/overview'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_policies_1(client):
    """Test case for get_organization_adaptive_policy_policies_1

    List adaptive policies in an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_policy_1(client):
    """Test case for get_organization_adaptive_policy_policy_1

    Return an adaptive policy
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_settings_1(client):
    """Test case for get_organization_adaptive_policy_settings_1

    Returns global adaptive policy settings in an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/settings'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_adaptive_policy_acl_1(client):
    """Test case for update_organization_adaptive_policy_acl_1

    Updates an adaptive policy ACL
    """
    body = openapi_server.UpdateOrganizationAdaptivePolicyAclRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/acls/{acl_id}'.format(organization_id='organization_id_example', acl_id='acl_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_adaptive_policy_group_1(client):
    """Test case for update_organization_adaptive_policy_group_1

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

async def test_update_organization_adaptive_policy_policy_1(client):
    """Test case for update_organization_adaptive_policy_policy_1

    Update an Adaptive Policy
    """
    body = openapi_server.UpdateOrganizationAdaptivePolicyPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_adaptive_policy_settings_1(client):
    """Test case for update_organization_adaptive_policy_settings_1

    Update global adaptive policy settings
    """
    body = openapi_server.UpdateOrganizationAdaptivePolicySettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/settings'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

