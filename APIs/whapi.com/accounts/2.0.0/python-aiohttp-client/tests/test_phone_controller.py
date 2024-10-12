# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_errors import AccountErrors
from openapi_server.models.phone import Phone


pytestmark = pytest.mark.asyncio

async def test_set_phone_number_3(client):
    """Test case for set_phone_number_3

    Sets a customer's plus card phone number
    """
    phone_number = openapi_server.Phone()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts/account/plusCard/phone/{old_phone_number}'.format(old_phone_number='old_phone_number_example'),
        headers=headers,
        json=phone_number,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

