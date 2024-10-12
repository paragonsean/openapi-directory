# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.io_t_spaces_name_availability_info import IoTSpacesNameAvailabilityInfo
from openapi_server.models.operation_inputs import OperationInputs
from openapi_server.models.operation_list_result import OperationListResult


pytestmark = pytest.mark.asyncio

async def test_io_t_spaces_check_name_availability(client):
    """Test case for io_t_spaces_check_name_availability

    
    """
    operation_inputs = {"name":"name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.IoTSpaces/checkNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=operation_inputs,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.IoTSpaces/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

