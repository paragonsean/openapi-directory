# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_period import BillingPeriod
from openapi_server.models.billing_periods_list_result import BillingPeriodsListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_billing_periods_get(client):
    """Test case for billing_periods_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Billing/billingPeriods/{billing_period_name}'.format(subscription_id='subscription_id_example', billing_period_name='billing_period_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_periods_list(client):
    """Test case for billing_periods_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Billing/billingPeriods'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

