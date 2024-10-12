# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erskine_may_part import ErskineMayPart


pytestmark = pytest.mark.asyncio

async def test_api_part_get(client):
    """Test case for api_part_get

    Returns a list of all parts.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Part',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_part_part_number_get(client):
    """Test case for api_part_part_number_get

    Returns a part by part number.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Part/{part_number}'.format(part_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

