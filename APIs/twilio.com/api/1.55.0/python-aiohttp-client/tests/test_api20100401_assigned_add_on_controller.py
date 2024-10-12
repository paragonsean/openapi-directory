# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn
from openapi_server.models.list_incoming_phone_number_assigned_add_on_response import ListIncomingPhoneNumberAssignedAddOnResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_incoming_phone_number_assigned_add_on(client):
    """Test case for create_incoming_phone_number_assigned_add_on

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'installed_add_on_sid': 'installed_add_on_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns.json'.format(account_sid='account_sid_example', resource_sid='resource_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_incoming_phone_number_assigned_add_on(client):
    """Test case for delete_incoming_phone_number_assigned_add_on

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{sid_jso}'.format(account_sid='account_sid_example', resource_sid='resource_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_incoming_phone_number_assigned_add_on(client):
    """Test case for fetch_incoming_phone_number_assigned_add_on

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{sid_jso}'.format(account_sid='account_sid_example', resource_sid='resource_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_incoming_phone_number_assigned_add_on(client):
    """Test case for list_incoming_phone_number_assigned_add_on

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns.json'.format(account_sid='account_sid_example', resource_sid='resource_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

