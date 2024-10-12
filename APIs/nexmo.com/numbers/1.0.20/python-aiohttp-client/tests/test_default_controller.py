# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_unauthorized import AccountUnauthorized
from openapi_server.models.available_numbers import AvailableNumbers
from openapi_server.models.inbound_numbers import InboundNumbers
from openapi_server.models.response import Response
from openapi_server.models.response420 import Response420
from openapi_server.models.unauthorized import Unauthorized


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_buy_a_number(client):
    """Test case for buy_a_number

    Buy a number
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'apiKey': 'special-key',
        'apiSecret': 'special-key',
    }
    data = {
        'country': 'country_example',
        'msisdn': 'msisdn_example',
        'target_api_key': 'target_api_key_example'
        }
    response = await client.request(
        method='POST',
        path='/number/buy',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_cancel_a_number(client):
    """Test case for cancel_a_number

    Cancel a number
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'apiKey': 'special-key',
        'apiSecret': 'special-key',
    }
    data = {
        'country': 'country_example',
        'msisdn': 'msisdn_example',
        'target_api_key': 'target_api_key_example'
        }
    response = await client.request(
        method='POST',
        path='/number/cancel',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_available_numbers(client):
    """Test case for get_available_numbers

    Search available numbers
    """
    params = [('country', 'country_example'),
                    ('type', 'mobile-lvn'),
                    ('pattern', '12345'),
                    ('search_pattern', 0),
                    ('features', 'SMS'),
                    ('size', 10),
                    ('index', 1)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
        'apiSecret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/number/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_owned_numbers(client):
    """Test case for get_owned_numbers

    List the numbers you own
    """
    params = [('application_id', 'aaaaaaaa-bbbb-cccc-dddd-0123456789ab'),
                    ('has_application', false),
                    ('country', 'country_example'),
                    ('pattern', '12345'),
                    ('search_pattern', 0),
                    ('size', 10),
                    ('index', 1)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
        'apiSecret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/numbers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_a_number(client):
    """Test case for update_a_number

    Update a number
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'apiKey': 'special-key',
        'apiSecret': 'special-key',
    }
    data = {
        'app_id': 'app_id_example',
        'country': 'country_example',
        'messages_callback_type': 'messages_callback_type_example',
        'messages_callback_value': 'messages_callback_value_example',
        'mo_http_url': 'mo_http_url_example',
        'mo_smpp_sys_type': 'mo_smpp_sys_type_example',
        'msisdn': 'msisdn_example',
        'voice_callback_type': 'voice_callback_type_example',
        'voice_callback_value': 'voice_callback_value_example',
        'voice_status_callback': 'voice_status_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/number/update',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

