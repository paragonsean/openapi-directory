# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_log_alert_list import ActivityLogAlertList
from openapi_server.models.activity_log_alert_patch_body import ActivityLogAlertPatchBody
from openapi_server.models.activity_log_alert_resource import ActivityLogAlertResource
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_activity_log_alerts_create_or_update(client):
    """Test case for activity_log_alerts_create_or_update

    
    """
    activity_log_alert = {"properties":{"condition":{"allOf":[{"field":"field","equals":"equals"},{"field":"field","equals":"equals"}]},"description":"description","scopes":["scopes","scopes"],"actions":{"actionGroups":[{"actionGroupId":"actionGroupId","webhookProperties":"{}"},{"actionGroupId":"actionGroupId","webhookProperties":"{}"}]},"enabled":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/activityLogAlerts/{activity_log_alert_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', activity_log_alert_name='activity_log_alert_name_example'),
        headers=headers,
        json=activity_log_alert,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_log_alerts_delete(client):
    """Test case for activity_log_alerts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/activityLogAlerts/{activity_log_alert_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', activity_log_alert_name='activity_log_alert_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_log_alerts_get(client):
    """Test case for activity_log_alerts_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/activityLogAlerts/{activity_log_alert_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', activity_log_alert_name='activity_log_alert_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_log_alerts_list_by_resource_group(client):
    """Test case for activity_log_alerts_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/activityLogAlerts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_log_alerts_list_by_subscription_id(client):
    """Test case for activity_log_alerts_list_by_subscription_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/activityLogAlerts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_log_alerts_update(client):
    """Test case for activity_log_alerts_update

    
    """
    activity_log_alert_patch = {"properties":{"enabled":True},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/activityLogAlerts/{activity_log_alert_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', activity_log_alert_name='activity_log_alert_name_example'),
        headers=headers,
        json=activity_log_alert_patch,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

