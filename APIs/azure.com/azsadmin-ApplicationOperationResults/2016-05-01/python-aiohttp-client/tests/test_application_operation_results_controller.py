# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_operation_result import ApplicationOperationResult
from openapi_server.models.application_operation_result_list import ApplicationOperationResultList


pytestmark = pytest.mark.asyncio

async def test_application_operation_results_get(client):
    """Test case for application_operation_results_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/applicationOperationResults/{operation}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', operation='operation_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_operation_results_list(client):
    """Test case for application_operation_results_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/applicationOperationResults'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

