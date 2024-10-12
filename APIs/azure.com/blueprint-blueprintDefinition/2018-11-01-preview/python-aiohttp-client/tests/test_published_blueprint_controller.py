# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.published_blueprint import PublishedBlueprint
from openapi_server.models.published_blueprint_list import PublishedBlueprintList


pytestmark = pytest.mark.asyncio

async def test_published_blueprints_create(client):
    """Test case for published_blueprints_create

    
    """
    published_blueprint = {"properties":{"changeNotes":"changeNotes","blueprintName":"blueprintName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}/versions/{version_id}'.format(scope='scope_example', blueprint_name='blueprint_name_example', version_id='version_id_example'),
        headers=headers,
        json=published_blueprint,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_published_blueprints_delete(client):
    """Test case for published_blueprints_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}/versions/{version_id}'.format(scope='scope_example', blueprint_name='blueprint_name_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_published_blueprints_get(client):
    """Test case for published_blueprints_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}/versions/{version_id}'.format(scope='scope_example', blueprint_name='blueprint_name_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_published_blueprints_list(client):
    """Test case for published_blueprints_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}/versions'.format(scope='scope_example', blueprint_name='blueprint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

