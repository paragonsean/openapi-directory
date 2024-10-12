# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_errors import AccountErrors
from openapi_server.models.phone import Phone
from openapi_server.models.plus_card_details import PlusCardDetails


pytestmark = pytest.mark.asyncio

async def test_get_plus_card_details_0(client):
    """Test case for get_plus_card_details_0

    Gets a customer's plus card details if they exist.
    """
    params = [('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/accounts/account/plusCard',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_lost_stolen_0(client):
    """Test case for set_lost_stolen_0

    Sets a customer's plus card as Lost/Stolen
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'api_ticket': 'api_ticket_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts/account/plusCard/lostStolen',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_phone_number_0(client):
    """Test case for set_phone_number_0

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


pytestmark = pytest.mark.asyncio

async def test_set_pin_0(client):
    """Test case for set_pin_0

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

async def test_update_pin_0(client):
    """Test case for update_pin_0

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

