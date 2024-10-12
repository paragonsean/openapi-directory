# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.subscription_plan_request import SubscriptionPlanRequest
from openapi_server.models.subscription_plan_response import SubscriptionPlanResponse


pytestmark = pytest.mark.asyncio

async def test_internal_request_subscription_plan(client):
    """Test case for internal_request_subscription_plan

    Request subscription plan
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/internal/tenant/subscription_plan',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_internal_set_subscription_plan(client):
    """Test case for internal_set_subscription_plan

    Set subscription plan
    """
    body = {"subscriptionPlanId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/internal/tenant/subscription_plan',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

