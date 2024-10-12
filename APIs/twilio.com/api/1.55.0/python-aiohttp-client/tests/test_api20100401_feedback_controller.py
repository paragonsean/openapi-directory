# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_message_message_feedback import ApiV2010AccountMessageMessageFeedback
from openapi_server.models.message_feedback_enum_outcome import MessageFeedbackEnumOutcome


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_message_feedback(client):
    """Test case for create_message_feedback

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'outcome': openapi_server.MessageFeedbackEnumOutcome()
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Feedback.json'.format(account_sid='account_sid_example', message_sid='message_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

