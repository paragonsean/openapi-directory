# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_participant_response import ListParticipantResponse
from openapi_server.models.proxy_v1_service_session_participant import ProxyV1ServiceSessionParticipant


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_participant(client):
    """Test case for create_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'friendly_name': 'friendly_name_example',
        'identifier': 'identifier_example',
        'proxy_identifier': 'proxy_identifier_example',
        'proxy_identifier_sid': 'proxy_identifier_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Sessions/{session_sid}/Participants'.format(service_sid='service_sid_example', session_sid='session_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_participant(client):
    """Test case for delete_participant

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{sid}'.format(service_sid='service_sid_example', session_sid='session_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_participant(client):
    """Test case for fetch_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Sessions/{session_sid}/Participants/{sid}'.format(service_sid='service_sid_example', session_sid='session_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_participant(client):
    """Test case for list_participant

    
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
        path='/v1/Services/{service_sid}/Sessions/{session_sid}/Participants'.format(service_sid='service_sid_example', session_sid='session_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

