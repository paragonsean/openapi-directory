# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.plan_acquisition import PlanAcquisition
from openapi_server.models.plan_acquisition_list import PlanAcquisitionList


pytestmark = pytest.mark.asyncio

async def test_acquired_plans_create(client):
    """Test case for acquired_plans_create

    
    """
    new_acquired_plan = {"externalReferenceId":"externalReferenceId","acquisitionId":"acquisitionId","planId":"planId","acquisitionTime":"2000-01-23T04:56:07.000+00:00","id":"id","provisioningState":"NotSpecified"}
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/subscriptions/{target_subscription_id}/acquiredPlans/{plan_acquisition_id}'.format(subscription_id='subscription_id_example', target_subscription_id='target_subscription_id_example', plan_acquisition_id='plan_acquisition_id_example'),
        headers=headers,
        json=new_acquired_plan,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_acquired_plans_delete(client):
    """Test case for acquired_plans_delete

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/subscriptions/{target_subscription_id}/acquiredPlans/{plan_acquisition_id}'.format(subscription_id='subscription_id_example', target_subscription_id='target_subscription_id_example', plan_acquisition_id='plan_acquisition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_acquired_plans_get(client):
    """Test case for acquired_plans_get

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/subscriptions/{target_subscription_id}/acquiredPlans/{plan_acquisition_id}'.format(subscription_id='subscription_id_example', target_subscription_id='target_subscription_id_example', plan_acquisition_id='plan_acquisition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_acquired_plans_list(client):
    """Test case for acquired_plans_list

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/subscriptions/{target_subscription_id}/acquiredPlans'.format(subscription_id='subscription_id_example', target_subscription_id='target_subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

