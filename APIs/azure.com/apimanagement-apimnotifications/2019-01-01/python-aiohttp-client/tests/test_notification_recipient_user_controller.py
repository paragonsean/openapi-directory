# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification_list_by_service_default_response import NotificationListByServiceDefaultResponse
from openapi_server.models.notification_recipient_user_create_or_update200_response import NotificationRecipientUserCreateOrUpdate200Response
from openapi_server.models.notification_recipient_user_list_by_notification200_response import NotificationRecipientUserListByNotification200Response


pytestmark = pytest.mark.asyncio

async def test_notification_recipient_user_check_entity_exists(client):
    """Test case for notification_recipient_user_check_entity_exists

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/notifications/{notification_name}/recipientUsers/{user_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', notification_name='notification_name_example', user_id='user_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_recipient_user_create_or_update(client):
    """Test case for notification_recipient_user_create_or_update

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/notifications/{notification_name}/recipientUsers/{user_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', notification_name='notification_name_example', user_id='user_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_recipient_user_delete(client):
    """Test case for notification_recipient_user_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/notifications/{notification_name}/recipientUsers/{user_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', notification_name='notification_name_example', user_id='user_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_recipient_user_list_by_notification(client):
    """Test case for notification_recipient_user_list_by_notification

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/notifications/{notification_name}/recipientUsers'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', notification_name='notification_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

