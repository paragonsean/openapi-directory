# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.binding_enum_binding_type import BindingEnumBindingType
from openapi_server.models.list_binding_response import ListBindingResponse
from openapi_server.models.notify_v1_service_binding import NotifyV1ServiceBinding


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_binding(client):
    """Test case for create_binding

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'address': 'address_example',
        'binding_type': openapi_server.BindingEnumBindingType(),
        'credential_sid': 'credential_sid_example',
        'endpoint': 'endpoint_example',
        'identity': 'identity_example',
        'notification_protocol_version': 'notification_protocol_version_example',
        'tag': ['tag_example']
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Bindings'.format(service_sid='service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_binding(client):
    """Test case for delete_binding

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{service_sid}/Bindings/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
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
        path='/v1/Services/{service_sid}/Bindings/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_binding(client):
    """Test case for list_binding

    
    """
    params = [('StartDate', '2013-10-20'),
                    ('EndDate', '2013-10-20'),
                    ('Identity', ['identity_example']),
                    ('Tag', ['tag_example']),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Bindings'.format(service_sid='service_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

