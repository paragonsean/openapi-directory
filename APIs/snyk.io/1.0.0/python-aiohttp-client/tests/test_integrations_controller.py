# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_new_integration_request import AddNewIntegrationRequest
from openapi_server.models.clone_an_integration_with_settings_and_credentials_request import CloneAnIntegrationWithSettingsAndCredentialsRequest
from openapi_server.models.get_existing_integration_by_type200_response import GetExistingIntegrationByType200Response
from openapi_server.models.retrieve200_response import Retrieve200Response
from openapi_server.models.update_existing_integration_request import UpdateExistingIntegrationRequest
from openapi_server.models.update_request import UpdateRequest


pytestmark = pytest.mark.asyncio

async def test_add_new_integration(client):
    """Test case for add_new_integration

    Add new integration
    """
    body = openapi_server.AddNewIntegrationRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/integrations'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clone_an_integration_with_settings_and_credentials(client):
    """Test case for clone_an_integration_with_settings_and_credentials

    Clone an integration (with settings and credentials)
    """
    body = openapi_server.CloneAnIntegrationWithSettingsAndCredentialsRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/integrations/{integration_id}/clone'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', integration_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_credentials(client):
    """Test case for delete_credentials

    Delete credentials
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/org/{org_id}/integrations/{integration_id}/authentication'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', integration_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_existing_integration_by_type(client):
    """Test case for get_existing_integration_by_type

    Get existing integration by type
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/integrations/{type}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', type='github'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list(client):
    """Test case for list

    List
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/integrations'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provision_new_broker_token(client):
    """Test case for provision_new_broker_token

    Provision new broker token
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/integrations/{integration_id}/authentication/provision-token'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', integration_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve(client):
    """Test case for retrieve

    Retrieve
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/integrations/{integration_id}/settings'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', integration_id='9a3e5d90-b782-468a-a042-9a2073736f0b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_switch_between_broker_tokens(client):
    """Test case for switch_between_broker_tokens

    Switch between broker tokens
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/integrations/{integration_id}/authentication/switch-token'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', integration_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update(client):
    """Test case for update

    Update
    """
    body = openapi_server.UpdateRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/org/{org_id}/integrations/{integration_id}/settings'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', integration_id='9a3e5d90-b782-468a-a042-9a2073736f0b'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_existing_integration(client):
    """Test case for update_existing_integration

    Update existing integration
    """
    body = openapi_server.UpdateExistingIntegrationRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/org/{org_id}/integrations/{integration_id}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', integration_id='9a3e5d90-b782-468a-a042-9a2073736f0b'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

