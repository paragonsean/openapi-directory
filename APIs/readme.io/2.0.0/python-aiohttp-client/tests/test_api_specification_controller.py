# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

async def test_delete_api_specification(client):
    """Test case for delete_api_specification

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/api-specification/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_specification(client):
    """Test case for get_api_specification

    
    """
    params = [('perPage', 10),
                    ('page', 1)]
    headers = { 
        'x_readme_version': 'v3.0',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/api-specification',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_update_api_specification(client):
    """Test case for update_api_specification

    
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = FormData()
    data.add_field('spec', '/path/to/file')
    response = await client.request(
        method='PUT',
        path='/api/v1/api-specification/{id}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_api_specification(client):
    """Test case for upload_api_specification

    
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'x_readme_version': 'v3.0',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = FormData()
    data.add_field('spec', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v1/api-specification',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

