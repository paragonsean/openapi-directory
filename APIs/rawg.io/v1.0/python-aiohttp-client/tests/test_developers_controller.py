# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.developer_single import DeveloperSingle
from openapi_server.models.developers_list200_response import DevelopersList200Response


pytestmark = pytest.mark.asyncio

async def test_developers_list(client):
    """Test case for developers_list

    Get a list of game developers.
    """
    params = [('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/developers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_developers_read(client):
    """Test case for developers_read

    Get details of the developer.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/developers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

