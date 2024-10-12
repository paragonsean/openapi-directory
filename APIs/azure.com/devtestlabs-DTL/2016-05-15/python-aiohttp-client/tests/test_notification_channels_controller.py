# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.notification_channel import NotificationChannel
from openapi_server.models.notification_channel_fragment import NotificationChannelFragment
from openapi_server.models.notify_parameters import NotifyParameters
from openapi_server.models.response_with_continuation_notification_channel import ResponseWithContinuationNotificationChannel


pytestmark = pytest.mark.asyncio

async def test_notification_channels_create_or_update(client):
    """Test case for notification_channels_create_or_update

    
    """
    notification_channel = {"properties":{"createdDate":"2000-01-23T04:56:07.000+00:00","webHookUrl":"webHookUrl","description":"description","provisioningState":"provisioningState","events":[{"eventName":"AutoShutdown"},{"eventName":"AutoShutdown"}],"uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/notificationchannels/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=notification_channel,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_channels_delete(client):
    """Test case for notification_channels_delete

    
    """
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/notificationchannels/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_channels_get(client):
    """Test case for notification_channels_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/notificationchannels/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_channels_list(client):
    """Test case for notification_channels_list

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/notificationchannels'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_channels_notify(client):
    """Test case for notification_channels_notify

    
    """
    notify_parameters = {"jsonPayload":"jsonPayload","eventName":"AutoShutdown"}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/notificationchannels/{name}/notify'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=notify_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_channels_update(client):
    """Test case for notification_channels_update

    
    """
    notification_channel = {"properties":{"webHookUrl":"webHookUrl","description":"description","provisioningState":"provisioningState","events":[{"eventName":"AutoShutdown"},{"eventName":"AutoShutdown"}],"uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/notificationchannels/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=notification_channel,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

