# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.create_device_request import CreateDeviceRequest
from openapi_server.models.list_push_providers_response import ListPushProvidersResponse
from openapi_server.models.response import Response
from openapi_server.models.upsert_push_provider_request import UpsertPushProviderRequest
from openapi_server.models.upsert_push_provider_response import UpsertPushProviderResponse


pytestmark = pytest.mark.asyncio

async def test_create_device_0(client):
    """Test case for create_device_0

    Create device
    """
    body = {"user_id":"user_id","push_provider_name":"push_provider_name","push_provider":"firebase","id":"id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/devices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_push_provider(client):
    """Test case for delete_push_provider

    Delete a push provider
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/push_providers/{type}/{name}'.format(type='type_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_push_providers(client):
    """Test case for list_push_providers

    List push providers
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/push_providers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_push_provider(client):
    """Test case for upsert_push_provider

    Upsert a push provider
    """
    body = {"push_provider":{"xiaomi_package_name":"xiaomi_package_name","apn_key_id":"apn_key_id","created_at":"2000-01-23T04:56:07.000+00:00","description":"description","firebase_data_template":"firebase_data_template","type":0,"firebase_credentials":"firebase_credentials","apn_p12_cert":"apn_p12_cert","updated_at":"2000-01-23T04:56:07.000+00:00","firebase_apn_template":"firebase_apn_template","apn_auth_key":"apn_auth_key","apn_topic":"apn_topic","apn_host":"apn_host","apn_development":True,"apn_auth_type":"apn_auth_type","disabled_at":"2000-01-23T04:56:07.000+00:00","xiaomi_app_secret":"xiaomi_app_secret","firebase_server_key":"firebase_server_key","apn_team_id":"apn_team_id","disabled_reason":"disabled_reason","huawei_app_secret":"huawei_app_secret","huawei_app_id":"huawei_app_id","name":"name","firebase_notification_template":"firebase_notification_template","apn_notification_template":"apn_notification_template"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/push_providers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

