# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_application import ApiV2010AccountApplication
from openapi_server.models.list_application_response import ListApplicationResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_application(client):
    """Test case for create_application

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'api_version': 'api_version_example',
        'friendly_name': 'friendly_name_example',
        'message_status_callback': 'message_status_callback_example',
        'public_application_connect_enabled': True,
        'sms_fallback_method': 'sms_fallback_method_example',
        'sms_fallback_url': 'sms_fallback_url_example',
        'sms_method': 'sms_method_example',
        'sms_status_callback': 'sms_status_callback_example',
        'sms_url': 'sms_url_example',
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example',
        'voice_caller_id_lookup': True,
        'voice_fallback_method': 'voice_fallback_method_example',
        'voice_fallback_url': 'voice_fallback_url_example',
        'voice_method': 'voice_method_example',
        'voice_url': 'voice_url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Applications.json'.format(account_sid='account_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_application(client):
    """Test case for delete_application

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Applications/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_application(client):
    """Test case for fetch_application

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Applications/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_application(client):
    """Test case for list_application

    
    """
    params = [('FriendlyName', 'friendly_name_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Applications.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_application(client):
    """Test case for update_application

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'api_version': 'api_version_example',
        'friendly_name': 'friendly_name_example',
        'message_status_callback': 'message_status_callback_example',
        'public_application_connect_enabled': True,
        'sms_fallback_method': 'sms_fallback_method_example',
        'sms_fallback_url': 'sms_fallback_url_example',
        'sms_method': 'sms_method_example',
        'sms_status_callback': 'sms_status_callback_example',
        'sms_url': 'sms_url_example',
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example',
        'voice_caller_id_lookup': True,
        'voice_fallback_method': 'voice_fallback_method_example',
        'voice_fallback_url': 'voice_fallback_url_example',
        'voice_method': 'voice_method_example',
        'voice_url': 'voice_url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Applications/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

