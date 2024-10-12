# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.export import Export
from openapi_server.models.export_execution_list_result import ExportExecutionListResult
from openapi_server.models.export_list_result import ExportListResult


pytestmark = pytest.mark.asyncio

async def test_exports_create_or_update(client):
    """Test case for exports_create_or_update

    
    """
    parameters = {"properties":{"schedule":{"recurrence":"Daily","recurrencePeriod":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"status":"Active"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.CostManagement/exports/{export_name}'.format(scope='scope_example', export_name='export_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_exports_delete(client):
    """Test case for exports_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.CostManagement/exports/{export_name}'.format(scope='scope_example', export_name='export_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_exports_execute(client):
    """Test case for exports_execute

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{scope}/providers/Microsoft.CostManagement/exports/{export_name}/run'.format(scope='scope_example', export_name='export_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_exports_get(client):
    """Test case for exports_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.CostManagement/exports/{export_name}'.format(scope='scope_example', export_name='export_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_exports_get_execution_history(client):
    """Test case for exports_get_execution_history

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.CostManagement/exports/{export_name}/runHistory'.format(scope='scope_example', export_name='export_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_exports_list(client):
    """Test case for exports_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.CostManagement/exports'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

