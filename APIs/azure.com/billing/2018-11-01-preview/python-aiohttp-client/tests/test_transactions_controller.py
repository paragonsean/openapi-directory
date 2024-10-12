# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.transactions_list_result import TransactionsListResult


pytestmark = pytest.mark.asyncio

async def test_transactions_list_by_billing_account_name(client):
    """Test case for transactions_list_by_billing_account_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/transactions'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_list_by_billing_profile_name(client):
    """Test case for transactions_list_by_billing_profile_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/transactions'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_list_by_customer_name(client):
    """Test case for transactions_list_by_customer_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/customers/{customer_name}/transactions'.format(billing_account_name='billing_account_name_example', customer_name='customer_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_list_by_invoice_section_name(client):
    """Test case for transactions_list_by_invoice_section_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/transactions'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

