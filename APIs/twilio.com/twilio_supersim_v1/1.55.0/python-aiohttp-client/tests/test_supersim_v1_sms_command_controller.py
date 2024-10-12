# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sms_command_response import ListSmsCommandResponse
from openapi_server.models.sms_command_enum_direction import SmsCommandEnumDirection
from openapi_server.models.sms_command_enum_status import SmsCommandEnumStatus
from openapi_server.models.supersim_v1_sms_command import SupersimV1SmsCommand


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_sms_command(client):
    """Test case for create_sms_command

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'callback_method': 'callback_method_example',
        'callback_url': 'callback_url_example',
        'payload': 'payload_example',
        'sim': 'sim_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/SmsCommands',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_sms_command(client):
    """Test case for fetch_sms_command

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/SmsCommands/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sms_command(client):
    """Test case for list_sms_command

    
    """
    params = [('Sim', 'sim_example'),
                    ('Status', openapi_server.SmsCommandEnumStatus()),
                    ('Direction', openapi_server.SmsCommandEnumDirection()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/SmsCommands',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

