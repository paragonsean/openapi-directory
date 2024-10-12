# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_account import BillingAccount
from openapi_server.models.billing_account_list_result import BillingAccountListResult
from openapi_server.models.billing_account_update_properties import BillingAccountUpdateProperties
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_billing_accounts_get(client):
    """Test case for billing_accounts_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_accounts_list(client):
    """Test case for billing_accounts_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_accounts_update(client):
    """Test case for billing_accounts_update

    
    """
    parameters = {"properties":{"country":"country","address":{"country":"country","firstName":"firstName","lastName":"lastName","city":"city","companyName":"companyName","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","region":"region"},"billingProfiles":[{"properties":{"address":{"country":"country","firstName":"firstName","lastName":"lastName","city":"city","companyName":"companyName","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","region":"region"},"invoiceEmailOptIn":True,"displayName":"displayName","currency":"currency","isClassic":True,"invoiceDay":0,"enabledAzureSKUs":[{"skuDescription":"skuDescription","skuId":"skuId"},{"skuDescription":"skuDescription","skuId":"skuId"}],"poNumber":"poNumber","invoiceSections":[{"properties":{"billingProfiles":[null,null],"displayName":"displayName"}},{"properties":{"billingProfiles":[null,null],"displayName":"displayName"}}]}},{"properties":{"address":{"country":"country","firstName":"firstName","lastName":"lastName","city":"city","companyName":"companyName","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","region":"region"},"invoiceEmailOptIn":True,"displayName":"displayName","currency":"currency","isClassic":True,"invoiceDay":0,"enabledAzureSKUs":[{"skuDescription":"skuDescription","skuId":"skuId"},{"skuDescription":"skuDescription","skuId":"skuId"}],"poNumber":"poNumber","invoiceSections":[{"properties":{"billingProfiles":[null,null],"displayName":"displayName"}},{"properties":{"billingProfiles":[null,null],"displayName":"displayName"}}]}}],"displayName":"displayName","accountType":"Organization","enrollmentAccounts":[{"properties":{"accountName":"accountName","endDate":"2000-01-23T04:56:07.000+00:00","costCenter":"costCenter","accountOwner":"accountOwner","startDate":"2000-01-23T04:56:07.000+00:00","status":"status"}},{"properties":{"accountName":"accountName","endDate":"2000-01-23T04:56:07.000+00:00","costCenter":"costCenter","accountOwner":"accountOwner","startDate":"2000-01-23T04:56:07.000+00:00","status":"status"}}],"company":"company","departments":[{"properties":{"departmentName":"departmentName","costCenter":"costCenter","enrollmentAccounts":[{"properties":{"accountName":"accountName","endDate":"2000-01-23T04:56:07.000+00:00","costCenter":"costCenter","accountOwner":"accountOwner","startDate":"2000-01-23T04:56:07.000+00:00","status":"status"}},{"properties":{"accountName":"accountName","endDate":"2000-01-23T04:56:07.000+00:00","costCenter":"costCenter","accountOwner":"accountOwner","startDate":"2000-01-23T04:56:07.000+00:00","status":"status"}}],"status":"status"}},{"properties":{"departmentName":"departmentName","costCenter":"costCenter","enrollmentAccounts":[{"properties":{"accountName":"accountName","endDate":"2000-01-23T04:56:07.000+00:00","costCenter":"costCenter","accountOwner":"accountOwner","startDate":"2000-01-23T04:56:07.000+00:00","status":"status"}},{"properties":{"accountName":"accountName","endDate":"2000-01-23T04:56:07.000+00:00","costCenter":"costCenter","accountOwner":"accountOwner","startDate":"2000-01-23T04:56:07.000+00:00","status":"status"}}],"status":"status"}}],"enrollmentDetails":{"endDate":"2000-01-23T04:56:07.000+00:00","billingCycle":"billingCycle","countryCode":"countryCode","channel":"channel","policies":{"reservedInstancesEnabled":True,"accountOwnerViewCharges":True,"marketplacesEnabled":True,"departmentAdminViewCharges":True},"currency":"currency","language":"language","startDate":"2000-01-23T04:56:07.000+00:00","status":"status"},"hasReadAccess":True,"invoiceSections":[{"properties":{"billingProfiles":[null,null],"displayName":"displayName"}},{"properties":{"billingProfiles":[null,null],"displayName":"displayName"}}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

