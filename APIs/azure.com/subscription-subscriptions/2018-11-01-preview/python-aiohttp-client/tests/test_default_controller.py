# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.modern_csp_subscription_creation_parameters import ModernCspSubscriptionCreationParameters
from openapi_server.models.modern_subscription_creation_parameters import ModernSubscriptionCreationParameters
from openapi_server.models.subscription_creation_result import SubscriptionCreationResult


pytestmark = pytest.mark.asyncio

async def test_subscription_factory_create_csp_subscription(client):
    """Test case for subscription_factory_create_csp_subscription

    
    """
    body = {"resellerId":"resellerId","serviceProviderId":"serviceProviderId","displayName":"displayName","skuId":"skuId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/customers/{customer_name}/providers/Microsoft.Subscription/createSubscription'.format(billing_account_name='billing_account_name_example', customer_name='customer_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_factory_create_subscription(client):
    """Test case for subscription_factory_create_subscription

    
    """
    body = {"managementGroupId":"managementGroupId","owner":{"objectId":"objectId"},"costCenter":"costCenter","displayName":"displayName","billingProfileId":"billingProfileId","additionalParameters":{"key":"{}"},"skuId":"skuId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections/{invoice_section_name}/providers/Microsoft.Subscription/createSubscription'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_operation_get(client):
    """Test case for subscription_operation_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Subscription/subscriptionOperations/{operation_id}'.format(operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

