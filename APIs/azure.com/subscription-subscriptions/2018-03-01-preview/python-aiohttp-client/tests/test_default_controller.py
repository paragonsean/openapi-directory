# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.subscription_creation_parameters import SubscriptionCreationParameters
from openapi_server.models.subscription_creation_result import SubscriptionCreationResult
from openapi_server.models.subscription_operation_list_result import SubscriptionOperationListResult


pytestmark = pytest.mark.asyncio

async def test_subscription_factory_create_subscription_in_enrollment_account(client):
    """Test case for subscription_factory_create_subscription_in_enrollment_account

    
    """
    body = {"offerType":"MS-AZR-0017P","displayName":"displayName","additionalParameters":{"key":"{}"},"owners":[{"objectId":"objectId"},{"objectId":"objectId"}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/enrollmentAccounts/{enrollment_account_name}/providers/Microsoft.Subscription/createSubscription'.format(enrollment_account_name='enrollment_account_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_operations_list(client):
    """Test case for subscription_operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Subscription/subscriptionOperations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

