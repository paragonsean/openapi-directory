# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deposit_method_response import DepositMethodResponse
from openapi_server.models.deposit_methods_response import DepositMethodsResponse


pytestmark = pytest.mark.asyncio

async def test_deposit_methods_get(client):
    """Test case for deposit_methods_get

    List of deposit methods
    """
    params = [('page[number]', 56),
                    ('page[size]', 56),
                    ('filter[search]', 'filter_search_example'),
                    ('filter[name]', 'filter_name_example'),
                    ('filter[code]', 'filter_code_example'),
                    ('filter[processor_name]', 'filter_processor_name_example'),
                    ('filter[category]', ['filter_category_example']),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/deposit-methods',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deposit_methods_id_get(client):
    """Test case for deposit_methods_id_get

    Deposit method by ID
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/deposit-methods/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

