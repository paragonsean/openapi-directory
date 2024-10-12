# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.availability_status import AvailabilityStatus
from openapi_server.models.availability_status_list_result import AvailabilityStatusListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_child_availability_statuses_get_by_resource(client):
    """Test case for child_availability_statuses_get_by_resource

    
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
        path='/{resource_uri}/providers/Microsoft.ResourceHealth/childAvailabilityStatuses/current'.format(resource_uri='resource_uri_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_child_availability_statuses_list(client):
    """Test case for child_availability_statuses_list

    
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
        path='/{resource_uri}/providers/Microsoft.ResourceHealth/childAvailabilityStatuses'.format(resource_uri='resource_uri_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

