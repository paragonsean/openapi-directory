# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.approval import Approval
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.lockbox_request_response import LockboxRequestResponse
from openapi_server.models.request_list_result import RequestListResult


pytestmark = pytest.mark.asyncio

async def test_requests_get(client):
    """Test case for requests_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CustomerLockbox/requests/{request_id}'.format(request_id='request_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_requests_list(client):
    """Test case for requests_list

    
    """
    params = [('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CustomerLockbox/requests'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_requests_update_status(client):
    """Test case for requests_update_status

    
    """
    approval = {"reason":"reason","decision":"Approve"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CustomerLockbox/requests/{request_id}/UpdateApproval'.format(subscription_id='subscription_id_example', request_id='request_id_example'),
        headers=headers,
        json=approval,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

