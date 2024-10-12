# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.management_group_aggregated_cost_result import ManagementGroupAggregatedCostResult


pytestmark = pytest.mark.asyncio

async def test_aggregated_cost_get_by_management_group(client):
    """Test case for aggregated_cost_get_by_management_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{management_group_id}/providers/Microsoft.Consumption/aggregatedcost'.format(management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aggregated_cost_get_for_billing_period_by_management_group(client):
    """Test case for aggregated_cost_get_for_billing_period_by_management_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{management_group_id}/providers/Microsoft.Billing/billingPeriods/{billing_period_name}/Microsoft.Consumption/aggregatedcost'.format(management_group_id='management_group_id_example', billing_period_name='billing_period_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

