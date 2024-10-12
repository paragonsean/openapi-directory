# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.browser_json_response import BrowserJsonResponse
from openapi_server.models.info_response import InfoResponse
from openapi_server.models.search_data import SearchData


pytestmark = pytest.mark.asyncio

async def test_api_delete_pic_post(client):
    """Test case for api_delete_pic_post

    Remove an image from a search request
    """
    params = [('id_search', 'id_search_example'),
                    ('id_pic', 'id_pic_example')]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/delete_pic',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_info_post(client):
    """Test case for api_info_post

    Returns remaining search credits, search engine online status, and number of indexed faces
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_search_post(client):
    """Test case for api_search_post

    
    """
    body = {"with_progress":True,"status_only":False,"demo":False,"id_search":"3vdi8t-s_8DAAA7D5E784616","id_captcha":"id_captcha"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_upload_pic_post(client):
    """Test case for api_upload_pic_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Bearer': 'special-key',
    }
    data = FormData()
    data.add_field('id_search', 'id_search_example')
    data.add_field('images', ['/path/to/file'])
    response = await client.request(
        method='POST',
        path='/api/upload_pic',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

