# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_key_pair_request import CreateKeyPairRequest
from openapi_server.models.create_webhook_request import CreateWebhookRequest
from openapi_server.models.customer_settings_request import CustomerSettingsRequest
from openapi_server.models.customer_settings_response import CustomerSettingsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.event_type_list import EventTypeList
from openapi_server.models.notification_channel_activation_request import NotificationChannelActivationRequest
from openapi_server.models.notification_channel_list import NotificationChannelList
from openapi_server.models.update_webhook_request import UpdateWebhookRequest
from openapi_server.models.user_key_pair_container import UserKeyPairContainer
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhook_list import WebhookList


pytestmark = pytest.mark.asyncio

async def test_create_and_preserve_key_pair(client):
    """Test case for create_and_preserve_key_pair

    Create system rescue key pair and preserve copy of old private key
    """
    body = {"privateKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"previousPrivateKey":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"publicKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","createdBy":5,"publicKey":"publicKey","version":"version"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/settings/keypairs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_webhook(client):
    """Test case for create_webhook

    Create webhook
    """
    body = {"eventTypeNames":["eventTypeNames","eventTypeNames"],"isEnabled":True,"name":"name","secret":"secret","triggerExampleEvent":True,"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/settings/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_system_rescue_key_pair(client):
    """Test case for remove_system_rescue_key_pair

    Remove system rescue key pair
    """
    params = [('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/settings/keypair',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_webhook(client):
    """Test case for remove_webhook

    Remove webhook
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/settings/webhooks/{webhook_id}'.format(webhook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_all_system_rescue_key_pairs(client):
    """Test case for request_all_system_rescue_key_pairs

    Request all system rescue key pairs
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/settings/keypairs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_list_of_event_types_for_config_manager(client):
    """Test case for request_list_of_event_types_for_config_manager

    Request list of event types
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/settings/webhooks/event_types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_list_of_webhooks(client):
    """Test case for request_list_of_webhooks

    Request list of webhooks
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/settings/webhooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_notification_channels(client):
    """Test case for request_notification_channels

    Request list of notification channels
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/settings/notifications/channels',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_settings(client):
    """Test case for request_settings

    Request customer settings
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_system_rescue_key_pair(client):
    """Test case for request_system_rescue_key_pair

    Request system rescue key pair
    """
    params = [('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/settings/keypair',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_webhook(client):
    """Test case for request_webhook

    Request webhook
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/settings/webhooks/{webhook_id}'.format(webhook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_webhook_lifetime(client):
    """Test case for reset_webhook_lifetime

    Reset webhook lifetime
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/settings/webhooks/{webhook_id}/reset_lifetime'.format(webhook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_settings(client):
    """Test case for set_settings

    Set customer settings
    """
    body = {"homeRoomQuota":0,"homeRoomsActive":True,"homeRoomParentName":"homeRoomParentName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/settings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_system_rescue_key_pair(client):
    """Test case for set_system_rescue_key_pair

    Activate client-side encryption for customer
    """
    body = {"privateKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","privateKey":"privateKey","createdBy":0,"version":"version"},"publicKeyContainer":{"createdAt":"2000-01-23T04:56:07.000+00:00","createdBy":5,"publicKey":"publicKey","version":"version"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/settings/keypair',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_toggle_notification_channels(client):
    """Test case for toggle_notification_channels

    Toggle notification channels
    """
    body = {"isEnabled":True,"channelId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/settings/notifications/channels',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webhook(client):
    """Test case for update_webhook

    Update webhook
    """
    body = {"eventTypeNames":["eventTypeNames","eventTypeNames"],"isEnabled":True,"name":"name","secret":"secret","triggerExampleEvent":True,"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/settings/webhooks/{webhook_id}'.format(webhook_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

