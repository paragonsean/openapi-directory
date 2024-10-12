# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.configuration_response_version import ConfigurationResponseVersion


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_configurations(client):
    """Test case for add_configurations

    Create user configurations
    """
    configurations = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/configurations.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=configurations,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_configurations(client):
    """Test case for delete_configurations

    Remove user configurations
    """
    configuration_ids = ['configuration_ids_example']
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/configurations.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=configuration_ids,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_configurations(client):
    """Test case for get_configurations

    Retrieve user configurations
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/configurations.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_configurations(client):
    """Test case for update_configurations

    Update user configurations
    """
    configurations = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/configurations.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=configurations,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

