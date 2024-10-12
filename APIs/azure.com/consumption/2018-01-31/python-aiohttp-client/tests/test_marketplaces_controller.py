# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.marketplaces_list_result import MarketplacesListResult


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list(client):
    """Test case for marketplaces_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Consumption/marketplaces'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketplaces_list_by_billing_period(client):
    """Test case for marketplaces_list_by_billing_period

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Billing/billingPeriods/{billing_period_name}/providers/Microsoft.Consumption/marketplaces'.format(subscription_id='subscription_id_example', billing_period_name='billing_period_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

