# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_validation_request import ApiV2010AccountValidationRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_validation_request(client):
    """Test case for create_validation_request

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_delay': 56,
        'extension': 'extension_example',
        'friendly_name': 'friendly_name_example',
        'phone_number': 'phone_number_example',
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/OutgoingCallerIds.json'.format(account_sid='account_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

