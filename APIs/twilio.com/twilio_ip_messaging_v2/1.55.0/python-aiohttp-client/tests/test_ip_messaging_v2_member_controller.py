# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ip_messaging_v2_service_channel_member import IpMessagingV2ServiceChannelMember
from openapi_server.models.list_member_response import ListMemberResponse
from openapi_server.models.member_enum_webhook_enabled_type import MemberEnumWebhookEnabledType


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_member(client):
    """Test case for create_member

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.MemberEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'identity': 'identity_example',
        'last_consumed_message_index': 56,
        'last_consumption_timestamp': '2013-10-20T19:20:30+01:00',
        'role_sid': 'role_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Members'.format(service_sid='service_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_member(client):
    """Test case for delete_member

    
    """
    headers = { 
        'x_twilio_webhook_enabled': openapi_server.MemberEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_member(client):
    """Test case for fetch_member

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_member(client):
    """Test case for list_member

    
    """
    params = [('Identity', ['identity_example']),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Members'.format(service_sid='service_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_member(client):
    """Test case for update_member

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_twilio_webhook_enabled': openapi_server.MemberEnumWebhookEnabledType(),
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'date_created': '2013-10-20T19:20:30+01:00',
        'date_updated': '2013-10-20T19:20:30+01:00',
        'last_consumed_message_index': 56,
        'last_consumption_timestamp': '2013-10-20T19:20:30+01:00',
        'role_sid': 'role_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

