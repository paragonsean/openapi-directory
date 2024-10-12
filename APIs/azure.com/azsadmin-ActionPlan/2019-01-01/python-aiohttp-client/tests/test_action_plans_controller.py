# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_plan_list import ActionPlanList
from openapi_server.models.action_plan_resource_entity import ActionPlanResourceEntity


pytestmark = pytest.mark.asyncio

async def test_action_plans_get(client):
    """Test case for action_plans_get

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/actionPlans/{plan_id}'.format(subscription_id='subscription_id_example', plan_id='plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_plans_list(client):
    """Test case for action_plans_list

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/actionPlans'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

