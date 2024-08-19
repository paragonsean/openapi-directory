# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_estimated_price200_response import GetEstimatedPrice200Response
from openapi_server.models.get_list_of_payments200_response import GetListOfPayments200Response
from openapi_server.models.get_payment_status200_response import GetPaymentStatus200Response
from openapi_server.models.get_the_minimum_payment_amount200_response import GetTheMinimumPaymentAmount200Response
from openapi_server.models.get_update_payment_estimate200_response import GetUpdatePaymentEstimate200Response


pytestmark = pytest.mark.asyncio

async def test_get_estimated_price(client):
    """Test case for get_estimated_price

    Get estimated price
    """
    params = [('amount', '3999.5000'),
                    ('currency_from', 'usd'),
                    ('currency_to', 'btc')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': '{{your_api_key}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/estimate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_of_payments(client):
    """Test case for get_list_of_payments

    Get list of payments
    """
    params = [('limit', '10'),
                    ('page', '0'),
                    ('sortBy', 'created_at'),
                    ('orderBy', 'asc'),
                    ('dateFrom', '2020-01-01'),
                    ('dateTo', '2021-01-01')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': '{{your_api_key}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/payment/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_status(client):
    """Test case for get_payment_status

    Get payment status
    """
    headers = { 
        'Accept': 'application/json',
        'x_api_key': '{{your_api_key}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/payment/{payment_id}'.format(payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_the_minimum_payment_amount(client):
    """Test case for get_the_minimum_payment_amount

    Get the minimum payment amount
    """
    params = [('currency_from', 'eth'),
                    ('currency_to', 'trx')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': '{{your_api_key}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/min-amount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_update_payment_estimate(client):
    """Test case for get_update_payment_estimate

    Get/Update payment estimate
    """
    headers = { 
        'Accept': 'application/json',
        'x_api_key': '{{your_api_key}}',
    }
    response = await client.request(
        method='POST',
        path='/v1/payment/{id}/update-merchant-estimate'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

