# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_call_call_notification_instance import ApiV2010AccountCallCallNotificationInstance
from openapi_server.models.api_v2010_account_notification_instance import ApiV2010AccountNotificationInstance
from openapi_server.models.list_call_notification_response import ListCallNotificationResponse
from openapi_server.models.list_notification_response import ListNotificationResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_call_notification(client):
    """Test case for fetch_call_notification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Notifications/{sid_jso}'.format(account_sid='account_sid_example', call_sid='call_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_notification(client):
    """Test case for fetch_notification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Notifications/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_call_notification(client):
    """Test case for list_call_notification

    
    """
    params = [('Log', 56),
                    ('MessageDate', '2013-10-20'),
                    ('MessageDate&lt;', '2013-10-20'),
                    ('MessageDate&gt;', '2013-10-20'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Notifications.json'.format(account_sid='account_sid_example', call_sid='call_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_notification(client):
    """Test case for list_notification

    
    """
    params = [('Log', 56),
                    ('MessageDate', '2013-10-20'),
                    ('MessageDate&lt;', '2013-10-20'),
                    ('MessageDate&gt;', '2013-10-20'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Notifications.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

