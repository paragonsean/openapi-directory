# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_input_callback_completion_batch_request import BatchInputCallbackCompletionBatchRequest
from openapi_server.models.callback_completion_request import CallbackCompletionRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_post_automation_v4_actions_callbacks_callback_id_complete_complete(client):
    """Test case for post_automation_v4_actions_callbacks_callback_id_complete_complete

    Completes a single callback
    """
    body = {"outputFields":{"key":"outputFields"}}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/automation/v4/actions/callbacks/{callback_id}/complete'.format(callback_id='callback_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_automation_v4_actions_callbacks_complete_complete_batch(client):
    """Test case for post_automation_v4_actions_callbacks_complete_complete_batch

    Completes a batch of callbacks
    """
    body = {"inputs":[{"outputFields":{"key":"outputFields"},"callbackId":"callbackId"},{"outputFields":{"key":"outputFields"},"callbackId":"callbackId"}]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/automation/v4/actions/callbacks/complete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

