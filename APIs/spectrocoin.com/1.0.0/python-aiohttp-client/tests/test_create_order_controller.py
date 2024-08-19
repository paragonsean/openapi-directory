# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.order_information_class import OrderInformationClass


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_order(client):
    """Test case for create_order

    Create merchant order
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_id': 56,
        'callback_url': 'callback_url_example',
        'culture': 'culture_example',
        'description': 'description_example',
        'failure_url': 'failure_url_example',
        'merchant_id': 56,
        'order_id': 'order_id_example',
        'pay_amount': 3.4,
        'pay_currency': 'pay_currency_example',
        'payer_email': 'payer_email_example',
        'payer_name': 'payer_name_example',
        'payer_surname': 'payer_surname_example',
        'receive_amount': 3.4,
        'receive_currency': 'receive_currency_example',
        'sign': 'sign_example',
        'success_url': 'success_url_example'
        }
    response = await client.request(
        method='POST',
        path='/api/merchant/1/api/createOrder',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

