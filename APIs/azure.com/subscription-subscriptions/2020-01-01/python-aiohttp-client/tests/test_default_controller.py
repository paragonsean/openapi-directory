# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.canceled_subscription_id import CanceledSubscriptionId
from openapi_server.models.enabled_subscription_id import EnabledSubscriptionId
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.modern_csp_subscription_creation_parameters import ModernCspSubscriptionCreationParameters
from openapi_server.models.modern_subscription_creation_parameters import ModernSubscriptionCreationParameters
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server.models.renamed_subscription_id import RenamedSubscriptionId
from openapi_server.models.subscription_creation_parameters import SubscriptionCreationParameters
from openapi_server.models.subscription_creation_result import SubscriptionCreationResult
from openapi_server.models.subscription_name import SubscriptionName


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Subscription/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_cancel(client):
    """Test case for subscription_cancel

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscription/cancel'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_create_csp_subscription(client):
    """Test case for subscription_create_csp_subscription

    
    """
    body = {"resellerId":"resellerId","displayName":"displayName","skuId":"skuId"}
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

async def test_subscription_create_subscription(client):
    """Test case for subscription_create_subscription

    
    """
    body = {"managementGroupId":"managementGroupId","owner":{"objectId":"objectId"},"costCenter":"costCenter","displayName":"displayName","skuId":"skuId"}
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

async def test_subscription_create_subscription_in_enrollment_account(client):
    """Test case for subscription_create_subscription_in_enrollment_account

    
    """
    body = {"managementGroupId":"managementGroupId","offerType":"MS-AZR-0017P","displayName":"displayName","owners":[{"objectId":"objectId"},{"objectId":"objectId"}]}
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

async def test_subscription_enable(client):
    """Test case for subscription_enable

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscription/enable'.format(subscription_id='subscription_id_example'),
        headers=headers,
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


pytestmark = pytest.mark.asyncio

async def test_subscription_rename(client):
    """Test case for subscription_rename

    
    """
    body = {"subscriptionName":"subscriptionName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscription/rename'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

