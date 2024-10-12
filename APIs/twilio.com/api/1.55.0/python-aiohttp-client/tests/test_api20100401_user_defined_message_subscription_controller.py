# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_call_user_defined_message_subscription import ApiV2010AccountCallUserDefinedMessageSubscription


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_user_defined_message_subscription(client):
    """Test case for create_user_defined_message_subscription

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'callback': 'callback_example',
        'idempotency_key': 'idempotency_key_example',
        'method': 'method_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/UserDefinedMessageSubscriptions.json'.format(account_sid='account_sid_example', call_sid='call_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_defined_message_subscription(client):
    """Test case for delete_user_defined_message_subscription

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/UserDefinedMessageSubscriptions/{sid_jso}'.format(account_sid='account_sid_example', call_sid='call_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

