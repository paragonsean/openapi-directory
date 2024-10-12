# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.style_entity import StyleEntity


pytestmark = pytest.mark.asyncio

async def test_delete_styles_path(client):
    """Test case for delete_styles_path

    Delete Style
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/styles/{path}'.format(path='path_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_styles_path(client):
    """Test case for get_styles_path

    Show Style
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/styles/{path}'.format(path='path_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_styles_path(client):
    """Test case for patch_styles_path

    Update Style
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/styles/{path}'.format(path='path_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

