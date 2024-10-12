# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.get_config200_response import GetConfig200Response
from openapi_server.models.recognize_file200_response import RecognizeFile200Response
from openapi_server.models.recognize_file400_response import RecognizeFile400Response


pytestmark = pytest.mark.asyncio

async def test_get_config(client):
    """Test case for get_config

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recognize_bytes(client):
    """Test case for recognize_bytes

    
    """
    image_bytes = 'image_bytes_example'
    params = [('secret_key', 'secret_key_example'),
                    ('recognize_vehicle', 0),
                    ('country', 'country_example'),
                    ('return_image', 0),
                    ('topn', 10)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/recognize_bytes',
        headers=headers,
        json=image_bytes,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_recognize_file(client):
    """Test case for recognize_file

    
    """
    params = [('secret_key', 'secret_key_example'),
                    ('recognize_vehicle', 0),
                    ('country', 'country_example'),
                    ('return_image', 0),
                    ('topn', 10),
                    ('is_cropped', 0)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('image', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v3/recognize',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recognize_url(client):
    """Test case for recognize_url

    
    """
    params = [('image_url', 'image_url_example'),
                    ('secret_key', 'secret_key_example'),
                    ('recognize_vehicle', 0),
                    ('country', 'country_example'),
                    ('return_image', 0),
                    ('topn', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/recognize_url',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

