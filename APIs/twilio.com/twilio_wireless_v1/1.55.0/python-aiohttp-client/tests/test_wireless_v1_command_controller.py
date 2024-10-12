# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.command_enum_command_mode import CommandEnumCommandMode
from openapi_server.models.command_enum_direction import CommandEnumDirection
from openapi_server.models.command_enum_status import CommandEnumStatus
from openapi_server.models.command_enum_transport import CommandEnumTransport
from openapi_server.models.list_command_response import ListCommandResponse
from openapi_server.models.wireless_v1_command import WirelessV1Command


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_command(client):
    """Test case for create_command

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'callback_method': 'callback_method_example',
        'callback_url': 'callback_url_example',
        'command': 'command_example',
        'command_mode': openapi_server.CommandEnumCommandMode(),
        'delivery_receipt_requested': True,
        'include_sid': 'include_sid_example',
        'sim': 'sim_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Commands',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_command(client):
    """Test case for delete_command

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Commands/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_command(client):
    """Test case for fetch_command

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Commands/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_command(client):
    """Test case for list_command

    
    """
    params = [('Sim', 'sim_example'),
                    ('Status', openapi_server.CommandEnumStatus()),
                    ('Direction', openapi_server.CommandEnumDirection()),
                    ('Transport', openapi_server.CommandEnumTransport()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Commands',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

