# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance import Balance
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_balances_get_by_billing_account(client):
    """Test case for balances_get_by_billing_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.Consumption/balances'.format(billing_account_id='billing_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_balances_get_for_billing_period_by_billing_account(client):
    """Test case for balances_get_for_billing_period_by_billing_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.Billing/billingPeriods/{billing_period_name}/providers/Microsoft.Consumption/balances'.format(billing_account_id='billing_account_id_example', billing_period_name='billing_period_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

