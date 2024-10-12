# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_stored_payment_methods_response import ListStoredPaymentMethodsResponse


pytestmark = pytest.mark.asyncio

async def test_delete_stored_payment_methods_stored_payment_method_id(client):
    """Test case for delete_stored_payment_methods_stored_payment_method_id

    Delete a token for stored payment details
    """
    params = [('shopperReference', 'shopper_reference_example'),
                    ('merchantAccount', 'merchant_account_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v70/storedPaymentMethods/{stored_payment_method_id}'.format(stored_payment_method_id='stored_payment_method_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stored_payment_methods(client):
    """Test case for get_stored_payment_methods

    Get tokens for stored payment details
    """
    params = [('shopperReference', 'shopper_reference_example'),
                    ('merchantAccount', 'merchant_account_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v70/storedPaymentMethods',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

