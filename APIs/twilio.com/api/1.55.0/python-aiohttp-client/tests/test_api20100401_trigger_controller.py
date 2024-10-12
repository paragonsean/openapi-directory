# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_usage_usage_trigger import ApiV2010AccountUsageUsageTrigger
from openapi_server.models.list_usage_trigger_response import ListUsageTriggerResponse
from openapi_server.models.usage_trigger_enum_recurring import UsageTriggerEnumRecurring
from openapi_server.models.usage_trigger_enum_trigger_field import UsageTriggerEnumTriggerField
from openapi_server.models.usage_trigger_enum_usage_category import UsageTriggerEnumUsageCategory


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_usage_trigger(client):
    """Test case for create_usage_trigger

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'callback_method': 'callback_method_example',
        'callback_url': 'callback_url_example',
        'friendly_name': 'friendly_name_example',
        'recurring': openapi_server.UsageTriggerEnumRecurring(),
        'trigger_by': openapi_server.UsageTriggerEnumTriggerField(),
        'trigger_value': 'trigger_value_example',
        'usage_category': openapi_server.UsageTriggerEnumUsageCategory()
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Usage/Triggers.json'.format(account_sid='account_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_usage_trigger(client):
    """Test case for delete_usage_trigger

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_usage_trigger(client):
    """Test case for fetch_usage_trigger

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_usage_trigger(client):
    """Test case for list_usage_trigger

    
    """
    params = [('Recurring', openapi_server.UsageTriggerEnumRecurring()),
                    ('TriggerBy', openapi_server.UsageTriggerEnumTriggerField()),
                    ('UsageCategory', openapi_server.UsageTriggerEnumUsageCategory()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Usage/Triggers.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_usage_trigger(client):
    """Test case for update_usage_trigger

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'callback_method': 'callback_method_example',
        'callback_url': 'callback_url_example',
        'friendly_name': 'friendly_name_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Usage/Triggers/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

