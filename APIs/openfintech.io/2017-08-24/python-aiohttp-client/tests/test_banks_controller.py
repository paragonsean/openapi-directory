# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bank_response import BankResponse
from openapi_server.models.banks_response import BanksResponse


pytestmark = pytest.mark.asyncio

async def test_banks_get(client):
    """Test case for banks_get

    List of banks
    """
    params = [('page[number]', 56),
                    ('page[size]', 56),
                    ('filter[sort_code]', 'filter_sort_code_example'),
                    ('filter[code]', 'filter_code_example'),
                    ('filter[status]', ['filter_status_example']),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/banks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_banks_id_get(client):
    """Test case for banks_id_get

    Bank by ID
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/banks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

