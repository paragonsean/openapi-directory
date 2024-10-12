# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.meshery_pattern import MesheryPattern
from openapi_server.models.patterns_api_response import PatternsAPIResponse


pytestmark = pytest.mark.asyncio

async def test_id_delete_deploy_pattern(client):
    """Test case for id_delete_deploy_pattern

    Handle DELETE request for Pattern Deploy
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/pattern/deploy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_delete_meshery_pattern(client):
    """Test case for id_delete_meshery_pattern

    Handle Delete for a Meshery Pattern
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/pattern/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_meshery_pattern(client):
    """Test case for id_get_meshery_pattern

    Handle GET for a Meshery Pattern
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pattern/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_pattern_files(client):
    """Test case for id_get_pattern_files

    Handle GET request for patterns
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pattern',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_getoam_meshery_pattern(client):
    """Test case for id_getoam_meshery_pattern

    Handles the get requests for the OAM objects
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oam/{type}'.format(type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_id_post_deploy_pattern(client):
    """Test case for id_post_deploy_pattern

    Handle POST request for Pattern Deploy
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'token': 'special-key',
    }
    data = FormData()
    data.add_field('upload_yaml_yml_file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/pattern/deploy',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_post_pattern_file(client):
    """Test case for id_post_pattern_file

    Handle POST requests for patterns
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pattern',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_postoam_meshery_pattern(client):
    """Test case for id_postoam_meshery_pattern

    Handles registering OMA objects
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/oam/{type}'.format(type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

