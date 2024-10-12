# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.events import Events


pytestmark = pytest.mark.asyncio

async def test_events_list_by_single_resource(client):
    """Test case for events_list_by_single_resource

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/Microsoft.ResourceHealth/events'.format(resource_uri='resource_uri_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_list_by_subscription_id(client):
    """Test case for events_list_by_subscription_id

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ResourceHealth/events'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

