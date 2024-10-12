# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tenant_list_result import TenantListResult


pytestmark = pytest.mark.asyncio

async def test_tenants_get(client):
    """Test case for tenants_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/billingProfiles/{billing_profile_id}/providers/Microsoft.Consumption/tenants'.format(billing_account_id='billing_account_id_example', billing_profile_id='billing_profile_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

