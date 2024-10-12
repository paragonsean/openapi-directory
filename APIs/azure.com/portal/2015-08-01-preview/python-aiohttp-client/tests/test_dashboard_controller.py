# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dashboard import Dashboard
from openapi_server.models.dashboard_list_result import DashboardListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patchable_dashboard import PatchableDashboard


pytestmark = pytest.mark.asyncio

async def test_dashboards_create_or_update(client):
    """Test case for dashboards_create_or_update

    
    """
    dashboard = {"name":"name","location":"location","id":"id","type":"type","properties":{"lenses":{"key":{"metadata":{"key":"{}"},"parts":{"key":{"metadata":{"key":"{}"},"position":{"rowSpan":1.4658129805029452,"metadata":{"key":"{}"},"colSpan":6.027456183070403,"x":5.962133916683182,"y":5.637376656633329}}},"order":0}},"metadata":{"key":"{}"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Portal/dashboards/{dashboard_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dashboard_name='dashboard_name_example'),
        headers=headers,
        json=dashboard,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboards_delete(client):
    """Test case for dashboards_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Portal/dashboards/{dashboard_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dashboard_name='dashboard_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboards_get(client):
    """Test case for dashboards_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Portal/dashboards/{dashboard_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dashboard_name='dashboard_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboards_list_by_resource_group(client):
    """Test case for dashboards_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Portal/dashboards'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboards_list_by_subscription(client):
    """Test case for dashboards_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Portal/dashboards'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dashboards_update(client):
    """Test case for dashboards_update

    
    """
    dashboard = {"properties":{"lenses":{"key":{"metadata":{"key":"{}"},"parts":{"key":{"metadata":{"key":"{}"},"position":{"rowSpan":1.4658129805029452,"metadata":{"key":"{}"},"colSpan":6.027456183070403,"x":5.962133916683182,"y":5.637376656633329}}},"order":0}},"metadata":{"key":"{}"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Portal/dashboards/{dashboard_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dashboard_name='dashboard_name_example'),
        headers=headers,
        json=dashboard,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

