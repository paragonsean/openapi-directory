# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.transaction import Transaction
from openapi_server.models.transaction_list_result import TransactionListResult


pytestmark = pytest.mark.asyncio

async def test_transactions_get(client):
    """Test case for transactions_get

    
    """
    params = [('periodStartDate', 'period_start_date_example'),
                    ('periodEndDate', 'period_end_date_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/transactions/{transaction_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', transaction_name='transaction_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_list_by_billing_account(client):
    """Test case for transactions_list_by_billing_account

    
    """
    params = [('api-version', 'api_version_example'),
                    ('periodStartDate', 'period_start_date_example'),
                    ('periodEndDate', 'period_end_date_example'),
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

async def test_transactions_list_by_billing_profile(client):
    """Test case for transactions_list_by_billing_profile

    
    """
    params = [('api-version', 'api_version_example'),
                    ('periodStartDate', 'period_start_date_example'),
                    ('periodEndDate', 'period_end_date_example'),
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

async def test_transactions_list_by_customer(client):
    """Test case for transactions_list_by_customer

    
    """
    params = [('api-version', 'api_version_example'),
                    ('periodStartDate', 'period_start_date_example'),
                    ('periodEndDate', 'period_end_date_example'),
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

async def test_transactions_list_by_invoice_section(client):
    """Test case for transactions_list_by_invoice_section

    
    """
    params = [('api-version', 'api_version_example'),
                    ('periodStartDate', 'period_start_date_example'),
                    ('periodEndDate', 'period_end_date_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections/{invoice_section_name}/transactions'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

