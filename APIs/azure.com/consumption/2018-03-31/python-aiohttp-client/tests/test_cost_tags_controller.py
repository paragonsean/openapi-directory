# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cost_tags import CostTags
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_cost_tags_create_or_update(client):
    """Test case for cost_tags_create_or_update

    
    """
    parameters = {"properties":{"costTags":[{"key":"key"},{"key":"key"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.Consumption/costTags'.format(billing_account_id='billing_account_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cost_tags_get(client):
    """Test case for cost_tags_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.Consumption/costTags'.format(billing_account_id='billing_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

