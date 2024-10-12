# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.send_an_sms200_response import SendAnSms200Response
from openapi_server.models.send_an_sms200_response1 import SendAnSms200Response1


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_send_an_sms(client):
    """Test case for send_an_sms

    Send an SMS
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'account_ref': 'account_ref_example',
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'body': 'body_example',
        'param_callback': 'param_callback_example',
        'client_ref': 'client_ref_example',
        'content_id': 'content_id_example',
        'entity_id': 'entity_id_example',
        '_from': '_from_example',
        'message_class': 56,
        'protocol_id': 56,
        'sig': 'sig_example',
        'status_report_req': True,
        'text': 'text_example',
        'to': 'to_example',
        'ttl': 259200000,
        'type': text,
        'udh': 'udh_example'
        }
    response = await client.request(
        method='POST',
        path='/sms/{format}'.format(format=json),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

