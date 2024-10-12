# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on_incoming_phone_number_assigned_add_on_extension import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension
from openapi_server.models.list_incoming_phone_number_assigned_add_on_extension_response import ListIncomingPhoneNumberAssignedAddOnExtensionResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_incoming_phone_number_assigned_add_on_extension(client):
    """Test case for fetch_incoming_phone_number_assigned_add_on_extension

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions/{sid_jso}'.format(account_sid='account_sid_example', resource_sid='resource_sid_example', assigned_add_on_sid='assigned_add_on_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_incoming_phone_number_assigned_add_on_extension(client):
    """Test case for list_incoming_phone_number_assigned_add_on_extension

    
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
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions.json'.format(account_sid='account_sid_example', resource_sid='resource_sid_example', assigned_add_on_sid='assigned_add_on_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

