# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exchanger_response import ExchangerResponse
from openapi_server.models.exchangers_response import ExchangersResponse


pytestmark = pytest.mark.asyncio

async def test_exchangers_get(client):
    """Test case for exchangers_get

    List of exchangers
    """
    params = [('page[number]', 56),
                    ('page[size]', 56),
                    ('filter[name]', 'filter_name_example'),
                    ('filter[status]', ['filter_status_example']),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/exchangers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_exchangers_id_get(client):
    """Test case for exchangers_id_get

    Exchanger by ID
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/exchangers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

