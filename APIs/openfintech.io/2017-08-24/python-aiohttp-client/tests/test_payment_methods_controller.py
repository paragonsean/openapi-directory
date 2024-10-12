# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_method_response import PaymentMethodResponse
from openapi_server.models.payment_methods_response import PaymentMethodsResponse


pytestmark = pytest.mark.asyncio

async def test_payment_methods_get(client):
    """Test case for payment_methods_get

    List of payment methods
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
        path='/v1/payment-methods',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_methods_id_get(client):
    """Test case for payment_methods_id_get

    Payment method by ID
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/payment-methods/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

