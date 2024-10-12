# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chat_v2_service_user_user_binding import ChatV2ServiceUserUserBinding
from openapi_server.models.list_user_binding_response import ListUserBindingResponse
from openapi_server.models.user_binding_enum_binding_type import UserBindingEnumBindingType


pytestmark = pytest.mark.asyncio

async def test_delete_user_binding(client):
    """Test case for delete_user_binding

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}'.format(service_sid='service_sid_example', user_sid='user_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_user_binding(client):
    """Test case for fetch_user_binding

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}'.format(service_sid='service_sid_example', user_sid='user_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_binding(client):
    """Test case for list_user_binding

    
    """
    params = [('BindingType', [openapi_server.UserBindingEnumBindingType()]),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Users/{user_sid}/Bindings'.format(service_sid='service_sid_example', user_sid='user_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

