# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.available_balance import AvailableBalance
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_available_balances_get_by_billing_profile(client):
    """Test case for available_balances_get_by_billing_profile

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/availableBalance/default'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

