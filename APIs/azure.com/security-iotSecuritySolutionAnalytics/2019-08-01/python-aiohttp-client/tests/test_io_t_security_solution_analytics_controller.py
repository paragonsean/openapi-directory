# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.io_t_security_solution_analytics_model import IoTSecuritySolutionAnalyticsModel
from openapi_server.models.io_t_security_solution_analytics_model_list import IoTSecuritySolutionAnalyticsModelList
from openapi_server.models.iot_security_solution_analytics_list_default_response import IotSecuritySolutionAnalyticsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_iot_security_solution_analytics_get(client):
    """Test case for iot_security_solution_analytics_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/iotSecuritySolutions/{solution_name}/analyticsModels/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', solution_name='solution_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_security_solution_analytics_list(client):
    """Test case for iot_security_solution_analytics_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/iotSecuritySolutions/{solution_name}/analyticsModels'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', solution_name='solution_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

