# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_details import DeviceDetails
from openapi_server.models.error import Error
from openapi_server.models.publish_push_notification_to_devices_request import PublishPushNotificationToDevicesRequest
from openapi_server.models.subscribe_push_device_to_channel_request import SubscribePushDeviceToChannelRequest


pytestmark = pytest.mark.asyncio

async def test_delete_push_device_details(client):
    """Test case for delete_push_device_details

    Delete a registered device's update token
    """
    params = [('format', 'format_example'),
                    ('channel', 'channel_example'),
                    ('deviceId', 'device_id_example'),
                    ('clientId', 'client_id_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/push/channelSubscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channels_with_push_subscribers(client):
    """Test case for get_channels_with_push_subscribers

    List all channels with at least one subscribed device
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/push/channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_push_device_details(client):
    """Test case for get_push_device_details

    Get a device registration
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/push/deviceRegistrations/{device_id}'.format(device_id='device_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_push_subscriptions_on_channels(client):
    """Test case for get_push_subscriptions_on_channels

    List channel subscriptions
    """
    params = [('format', 'format_example'),
                    ('channel', 'channel_example'),
                    ('deviceId', 'device_id_example'),
                    ('clientId', 'client_id_example'),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/push/channelSubscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registered_push_devices(client):
    """Test case for get_registered_push_devices

    List devices registered for receiving push notifications
    """
    params = [('format', 'format_example'),
                    ('deviceId', 'device_id_example'),
                    ('clientId', 'client_id_example'),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/push/deviceRegistrations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_patch_push_device_details(client):
    """Test case for patch_push_device_details

    Update a device registration
    """
    body = {"deviceSecret":"deviceSecret","metadata":"{}","clientId":"clientId","formFactor":"phone","push.recipient":{"registrationToken":"registrationToken","clientId":"clientId","transportType":"apns","deviceId":"deviceId","deviceToken":"deviceToken"},"id":"id","push.state":"Active","platform":"ios"}
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/push/deviceRegistrations/{device_id}'.format(device_id='device_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_publish_push_notification_to_devices(client):
    """Test case for publish_push_notification_to_devices

    Publish a push notification to device(s)
    """
    body = openapi_server.PublishPushNotificationToDevicesRequest()
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/push/publish',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_push_device_details(client):
    """Test case for put_push_device_details

    Update a device registration
    """
    body = {"deviceSecret":"deviceSecret","metadata":"{}","clientId":"clientId","formFactor":"phone","push.recipient":{"registrationToken":"registrationToken","clientId":"clientId","transportType":"apns","deviceId":"deviceId","deviceToken":"deviceToken"},"id":"id","push.state":"Active","platform":"ios"}
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/push/deviceRegistrations/{device_id}'.format(device_id='device_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_register_push_device(client):
    """Test case for register_push_device

    Register a device for receiving push notifications
    """
    body = {"deviceSecret":"deviceSecret","metadata":"{}","clientId":"clientId","formFactor":"phone","push.recipient":{"registrationToken":"registrationToken","clientId":"clientId","transportType":"apns","deviceId":"deviceId","deviceToken":"deviceToken"},"id":"id","push.state":"Active","platform":"ios"}
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/push/deviceRegistrations',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_subscribe_push_device_to_channel(client):
    """Test case for subscribe_push_device_to_channel

    Subscribe a device to a channel
    """
    body = {"channel":"my:channel","clientId":"myClientId"}
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/push/channelSubscriptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unregister_all_push_devices(client):
    """Test case for unregister_all_push_devices

    Unregister matching devices for push notifications
    """
    params = [('format', 'format_example'),
                    ('deviceId', 'device_id_example'),
                    ('clientId', 'client_id_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/push/deviceRegistrations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unregister_push_device(client):
    """Test case for unregister_push_device

    Unregister a single device for push notifications
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/push/deviceRegistrations/{device_id}'.format(device_id='device_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_push_device_details(client):
    """Test case for update_push_device_details

    Reset a registered device's update token
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/push/deviceRegistrations/{device_id}/resetUpdateToken'.format(device_id='device_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

