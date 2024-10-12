# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server.models.notify_v1_service import NotifyV1Service


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_service(client):
    """Test case for create_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'alexa_skill_id': 'alexa_skill_id_example',
        'apn_credential_sid': 'apn_credential_sid_example',
        'default_alexa_notification_protocol_version': 'default_alexa_notification_protocol_version_example',
        'default_apn_notification_protocol_version': 'default_apn_notification_protocol_version_example',
        'default_fcm_notification_protocol_version': 'default_fcm_notification_protocol_version_example',
        'default_gcm_notification_protocol_version': 'default_gcm_notification_protocol_version_example',
        'delivery_callback_enabled': True,
        'delivery_callback_url': 'delivery_callback_url_example',
        'facebook_messenger_page_id': 'facebook_messenger_page_id_example',
        'fcm_credential_sid': 'fcm_credential_sid_example',
        'friendly_name': 'friendly_name_example',
        'gcm_credential_sid': 'gcm_credential_sid_example',
        'log_enabled': True,
        'messaging_service_sid': 'messaging_service_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service(client):
    """Test case for delete_service

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service(client):
    """Test case for fetch_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service(client):
    """Test case for list_service

    
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
        path='/v1/Services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service(client):
    """Test case for update_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'alexa_skill_id': 'alexa_skill_id_example',
        'apn_credential_sid': 'apn_credential_sid_example',
        'default_alexa_notification_protocol_version': 'default_alexa_notification_protocol_version_example',
        'default_apn_notification_protocol_version': 'default_apn_notification_protocol_version_example',
        'default_fcm_notification_protocol_version': 'default_fcm_notification_protocol_version_example',
        'default_gcm_notification_protocol_version': 'default_gcm_notification_protocol_version_example',
        'delivery_callback_enabled': True,
        'delivery_callback_url': 'delivery_callback_url_example',
        'facebook_messenger_page_id': 'facebook_messenger_page_id_example',
        'fcm_credential_sid': 'fcm_credential_sid_example',
        'friendly_name': 'friendly_name_example',
        'gcm_credential_sid': 'gcm_credential_sid_example',
        'log_enabled': True,
        'messaging_service_sid': 'messaging_service_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

