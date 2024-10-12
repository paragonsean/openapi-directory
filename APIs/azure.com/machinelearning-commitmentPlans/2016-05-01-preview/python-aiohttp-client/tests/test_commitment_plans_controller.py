# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.commitment_plan import CommitmentPlan
from openapi_server.models.commitment_plan_list_result import CommitmentPlanListResult
from openapi_server.models.commitment_plan_patch_payload import CommitmentPlanPatchPayload
from openapi_server.models.plan_usage_history_list_result import PlanUsageHistoryListResult


pytestmark = pytest.mark.asyncio

async def test_commitment_plans_create_or_update(client):
    """Test case for commitment_plans_create_or_update

    
    """
    create_or_update_payload = {"etag":"etag","sku":{"tier":"tier","name":"name","capacity":7},"properties":{"chargeForOverage":True,"chargeForPlan":True,"includedQuantities":{"key":{"overageMeter":"overageMeter","amount":6.027456183070403,"includedQuantityMeter":"includedQuantityMeter","allowance":0.8008281904610115}},"maxAssociationLimit":1,"creationDate":"2000-01-23T04:56:07.000+00:00","maxCapacityLimit":5,"minCapacityLimit":5,"refillFrequencyInDays":2,"planMeter":"planMeter","suspendPlanOnOverage":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/commitmentPlans/{commitment_plan_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', commitment_plan_name='commitment_plan_name_example'),
        headers=headers,
        json=create_or_update_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commitment_plans_get(client):
    """Test case for commitment_plans_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/commitmentPlans/{commitment_plan_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', commitment_plan_name='commitment_plan_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commitment_plans_list(client):
    """Test case for commitment_plans_list

    
    """
    params = [('$skipToken', 'skip_token_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MachineLearning/commitmentPlans'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commitment_plans_list_in_resource_group(client):
    """Test case for commitment_plans_list_in_resource_group

    
    """
    params = [('$skipToken', 'skip_token_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/commitmentPlans'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commitment_plans_patch(client):
    """Test case for commitment_plans_patch

    
    """
    patch_payload = {"sku":{"tier":"tier","name":"name","capacity":7},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/commitmentPlans/{commitment_plan_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', commitment_plan_name='commitment_plan_name_example'),
        headers=headers,
        json=patch_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commitment_plans_remove(client):
    """Test case for commitment_plans_remove

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/commitmentPlans/{commitment_plan_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', commitment_plan_name='commitment_plan_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_usage_history_list(client):
    """Test case for usage_history_list

    
    """
    params = [('$skipToken', 'skip_token_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/commitmentPlans/{commitment_plan_name}/usageHistory'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', commitment_plan_name='commitment_plan_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

