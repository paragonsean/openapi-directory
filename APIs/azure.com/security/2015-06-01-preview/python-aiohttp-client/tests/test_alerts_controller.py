# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert import Alert
from openapi_server.models.alert_list import AlertList
from openapi_server.models.cloud_error import CloudError


pytestmark = pytest.mark.asyncio

async def test_alerts_get_resource_group_level_alerts(client):
    """Test case for alerts_get_resource_group_level_alerts

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/locations/{asc_location}/alerts/{alert_name}'.format(subscription_id='subscription_id_example', asc_location='asc_location_example', alert_name='alert_name_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_get_subscription_level_alert(client):
    """Test case for alerts_get_subscription_level_alert

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/locations/{asc_location}/alerts/{alert_name}'.format(subscription_id='subscription_id_example', asc_location='asc_location_example', alert_name='alert_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_list(client):
    """Test case for alerts_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/alerts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_list_by_resource_group(client):
    """Test case for alerts_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/alerts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_list_resource_group_level_alerts_by_region(client):
    """Test case for alerts_list_resource_group_level_alerts_by_region

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/locations/{asc_location}/alerts'.format(subscription_id='subscription_id_example', asc_location='asc_location_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_list_subscription_level_alerts_by_region(client):
    """Test case for alerts_list_subscription_level_alerts_by_region

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/locations/{asc_location}/alerts'.format(subscription_id='subscription_id_example', asc_location='asc_location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_update_resource_group_level_alert_state(client):
    """Test case for alerts_update_resource_group_level_alert_state

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/locations/{asc_location}/alerts/{alert_name}/{alert_update_action_type}'.format(subscription_id='subscription_id_example', asc_location='asc_location_example', alert_name='alert_name_example', alert_update_action_type='alert_update_action_type_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_update_subscription_level_alert_state(client):
    """Test case for alerts_update_subscription_level_alert_state

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/locations/{asc_location}/alerts/{alert_name}/{alert_update_action_type}'.format(subscription_id='subscription_id_example', asc_location='asc_location_example', alert_name='alert_name_example', alert_update_action_type='alert_update_action_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

