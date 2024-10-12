# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_key_info import APIKeyInfo
from openapi_server.models.zone_info import ZoneInfo
from openapi_server.models.zone_stats import ZoneStats


pytestmark = pytest.mark.asyncio

async def test_get_api_info_item(client):
    """Test case for get_api_info_item

    
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/info/api',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_statistics_collection(client):
    """Test case for get_statistics_collection

    Returns overall stagtistics
    """
    params = [('page', 'page_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/info/stat/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_statistics_item(client):
    """Test case for get_statistics_item

    Returns statistics for specific zone
    """
    params = [('page', 'page_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/info/stat/{zone}'.format(zone='zone_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_info_tld_get(client):
    """Test case for info_tld_get

    Returns overall Tld info
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/info/tld/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_info_tld_zone_get(client):
    """Test case for info_tld_zone_get

    Returns statistics for specific zone
    """
    params = [('page', 'page_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/info/tld/{zone}'.format(zone='zone_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

