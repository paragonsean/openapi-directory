# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.line_of_credit import LineOfCredit


pytestmark = pytest.mark.asyncio

async def test_line_of_credits_get(client):
    """Test case for line_of_credits_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Billing/billingAccounts/default/lineOfCredit/default'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_of_credits_update(client):
    """Test case for line_of_credits_update

    
    """
    parameters = {"properties":{"reason":"reason","creditLimit":{"currency":"currency","value":0.8008281904610115},"remainingBalance":{"currency":"currency","value":0.8008281904610115},"status":"Approved"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Billing/billingAccounts/default/lineOfCredit/default'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

