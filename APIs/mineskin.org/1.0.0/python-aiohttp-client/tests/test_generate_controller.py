# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_upload_post200_response import GenerateUploadPost200Response
from openapi_server.models.generate_upload_post400_response import GenerateUploadPost400Response
from openapi_server.models.generate_upload_post429_response import GenerateUploadPost429Response
from openapi_server.models.generate_url_post_request import GenerateUrlPostRequest
from openapi_server.models.generate_user_post_request import GenerateUserPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_generate_upload_post(client):
    """Test case for generate_upload_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'user_agent': 'ExampleApp/v1.0',
        'apiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'model': steve,
        'name': 'name_example',
        'variant': 'variant_example',
        'visibility': 0,
        'file': '/path/to/file'
        }
    response = await client.request(
        method='POST',
        path='/generate/upload',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_url_post(client):
    """Test case for generate_url_post

    
    """
    body = openapi_server.GenerateUrlPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'user_agent': 'ExampleApp/v1.0',
        'apiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/generate/url',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_user_post(client):
    """Test case for generate_user_post

    
    """
    body = openapi_server.GenerateUserPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'user_agent': 'ExampleApp/v1.0',
        'apiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/generate/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

