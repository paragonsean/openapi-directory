# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversations_v1_service_service_binding import ConversationsV1ServiceServiceBinding
from openapi_server.models.list_service_binding_response import ListServiceBindingResponse
from openapi_server.models.service_binding_enum_binding_type import ServiceBindingEnumBindingType


pytestmark = pytest.mark.asyncio

async def test_delete_service_binding(client):
    """Test case for delete_service_binding

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{chat_service_sid}/Bindings/{sid}'.format(chat_service_sid='chat_service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service_binding(client):
    """Test case for fetch_service_binding

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Bindings/{sid}'.format(chat_service_sid='chat_service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_binding(client):
    """Test case for list_service_binding

    
    """
    params = [('BindingType', [openapi_server.ServiceBindingEnumBindingType()]),
                    ('Identity', ['identity_example']),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{chat_service_sid}/Bindings'.format(chat_service_sid='chat_service_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

