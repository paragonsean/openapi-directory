# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.currencies_response import CurrenciesResponse
from openapi_server.models.currency_response import CurrencyResponse


pytestmark = pytest.mark.asyncio

async def test_currencies_get(client):
    """Test case for currencies_get

    List of currencies
    """
    params = [('page[number]', 56),
                    ('page[size]', 56),
                    ('filter[search]', 'filter_search_example'),
                    ('filter[code_iso_alpha3]', 'filter_code_iso_alpha3_example'),
                    ('filter[code_iso_numeric3]', 56),
                    ('filter[code_estandards_alpha]', 'filter_code_estandards_alpha_example'),
                    ('filter[currency_type]', ['filter_currency_type_example']),
                    ('filter[category]', ['filter_category_example']),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/currencies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currencies_id_get(client):
    """Test case for currencies_id_get

    Currency by ID
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/currencies/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

