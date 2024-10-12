# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.charge_summary import ChargeSummary
from openapi_server.models.charges_list_result import ChargesListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_charges_list_by_department(client):
    """Test case for charges_list_by_department

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/departments/{department_id}/providers/Microsoft.Consumption/charges'.format(billing_account_id='billing_account_id_example', department_id='department_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_charges_list_by_enrollment_account(client):
    """Test case for charges_list_by_enrollment_account

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/enrollmentAccounts/{enrollment_account_id}/providers/Microsoft.Consumption/charges'.format(billing_account_id='billing_account_id_example', enrollment_account_id='enrollment_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_charges_list_for_billing_period_by_department(client):
    """Test case for charges_list_for_billing_period_by_department

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/departments/{department_id}/providers/Microsoft.Billing/billingPeriods/{billing_period_name}/providers/Microsoft.Consumption/charges'.format(billing_account_id='billing_account_id_example', department_id='department_id_example', billing_period_name='billing_period_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_charges_list_for_billing_period_by_enrollment_account(client):
    """Test case for charges_list_for_billing_period_by_enrollment_account

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/enrollmentAccounts/{enrollment_account_id}/providers/Microsoft.Billing/billingPeriods/{billing_period_name}/providers/Microsoft.Consumption/charges'.format(billing_account_id='billing_account_id_example', enrollment_account_id='enrollment_account_id_example', billing_period_name='billing_period_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

