# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.filter import Filter


pytestmark = pytest.mark.asyncio

async def test_filters_filter_name_get(client):
    """Test case for filters_filter_name_get

    Get Single Filter by filterName
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/filters/{filter_name}'.format(filter_name='filter_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filters_get(client):
    """Test case for filters_get

    Shop Filters
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/filters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

