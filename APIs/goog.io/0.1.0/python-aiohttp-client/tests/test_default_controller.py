# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.crawl200_response import Crawl200Response
from openapi_server.models.get_the_status_of_the_api_service200_response import GetTheStatusOfTheAPIService200Response
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.images200_response import Images200Response
from openapi_server.models.news200_response import News200Response
from openapi_server.models.search200_response import Search200Response
from openapi_server.models.serp200_response import Serp200Response
from openapi_server.models.serp_data import SerpData


pytestmark = pytest.mark.asyncio

async def test_crawl(client):
    """Test case for crawl

    Crawl
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/crawl/{query}'.format(query='q=google+search+api'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_the_status_of_the_api_service(client):
    """Test case for get_the_status_of_the_api_service

    Status
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images(client):
    """Test case for images

    Images
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/images/{query}'.format(query='query_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_news(client):
    """Test case for news

    News
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/news/{query}'.format(query='query_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Search
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/search/{query}'.format(query='q=google+search+api'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_serp(client):
    """Test case for serp

    SERP
    """
    body = {"website":"website","query":"query"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/serp/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

