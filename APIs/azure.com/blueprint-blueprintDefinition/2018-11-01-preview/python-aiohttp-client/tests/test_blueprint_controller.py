# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.blueprint import Blueprint
from openapi_server.models.blueprint_list import BlueprintList


pytestmark = pytest.mark.asyncio

async def test_blueprints_create_or_update(client):
    """Test case for blueprints_create_or_update

    
    """
    blueprint = {"properties":{"layout":"{}","versions":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}'.format(scope='scope_example', blueprint_name='blueprint_name_example'),
        headers=headers,
        json=blueprint,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blueprints_delete(client):
    """Test case for blueprints_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}'.format(scope='scope_example', blueprint_name='blueprint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blueprints_get(client):
    """Test case for blueprints_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}'.format(scope='scope_example', blueprint_name='blueprint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blueprints_list(client):
    """Test case for blueprints_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

