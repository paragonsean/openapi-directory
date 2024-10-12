# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_wireless_command_response import ListWirelessCommandResponse
from openapi_server.models.preview_wireless_command import PreviewWirelessCommand


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_wireless_command(client):
    """Test case for create_wireless_command

    
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
        'command_mode': 'command_mode_example',
        'device': 'device_example',
        'include_sid': 'include_sid_example',
        'sim': 'sim_example'
        }
    response = await client.request(
        method='POST',
        path='/wireless/Commands',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_wireless_command(client):
    """Test case for fetch_wireless_command

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/wireless/Commands/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_wireless_command(client):
    """Test case for list_wireless_command

    
    """
    params = [('Device', 'device_example'),
                    ('Sim', 'sim_example'),
                    ('Status', 'status_example'),
                    ('Direction', 'direction_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/wireless/Commands',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

