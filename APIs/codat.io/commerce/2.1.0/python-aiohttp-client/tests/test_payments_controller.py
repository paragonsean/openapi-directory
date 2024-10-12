# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_methods import PaymentMethods
from openapi_server.models.payments import Payments


pytestmark = pytest.mark.asyncio

async def test_list_payment_methods(client):
    """Test case for list_payment_methods

    List payment methods
    """
    params = [('page', 1),
                    ('pageSize', 100),
                    ('query', 'query_example'),
                    ('orderBy', '-modifiedDate')]
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/connections/{connection_id}/data/commerce-paymentMethods',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_payments(client):
    """Test case for list_payments

    List payments
    """
    params = [('page', 1),
                    ('pageSize', 100),
                    ('query', 'query_example'),
                    ('orderBy', '-modifiedDate')]
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/connections/{connection_id}/data/commerce-payments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

