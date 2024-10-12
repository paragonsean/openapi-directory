# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_message_interaction_response import ListMessageInteractionResponse
from openapi_server.models.proxy_v1_service_session_participant_message_interaction import ProxyV1ServiceSessionParticipantMessageInteraction


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_message_interaction(client):
    """Test case for create_message_interaction

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'body': 'body_example',
        'media_url': ['media_url_example']
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions'.format(service_sid='service_sid_example', session_sid='session_sid_example', participant_sid='participant_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_message_interaction(client):
    """Test case for fetch_message_interaction

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions/{sid}'.format(service_sid='service_sid_example', session_sid='session_sid_example', participant_sid='participant_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_message_interaction(client):
    """Test case for list_message_interaction

    
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
        path='/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions'.format(service_sid='service_sid_example', session_sid='session_sid_example', participant_sid='participant_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

