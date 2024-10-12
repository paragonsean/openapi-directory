# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_media_intent_handling_invocation import AddMediaIntentHandlingInvocation
from openapi_server.models.add_media_intent_handling_invocation_response import AddMediaIntentHandlingInvocationResponse
from openapi_server.models.play_media_intent_handling_invocation import PlayMediaIntentHandlingInvocation
from openapi_server.models.play_media_intent_handling_invocation_response import PlayMediaIntentHandlingInvocationResponse
from openapi_server.models.update_media_affinity_intent_handling_invocation import UpdateMediaAffinityIntentHandlingInvocation
from openapi_server.models.update_media_affinity_intent_handling_invocation_response import UpdateMediaAffinityIntentHandlingInvocationResponse


pytestmark = pytest.mark.asyncio

async def test_add_media_intent_handling(client):
    """Test case for add_media_intent_handling

    addMedia
    """
    body = {"method":"AddMediaIntentHandling.resolveMediaItems","params":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_applecloudextension_session_id': 'x_applecloudextension_session_id_example',
        'x_applecloudextension_retry_count': 3.4,
        'request_timeout': 3.4,
        'user_agent': 'user_agent_example',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='POST',
        path='/api/intent/addMedia',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_play_media_intent_handling(client):
    """Test case for play_media_intent_handling

    playMedia
    """
    body = {"method":"PlayMediaIntentHandling.resolveMediaItems","params":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_applecloudextension_session_id': 'x_applecloudextension_session_id_example',
        'x_applecloudextension_retry_count': 3.4,
        'request_timeout': 3.4,
        'user_agent': 'user_agent_example',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='POST',
        path='/api/intent/playMedia',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_media_affinity_intent_handling(client):
    """Test case for update_media_affinity_intent_handling

    updateMediaAffinity
    """
    body = {"method":"UpdateMediaAffinityIntentHandling.resolveMediaItems","params":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_applecloudextension_session_id': 'x_applecloudextension_session_id_example',
        'x_applecloudextension_retry_count': 3.4,
        'request_timeout': 3.4,
        'user_agent': 'user_agent_example',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='POST',
        path='/api/intent/updateMediaAffinity',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

