# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

async def test_delete_swagger(client):
    """Test case for delete_swagger

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/swagger/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_update_swagger(client):
    """Test case for update_swagger

    
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = FormData()
    data.add_field('swagger', '/path/to/file')
    response = await client.request(
        method='PUT',
        path='/api/v1/swagger/{id}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_swagger(client):
    """Test case for upload_swagger

    
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = FormData()
    data.add_field('swagger', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v1/swagger',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

