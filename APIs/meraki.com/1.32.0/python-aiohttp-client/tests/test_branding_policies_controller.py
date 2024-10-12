# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_branding_policy201_response import CreateOrganizationBrandingPolicy201Response
from openapi_server.models.create_organization_branding_policy_request import CreateOrganizationBrandingPolicyRequest
from openapi_server.models.get_organization_branding_policies200_response_inner import GetOrganizationBrandingPolicies200ResponseInner
from openapi_server.models.get_organization_branding_policies_priorities200_response import GetOrganizationBrandingPoliciesPriorities200Response
from openapi_server.models.update_organization_branding_policies_priorities_request import UpdateOrganizationBrandingPoliciesPrioritiesRequest
from openapi_server.models.update_organization_branding_policy_request import UpdateOrganizationBrandingPolicyRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_branding_policy_1(client):
    """Test case for create_organization_branding_policy_1

    Add a new branding policy to an organization
    """
    body = openapi_server.CreateOrganizationBrandingPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/brandingPolicies'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_branding_policy_1(client):
    """Test case for delete_organization_branding_policy_1

    Delete a branding policy
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/brandingPolicies/{branding_policy_id}'.format(organization_id='organization_id_example', branding_policy_id='branding_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_branding_policies_1(client):
    """Test case for get_organization_branding_policies_1

    List the branding policies of an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/brandingPolicies'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_branding_policies_priorities_1(client):
    """Test case for get_organization_branding_policies_priorities_1

    Return the branding policy IDs of an organization in priority order
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/brandingPolicies/priorities'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_branding_policy_1(client):
    """Test case for get_organization_branding_policy_1

    Return a branding policy
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/brandingPolicies/{branding_policy_id}'.format(organization_id='organization_id_example', branding_policy_id='branding_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_branding_policies_priorities_1(client):
    """Test case for update_organization_branding_policies_priorities_1

    Update the priority ordering of an organization's branding policies.
    """
    body = openapi_server.UpdateOrganizationBrandingPoliciesPrioritiesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/brandingPolicies/priorities'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_branding_policy_1(client):
    """Test case for update_organization_branding_policy_1

    Update a branding policy
    """
    body = openapi_server.UpdateOrganizationBrandingPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/brandingPolicies/{branding_policy_id}'.format(organization_id='organization_id_example', branding_policy_id='branding_policy_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

