# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.binding_enum_binding_type import BindingEnumBindingType
from openapi_server.models.chat_v2_service_binding import ChatV2ServiceBinding
from openapi_server.models.list_binding_response import ListBindingResponse


pytestmark = pytest.mark.asyncio

async def test_delete_binding(client):
    """Test case for delete_binding

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{service_sid}/Bindings/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_binding(client):
    """Test case for fetch_binding

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Bindings/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_binding(client):
    """Test case for list_binding

    
    """
    params = [('BindingType', [openapi_server.BindingEnumBindingType()]),
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
        path='/v2/Services/{service_sid}/Bindings'.format(service_sid='service_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

