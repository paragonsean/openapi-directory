# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ip_command_enum_direction import IpCommandEnumDirection
from openapi_server.models.ip_command_enum_payload_type import IpCommandEnumPayloadType
from openapi_server.models.ip_command_enum_status import IpCommandEnumStatus
from openapi_server.models.list_ip_command_response import ListIpCommandResponse
from openapi_server.models.supersim_v1_ip_command import SupersimV1IpCommand


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_ip_command(client):
    """Test case for create_ip_command

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'callback_method': 'callback_method_example',
        'callback_url': 'callback_url_example',
        'device_port': 56,
        'payload': 'payload_example',
        'payload_type': openapi_server.IpCommandEnumPayloadType(),
        'sim': 'sim_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/IpCommands',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_ip_command(client):
    """Test case for fetch_ip_command

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/IpCommands/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_ip_command(client):
    """Test case for list_ip_command

    
    """
    params = [('Sim', 'sim_example'),
                    ('SimIccid', 'sim_iccid_example'),
                    ('Status', openapi_server.IpCommandEnumStatus()),
                    ('Direction', openapi_server.IpCommandEnumDirection()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/IpCommands',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

