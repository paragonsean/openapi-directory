# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_parameters import CheckNameAvailabilityParameters
from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server.models.services_name_availability_info import ServicesNameAvailabilityInfo


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
        path='/providers/Microsoft.HealthcareApis/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_check_name_availability(client):
    """Test case for services_check_name_availability

    
    """
    check_name_availability_inputs = {"name":"name","type":"type"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.HealthcareApis/checkNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=check_name_availability_inputs,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

