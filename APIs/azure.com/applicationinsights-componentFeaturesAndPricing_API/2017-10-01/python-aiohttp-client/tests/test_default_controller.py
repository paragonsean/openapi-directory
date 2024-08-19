# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_insights_component_pricing_plan import ApplicationInsightsComponentPricingPlan


pytestmark = pytest.mark.asyncio

async def test_component_current_pricing_plan_create_and_update(client):
    """Test case for component_current_pricing_plan_create_and_update

    
    """
    pricing_plan_properties = {"properties":{"cap":0.8008281904610115,"planType":"planType","stopSendNotificationWhenHitThreshold":True,"stopSendNotificationWhenHitCap":True,"resetHour":1,"maxHistoryCap":6.027456183070403,"warningThreshold":5}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/components/{resource_name}/pricingPlans/current'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example'),
        headers=headers,
        json=pricing_plan_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_component_current_pricing_plan_get(client):
    """Test case for component_current_pricing_plan_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/components/{resource_name}/pricingPlans/current'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_component_current_pricing_plan_update(client):
    """Test case for component_current_pricing_plan_update

    
    """
    pricing_plan_properties = {"properties":{"cap":0.8008281904610115,"planType":"planType","stopSendNotificationWhenHitThreshold":True,"stopSendNotificationWhenHitCap":True,"resetHour":1,"maxHistoryCap":6.027456183070403,"warningThreshold":5}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/components/{resource_name}/pricingPlans/current'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example'),
        headers=headers,
        json=pricing_plan_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

