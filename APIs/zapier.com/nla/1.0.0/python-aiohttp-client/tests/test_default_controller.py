# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.execute_request import ExecuteRequest
from openapi_server.models.execute_response import ExecuteResponse
from openapi_server.models.exposed_action_response_schema import ExposedActionResponseSchema


pytestmark = pytest.mark.asyncio

async def test_check(client):
    """Test case for check

    Check
    """
    headers = { 
        'AccessPointApiKeyQuery': 'special-key',
        'SessionAuth': 'special-key',
        'AccessPointApiKeyHeader': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/check/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_execute_app_action_endpoint(client):
    """Test case for execute_app_action_endpoint

    Execute App Action Endpoint
    """
    body = {"instructions":"instructions","preview_only":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'AccessPointApiKeyQuery': 'special-key',
        'SessionAuth': 'special-key',
        'AccessPointApiKeyHeader': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/exposed/{exposed_app_action_id}/execute'.format(exposed_app_action_id='exposed_app_action_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_configuration_link(client):
    """Test case for get_configuration_link

    Get Configuration Link
    """
    headers = { 
        'AccessPointApiKeyQuery': 'special-key',
        'SessionAuth': 'special-key',
        'AccessPointApiKeyHeader': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/configuration-link/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_execution_log_endpoint(client):
    """Test case for get_execution_log_endpoint

    Get Execution Log Endpoint
    """
    headers = { 
        'Accept': 'application/json',
        'AccessPointApiKeyQuery': 'special-key',
        'SessionAuth': 'special-key',
        'AccessPointApiKeyHeader': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/execution-log/{execution_log_id}'.format(execution_log_id='execution_log_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_exposed_actions(client):
    """Test case for list_exposed_actions

    List Exposed Actions
    """
    headers = { 
        'Accept': 'application/json',
        'AccessPointApiKeyQuery': 'special-key',
        'SessionAuth': 'special-key',
        'AccessPointApiKeyHeader': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/exposed/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

