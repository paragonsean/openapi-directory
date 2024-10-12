# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_adaptive_policy_acl_request import CreateOrganizationAdaptivePolicyAclRequest
from openapi_server.models.update_organization_adaptive_policy_acl_request import UpdateOrganizationAdaptivePolicyAclRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_adaptive_policy_acl_2(client):
    """Test case for create_organization_adaptive_policy_acl_2

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

async def test_delete_organization_adaptive_policy_acl_2(client):
    """Test case for delete_organization_adaptive_policy_acl_2

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

async def test_get_organization_adaptive_policy_acl_2(client):
    """Test case for get_organization_adaptive_policy_acl_2

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

async def test_get_organization_adaptive_policy_acls_2(client):
    """Test case for get_organization_adaptive_policy_acls_2

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

async def test_update_organization_adaptive_policy_acl_2(client):
    """Test case for update_organization_adaptive_policy_acl_2

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

