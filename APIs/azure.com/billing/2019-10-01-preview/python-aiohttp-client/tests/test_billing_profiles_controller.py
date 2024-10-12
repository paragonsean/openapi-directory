# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_profile import BillingProfile
from openapi_server.models.billing_profile_creation_request import BillingProfileCreationRequest
from openapi_server.models.billing_profile_list_result import BillingProfileListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_billing_profiles_create(client):
    """Test case for billing_profiles_create

    
    """
    parameters = {"address":{"country":"country","firstName":"firstName","lastName":"lastName","city":"city","companyName":"companyName","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","region":"region"},"invoiceEmailOptIn":True,"displayName":"displayName","enabledAzurePlans":[{"skuDescription":"skuDescription","skuId":"skuId"},{"skuDescription":"skuDescription","skuId":"skuId"}],"poNumber":"poNumber"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_profiles_get(client):
    """Test case for billing_profiles_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_profiles_list_by_billing_account(client):
    """Test case for billing_profiles_list_by_billing_account

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_profiles_update(client):
    """Test case for billing_profiles_update

    
    """
    parameters = {"properties":{"address":{"country":"country","firstName":"firstName","lastName":"lastName","city":"city","companyName":"companyName","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","region":"region"},"invoiceEmailOptIn":True,"displayName":"displayName","enabledAzurePlans":[{"skuDescription":"skuDescription","skuId":"skuId"},{"skuDescription":"skuDescription","skuId":"skuId"}],"currency":"currency","invoiceDay":0,"poNumber":"poNumber","invoiceSections":[{"properties":{"displayName":"displayName"}},{"properties":{"displayName":"displayName"}}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

