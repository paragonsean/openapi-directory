# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer import Customer
from openapi_server.models.customer_list_result import CustomerListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_customers_get(client):
    """Test case for customers_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/customers/{customer_name}'.format(billing_account_name='billing_account_name_example', customer_name='customer_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_list_by_billing_account_name(client):
    """Test case for customers_list_by_billing_account_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skiptoken', 'skiptoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/customers'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

