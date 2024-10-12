# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credit_card import CreditCard
from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus


pytestmark = pytest.mark.asyncio

async def test_delete_credit_card(client):
    """Test case for delete_credit_card

    Delete credit card
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/payment/{card_id}/delete'.format(card_id=4242424242424242),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_credit_card(client):
    """Test case for get_credit_card

    View saved credit card
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payment/{card_id}'.format(card_id=4242424242424242),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_card_payment_code(client):
    """Test case for reset_card_payment_code

    Reset credit card payment code
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payment/{card_id}/reset-payment-code'.format(card_id=4242424242424242),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_corporate_payment_code(client):
    """Test case for reset_corporate_payment_code

    Reset payment code
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payment/reset-corporate-payment-code',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_toggle_corporate_auto_charge(client):
    """Test case for toggle_corporate_auto_charge

    Manage automatic charges on your credit card
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payment/toggle-corporate-auto-charge',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

