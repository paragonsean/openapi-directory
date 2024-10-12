# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_convert(client):
    """Test case for convert

    Convert a Swagger 2.0 definition passed in the body to OpenAPI 3.0.x 
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('filename', 'filename_example')
    data.add_field('source', 'source_example')
    data.add_field('validate', 'validate_example')
    response = await client.request(
        method='POST',
        path='/api/v1/convert',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_url(client):
    """Test case for convert_url

    Convert a Swagger 2.0 definition to OpenAPI 3.0.x from a URL
    """
    params = [('url', 'https://raw.githubusercontent.com/Mermade/openapi-webconverter/master/contract/swagger.json')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/convert',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

