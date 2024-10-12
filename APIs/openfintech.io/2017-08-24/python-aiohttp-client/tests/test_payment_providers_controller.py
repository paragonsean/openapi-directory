# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_provider_response import PaymentProviderResponse
from openapi_server.models.payment_providers_response import PaymentProvidersResponse


pytestmark = pytest.mark.asyncio

async def test_payment_providers_get(client):
    """Test case for payment_providers_get

    List of payment providers
    """
    params = [('page[number]', 56),
                    ('page[size]', 56),
                    ('filter[search]', 'filter_search_example'),
                    ('filter[name]', 'filter_name_example'),
                    ('filter[code]', 'filter_code_example'),
                    ('filter[types]', ['filter_types_example']),
                    ('filter[sales_channels]', ['filter_sales_channels_example']),
                    ('filter[features]', ['filter_features_example']),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/payment-providers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_providers_id_get(client):
    """Test case for payment_providers_id_get

    Payment provider by ID
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/payment-providers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

