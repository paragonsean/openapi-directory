# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_errors import AccountErrors


pytestmark = pytest.mark.asyncio

async def test_set_pin_3(client):
    """Test case for set_pin_3

    Sets a customer's plus card pin
    """
    pin = 3.4
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts/account/plusCard/pin',
        headers=headers,
        json=pin,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_pin_3(client):
    """Test case for update_pin_3

    Updates a customer's plus card pin
    """
    pin = 3.4
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='PUT',
        path='/v2/accounts/account/plusCard/pin',
        headers=headers,
        json=pin,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

