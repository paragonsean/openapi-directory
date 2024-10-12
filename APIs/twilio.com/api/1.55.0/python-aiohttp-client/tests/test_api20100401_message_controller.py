# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_message import ApiV2010AccountMessage
from openapi_server.models.list_message_response import ListMessageResponse
from openapi_server.models.message_enum_address_retention import MessageEnumAddressRetention
from openapi_server.models.message_enum_content_retention import MessageEnumContentRetention
from openapi_server.models.message_enum_risk_check import MessageEnumRiskCheck
from openapi_server.models.message_enum_schedule_type import MessageEnumScheduleType
from openapi_server.models.message_enum_update_status import MessageEnumUpdateStatus


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_message(client):
    """Test case for create_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'address_retention': openapi_server.MessageEnumAddressRetention(),
        'application_sid': 'application_sid_example',
        'attempt': 56,
        'body': 'body_example',
        'content_retention': openapi_server.MessageEnumContentRetention(),
        'content_sid': 'content_sid_example',
        'content_variables': 'content_variables_example',
        'force_delivery': True,
        '_from': '_from_example',
        'max_price': 3.4,
        'media_url': ['media_url_example'],
        'messaging_service_sid': 'messaging_service_sid_example',
        'persistent_action': ['persistent_action_example'],
        'provide_feedback': True,
        'risk_check': openapi_server.MessageEnumRiskCheck(),
        'schedule_type': openapi_server.MessageEnumScheduleType(),
        'send_as_mms': True,
        'send_at': '2013-10-20T19:20:30+01:00',
        'shorten_urls': True,
        'smart_encoded': True,
        'status_callback': 'status_callback_example',
        'to': 'to_example',
        'validity_period': 56
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Messages.json'.format(account_sid='account_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_message(client):
    """Test case for delete_message

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Messages/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_message(client):
    """Test case for fetch_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Messages/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_message(client):
    """Test case for list_message

    
    """
    params = [('To', 'to_example'),
                    ('From', '_from_example'),
                    ('DateSent', '2013-10-20T19:20:30+01:00'),
                    ('DateSent&lt;', '2013-10-20T19:20:30+01:00'),
                    ('DateSent&gt;', '2013-10-20T19:20:30+01:00'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Messages.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_message(client):
    """Test case for update_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'body': 'body_example',
        'status': openapi_server.MessageEnumUpdateStatus()
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Messages/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

