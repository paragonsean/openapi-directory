# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_provider_info import ServiceProviderInfo
from openapi_server.models.tnr_msg import TnrMsg


pytestmark = pytest.mark.asyncio

async def test_capabilities(client):
    """Test case for capabilities

    capabilities
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/eu-bon/utis/1.0/capabilities',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    search
    """
    params = [('query', 'query_example'),
                    ('providers', 'pesi,eunis,bgbm-cdm-server[col]'),
                    ('searchMode', scientificNameExact),
                    ('addSynonymy', False),
                    ('timeout', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/eu-bon/utis/1.0/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

