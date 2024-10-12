# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification_get_default_response import NotificationGetDefaultResponse
from openapi_server.models.recipient_user_contract import RecipientUserContract


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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/notifications/{notification_name}/recipientUsers/{uid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', notification_name='notification_name_example', uid='uid_example', subscription_id='subscription_id_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/notifications/{notification_name}/recipientUsers/{uid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', notification_name='notification_name_example', uid='uid_example', subscription_id='subscription_id_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/notifications/{notification_name}/recipientUsers/{uid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', notification_name='notification_name_example', uid='uid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

