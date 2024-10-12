# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entry_info_response import EntryInfoResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.info_response import InfoResponse


pytestmark = pytest.mark.asyncio

async def test_get_entry_info_info_entry_get(client):
    """Test case for get_entry_info_info_entry_get

    Get Entry Info
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/info/{entry}'.format(entry='entry_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_info_info_get(client):
    """Test case for get_info_info_get

    Get Info
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

