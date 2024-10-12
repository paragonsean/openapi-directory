# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.crawl_url_read import CrawlUrlRead


pytestmark = pytest.mark.asyncio

async def test_get_crawl_url_collection(client):
    """Test case for get_crawl_url_collection

    Retrieves the collection of CrawlUrl resources.
    """
    params = [('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crawl-urls',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_crawl_url_item(client):
    """Test case for get_crawl_url_item

    Retrieves a CrawlUrl resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crawl-urls/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

