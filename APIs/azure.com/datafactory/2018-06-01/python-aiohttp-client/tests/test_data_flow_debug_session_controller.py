# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_data_flow_to_debug_session_response import AddDataFlowToDebugSessionResponse
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.create_data_flow_debug_session_request import CreateDataFlowDebugSessionRequest
from openapi_server.models.create_data_flow_debug_session_response import CreateDataFlowDebugSessionResponse
from openapi_server.models.data_flow_debug_command_request import DataFlowDebugCommandRequest
from openapi_server.models.data_flow_debug_command_response import DataFlowDebugCommandResponse
from openapi_server.models.data_flow_debug_package import DataFlowDebugPackage
from openapi_server.models.delete_data_flow_debug_session_request import DeleteDataFlowDebugSessionRequest
from openapi_server.models.query_data_flow_debug_sessions_response import QueryDataFlowDebugSessionsResponse


pytestmark = pytest.mark.asyncio

async def test_data_flow_debug_session_add_data_flow(client):
    """Test case for data_flow_debug_session_add_data_flow

    
    """
    request = {"debugSettings":{"datasetParameters":"{}","sourceSettings":[{"rowLimit":0,"sourceName":"sourceName"},{"rowLimit":0,"sourceName":"sourceName"}],"parameters":{"key":"{}"}},"dataFlow":{"properties":"{}"},"linkedServices":[{"properties":{"key":"{}"}},{"properties":{"key":"{}"}}],"datasets":[{"properties":{"key":"{}"}},{"properties":{"key":"{}"}}],"sessionId":"sessionId","staging":{"folderPath":"folderPath","linkedService":{"type":"LinkedServiceReference","parameters":{"key":"{}"},"referenceName":"referenceName"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/addDataFlowToDebugSession'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_flow_debug_session_create(client):
    """Test case for data_flow_debug_session_create

    
    """
    request = {"timeToLive":6,"computeType":"computeType","coreCount":0,"integrationRuntime":{"properties":{"key":"{}"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/createDataFlowDebugSession'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_flow_debug_session_delete(client):
    """Test case for data_flow_debug_session_delete

    
    """
    request = {"sessionId":"sessionId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/deleteDataFlowDebugSession'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_flow_debug_session_execute_command(client):
    """Test case for data_flow_debug_session_execute_command

    
    """
    request = {"sessionId":"sessionId","command":"executePreviewQuery","commandPayload":{"expression":"expression","columns":["columns","columns"],"streamName":"streamName","rowLimits":0}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/executeDataFlowDebugCommand'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_flow_debug_session_query_by_factory(client):
    """Test case for data_flow_debug_session_query_by_factory

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/queryDataFlowDebugSessions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

