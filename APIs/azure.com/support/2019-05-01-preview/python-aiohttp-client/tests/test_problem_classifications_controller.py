# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_response import ExceptionResponse
from openapi_server.models.problem_classification import ProblemClassification
from openapi_server.models.problem_classifications_list_result import ProblemClassificationsListResult


pytestmark = pytest.mark.asyncio

async def test_problem_classifications_get(client):
    """Test case for problem_classifications_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Support/services/{service_name}/problemClassifications/{problem_classification_name}'.format(service_name='service_name_example', problem_classification_name='problem_classification_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_problem_classifications_list(client):
    """Test case for problem_classifications_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Support/services/{service_name}/problemClassifications'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

