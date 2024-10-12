# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_early_access_features_opt_in_request import CreateOrganizationEarlyAccessFeaturesOptInRequest
from openapi_server.models.update_organization_early_access_features_opt_in_request import UpdateOrganizationEarlyAccessFeaturesOptInRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_early_access_features_opt_in_2(client):
    """Test case for create_organization_early_access_features_opt_in_2

    Create a new early access feature opt-in for an organization
    """
    body = openapi_server.CreateOrganizationEarlyAccessFeaturesOptInRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features/optIns'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_early_access_features_opt_in_2(client):
    """Test case for delete_organization_early_access_features_opt_in_2

    Delete an early access feature opt-in
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}'.format(organization_id='organization_id_example', opt_in_id='opt_in_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_early_access_features_2(client):
    """Test case for get_organization_early_access_features_2

    List the available early access features for organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_early_access_features_opt_in_2(client):
    """Test case for get_organization_early_access_features_opt_in_2

    Show an early access feature opt-in for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}'.format(organization_id='organization_id_example', opt_in_id='opt_in_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_early_access_features_opt_ins_2(client):
    """Test case for get_organization_early_access_features_opt_ins_2

    List the early access feature opt-ins for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features/optIns'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_early_access_features_opt_in_2(client):
    """Test case for update_organization_early_access_features_opt_in_2

    Update an early access feature opt-in for an organization
    """
    body = openapi_server.UpdateOrganizationEarlyAccessFeaturesOptInRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/earlyAccess/features/optIns/{opt_in_id}'.format(organization_id='organization_id_example', opt_in_id='opt_in_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

