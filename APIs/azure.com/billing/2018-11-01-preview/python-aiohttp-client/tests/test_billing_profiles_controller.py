# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_profile import BillingProfile
from openapi_server.models.billing_profile_creation_parameters import BillingProfileCreationParameters
from openapi_server.models.billing_profile_list_result import BillingProfileListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_billing_profiles_create(client):
    """Test case for billing_profiles_create

    
    """
    parameters = {"enableAzureSKUs":[{"skuDescription":"skuDescription","skuId":"skuId"},{"skuDescription":"skuDescription","skuId":"skuId"}],"address":{"country":"country","firstName":"firstName","lastName":"lastName","city":"city","companyName":"companyName","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","region":"region"},"invoiceEmailOptIn":True,"displayName":"displayName","poNumber":"poNumber"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles'.format(billing_account_name='billing_account_name_example'),
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

async def test_billing_profiles_list_by_billing_account_name(client):
    """Test case for billing_profiles_list_by_billing_account_name

    
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
    parameters = {"properties":{"address":{"country":"country","firstName":"firstName","lastName":"lastName","city":"city","companyName":"companyName","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","region":"region"},"invoiceEmailOptIn":True,"displayName":"displayName","currency":"currency","isClassic":True,"invoiceDay":0,"enabledAzureSKUs":[{"skuDescription":"skuDescription","skuId":"skuId"},{"skuDescription":"skuDescription","skuId":"skuId"}],"poNumber":"poNumber","invoiceSections":[{"properties":{"billingProfiles":[null,null],"displayName":"displayName"}},{"properties":{"billingProfiles":[null,null],"displayName":"displayName"}}]}}
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

