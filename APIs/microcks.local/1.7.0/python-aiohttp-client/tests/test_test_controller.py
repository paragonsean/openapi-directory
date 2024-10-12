# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.counter import Counter
from openapi_server.models.request_response_pair import RequestResponsePair
from openapi_server.models.test_case_result import TestCaseResult
from openapi_server.models.test_case_return_dto import TestCaseReturnDTO
from openapi_server.models.test_request import TestRequest
from openapi_server.models.test_result import TestResult
from openapi_server.models.unidirectional_event import UnidirectionalEvent


pytestmark = pytest.mark.asyncio

async def test_create_test(client):
    """Test case for create_test

    Create a new Test
    """
    body = {"secretName":"secretName","filteredOperations":["filteredOperations","filteredOperations"],"operationHeaders":{"key":[{"values":"values","name":"name"},{"values":"values","name":"name"}]},"runnerType":"HTTP","serviceId":"serviceId","testEndpoint":"testEndpoint","timeout":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/tests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events_by_test_case(client):
    """Test case for get_events_by_test_case

    Get events for TestCase
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tests/{id}/events/{test_case_id}'.format(id='id_example', test_case_id='test_case_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_messages_by_test_case(client):
    """Test case for get_messages_by_test_case

    Get messages for TestCase
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tests/{id}/messages/{test_case_id}'.format(id='id_example', test_case_id='test_case_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_test_result(client):
    """Test case for get_test_result

    Get TestResult
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tests/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_test_results_by_service(client):
    """Test case for get_test_results_by_service

    Get TestResults by Service
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tests/service/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_test_results_by_service_counter(client):
    """Test case for get_test_results_by_service_counter

    Get the TestResults for Service counter
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tests/service/{service_id}/count'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_report_test_case_result(client):
    """Test case for report_test_case_result

    Report and create a new TestCaseResult
    """
    body = {"operationName":"operationName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/tests/{id}/testCaseResult'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

