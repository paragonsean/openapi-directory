# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.availability_status import AvailabilityStatus
from openapi_server.models.availability_status_list_result import AvailabilityStatusListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_availability_statuses_get_by_resource(client):
    """Test case for availability_statuses_get_by_resource

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/Microsoft.ResourceHealth/availabilityStatuses/current'.format(resource_uri='resource_uri_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_availability_statuses_list(client):
    """Test case for availability_statuses_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/Microsoft.ResourceHealth/availabilityStatuses'.format(resource_uri='resource_uri_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_availability_statuses_list_by_resource_group(client):
    """Test case for availability_statuses_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ResourceHealth/availabilityStatuses'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_availability_statuses_list_by_subscription_id(client):
    """Test case for availability_statuses_list_by_subscription_id

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ResourceHealth/availabilityStatuses'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

