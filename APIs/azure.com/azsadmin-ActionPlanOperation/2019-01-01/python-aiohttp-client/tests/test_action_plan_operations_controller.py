# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_plan_operation_resource_entity import ActionPlanOperationResourceEntity
from openapi_server.models.action_plan_operations_list import ActionPlanOperationsList


pytestmark = pytest.mark.asyncio

async def test_action_plan_operations_get(client):
    """Test case for action_plan_operations_get

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/actionPlans/{plan_id}/operations/{operation_id}'.format(subscription_id='subscription_id_example', plan_id='plan_id_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_action_plan_operations_list(client):
    """Test case for action_plan_operations_list

    
    """
    params = [('api-version', '2019-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Deployment.Admin/locations/global/actionPlans/{plan_id}/operations'.format(subscription_id='subscription_id_example', plan_id='plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

