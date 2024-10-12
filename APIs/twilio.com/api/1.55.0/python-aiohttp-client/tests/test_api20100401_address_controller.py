# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_address import ApiV2010AccountAddress
from openapi_server.models.list_address_response import ListAddressResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_address(client):
    """Test case for create_address

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'auto_correct_address': True,
        'city': 'city_example',
        'customer_name': 'customer_name_example',
        'emergency_enabled': True,
        'friendly_name': 'friendly_name_example',
        'iso_country': 'iso_country_example',
        'postal_code': 'postal_code_example',
        'region': 'region_example',
        'street': 'street_example',
        'street_secondary': 'street_secondary_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Addresses.json'.format(account_sid='account_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_address(client):
    """Test case for delete_address

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Addresses/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_address(client):
    """Test case for fetch_address

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Addresses/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_address(client):
    """Test case for list_address

    
    """
    params = [('CustomerName', 'customer_name_example'),
                    ('FriendlyName', 'friendly_name_example'),
                    ('IsoCountry', 'iso_country_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Addresses.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_address(client):
    """Test case for update_address

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'auto_correct_address': True,
        'city': 'city_example',
        'customer_name': 'customer_name_example',
        'emergency_enabled': True,
        'friendly_name': 'friendly_name_example',
        'postal_code': 'postal_code_example',
        'region': 'region_example',
        'street': 'street_example',
        'street_secondary': 'street_secondary_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Addresses/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

