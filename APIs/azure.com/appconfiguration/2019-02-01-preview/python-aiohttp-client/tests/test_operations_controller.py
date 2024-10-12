# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_parameters import CheckNameAvailabilityParameters
from openapi_server.models.error import Error
from openapi_server.models.name_availability_status import NameAvailabilityStatus
from openapi_server.models.operation_definition_list_result import OperationDefinitionListResult


pytestmark = pytest.mark.asyncio

async def test_operations_check_name_availability(client):
    """Test case for operations_check_name_availability

    
    """
    check_name_availability_parameters = {"name":"name","type":"Microsoft.AppConfiguration/configurationStores"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.AppConfiguration/checkNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=check_name_availability_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.AppConfiguration/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

