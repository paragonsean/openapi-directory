# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.integration_configuration import IntegrationConfiguration
from openapi_server.models.integration_configurations import IntegrationConfigurations


pytestmark = pytest.mark.asyncio

async def test_create_integration(client):
    """Test case for create_integration

    Create an integration for the specified API and version
    """
    integration_type_configuration = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apis/{owner}/{api}/{version}/integrations'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        json=integration_type_configuration,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_integration(client):
    """Test case for delete_integration

    Delete an integration
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apis/{owner}/{api}/{version}/integrations/{integration_id}'.format(owner='owner_example', api='api_example', version='version_example', integration_id='integration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_execute_integration(client):
    """Test case for execute_integration

    Run an integration
    """
    params = [('commitMessage', 'commit_message_example')]
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apis/{owner}/{api}/{version}/integrations/{integration_id}/execute'.format(owner='owner_example', api='api_example', version='version_example', integration_id='integration_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_integration_by_id(client):
    """Test case for get_integration_by_id

    Get integration settings
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}/{version}/integrations/{integration_id}'.format(owner='owner_example', api='api_example', version='version_example', integration_id='integration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_integrations(client):
    """Test case for get_integrations

    Get all integrations configured for the specified API version
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}/{version}/integrations'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_integration(client):
    """Test case for patch_integration

    Partially update integration settings
    """
    integration_type_configuration = None
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/apis/{owner}/{api}/{version}/integrations/{integration_id}'.format(owner='owner_example', api='api_example', version='version_example', integration_id='integration_id_example'),
        headers=headers,
        json=integration_type_configuration,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_integration(client):
    """Test case for update_integration

    Update integration settings
    """
    integration_type_configuration = None
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apis/{owner}/{api}/{version}/integrations/{integration_id}'.format(owner='owner_example', api='api_example', version='version_example', integration_id='integration_id_example'),
        headers=headers,
        json=integration_type_configuration,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

