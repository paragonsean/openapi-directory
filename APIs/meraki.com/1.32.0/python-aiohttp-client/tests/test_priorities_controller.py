# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_branding_policies_priorities200_response import GetOrganizationBrandingPoliciesPriorities200Response
from openapi_server.models.update_organization_branding_policies_priorities_request import UpdateOrganizationBrandingPoliciesPrioritiesRequest


pytestmark = pytest.mark.asyncio

async def test_get_organization_branding_policies_priorities_2(client):
    """Test case for get_organization_branding_policies_priorities_2

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

async def test_update_organization_branding_policies_priorities_2(client):
    """Test case for update_organization_branding_policies_priorities_2

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

