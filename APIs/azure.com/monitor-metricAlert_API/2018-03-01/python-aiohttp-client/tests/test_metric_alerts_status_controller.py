# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.metric_alert_status_collection import MetricAlertStatusCollection
from openapi_server.models.metric_alerts_list_by_subscription_default_response import MetricAlertsListBySubscriptionDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_metric_alerts_status_list(client):
    """Test case for metric_alerts_status_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/metricAlerts/{rule_name}/status'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', rule_name='rule_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metric_alerts_status_list_by_name(client):
    """Test case for metric_alerts_status_list_by_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/metricAlerts/{rule_name}/status/{status_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', rule_name='rule_name_example', status_name='status_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

