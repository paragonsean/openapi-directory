# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_pages_post_request import ApiPagesPostRequest
from openapi_server.models.page import Page


pytestmark = pytest.mark.asyncio

async def test_api_pages_get(client):
    """Test case for api_pages_get

    show details for all pages
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/pages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_pages_id_delete(client):
    """Test case for api_pages_id_delete

    remove a page
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/api/pages/{id}'.format(id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_pages_id_get(client):
    """Test case for api_pages_id_get

    show details for a page
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/pages/{id}'.format(id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_pages_id_put(client):
    """Test case for api_pages_id_put

    update details for a page
    """
    body = {"social_image":"{}","template":"contained","body_markdown":"body_markdown","is_top_level_path":True,"description":"description","title":"title","body_json":"body_json","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/api/pages/{id}'.format(id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_pages_post(client):
    """Test case for api_pages_post

    pages
    """
    body = openapi_server.ApiPagesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/api/pages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

