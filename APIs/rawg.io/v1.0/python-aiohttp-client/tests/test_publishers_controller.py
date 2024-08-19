# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.publisher_single import PublisherSingle
from openapi_server.models.publishers_list200_response import PublishersList200Response


pytestmark = pytest.mark.asyncio

async def test_publishers_list(client):
    """Test case for publishers_list

    Get a list of video game publishers.
    """
    params = [('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/publishers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publishers_read(client):
    """Test case for publishers_read

    Get details of the publisher.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/publishers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

