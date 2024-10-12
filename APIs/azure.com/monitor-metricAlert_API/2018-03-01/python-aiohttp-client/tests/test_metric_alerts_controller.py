# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.metric_alert_resource import MetricAlertResource
from openapi_server.models.metric_alert_resource_collection import MetricAlertResourceCollection
from openapi_server.models.metric_alert_resource_patch import MetricAlertResourcePatch
from openapi_server.models.metric_alerts_list_by_subscription_default_response import MetricAlertsListBySubscriptionDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_metric_alerts_create_or_update(client):
    """Test case for metric_alerts_create_or_update

    
    """
    parameters = {"properties":{"autoMitigate":True,"severity":0,"windowSize":"windowSize","criteria":{"odata.type":"Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria"},"evaluationFrequency":"evaluationFrequency","description":"description","lastUpdatedTime":"2000-01-23T04:56:07.000+00:00","scopes":["scopes","scopes"],"targetResourceRegion":"targetResourceRegion","actions":[{"actionGroupId":"actionGroupId","webhookProperties":{"key":"webhookProperties"}},{"actionGroupId":"actionGroupId","webhookProperties":{"key":"webhookProperties"}}],"enabled":True,"targetResourceType":"targetResourceType"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/metricAlerts/{rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', rule_name='rule_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metric_alerts_delete(client):
    """Test case for metric_alerts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/metricAlerts/{rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', rule_name='rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metric_alerts_get(client):
    """Test case for metric_alerts_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/metricAlerts/{rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', rule_name='rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metric_alerts_list_by_resource_group(client):
    """Test case for metric_alerts_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/metricAlerts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metric_alerts_list_by_subscription(client):
    """Test case for metric_alerts_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Insights/metricAlerts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metric_alerts_update(client):
    """Test case for metric_alerts_update

    
    """
    parameters = {"properties":{"autoMitigate":True,"severity":0,"windowSize":"windowSize","criteria":{"odata.type":"Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria"},"evaluationFrequency":"evaluationFrequency","description":"description","lastUpdatedTime":"2000-01-23T04:56:07.000+00:00","scopes":["scopes","scopes"],"targetResourceRegion":"targetResourceRegion","actions":[{"actionGroupId":"actionGroupId","webhookProperties":{"key":"webhookProperties"}},{"actionGroupId":"actionGroupId","webhookProperties":{"key":"webhookProperties"}}],"enabled":True,"targetResourceType":"targetResourceType"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/metricAlerts/{rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', rule_name='rule_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

