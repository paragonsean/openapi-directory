# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.plan import Plan
from openapi_server.models.plan_list import PlanList
from openapi_server.models.plans_list_metric_definitions200_response import PlansListMetricDefinitions200Response
from openapi_server.models.plans_list_metrics200_response import PlansListMetrics200Response


pytestmark = pytest.mark.asyncio

async def test_plans_create_or_update(client):
    """Test case for plans_create_or_update

    
    """
    new_plan = {"properties":{"externalReferenceId":"externalReferenceId","displayName":"displayName","quotaIds":["quotaIds","quotaIds"],"name":"name","subscriptionCount":0,"description":"description","skuIds":["skuIds","skuIds"]}}
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/plans/{plan}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', plan='plan_example'),
        headers=headers,
        json=new_plan,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_plans_delete(client):
    """Test case for plans_delete

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/plans/{plan}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', plan='plan_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_plans_get(client):
    """Test case for plans_get

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/plans/{plan}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', plan='plan_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_plans_list(client):
    """Test case for plans_list

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/plans'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_plans_list_all(client):
    """Test case for plans_list_all

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/plans'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_plans_list_metric_definitions(client):
    """Test case for plans_list_metric_definitions

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/plans/{plan}/metricDefinitions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', plan='plan_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_plans_list_metrics(client):
    """Test case for plans_list_metrics

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/plans/{plan}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', plan='plan_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

