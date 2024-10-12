# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.integration_runtime_nodes_get_ip_address200_response import IntegrationRuntimeNodesGetIpAddress200Response
from openapi_server.models.integration_runtime_nodes_update200_response import IntegrationRuntimeNodesUpdate200Response
from openapi_server.models.update_integration_runtime_node_request import UpdateIntegrationRuntimeNodeRequest


pytestmark = pytest.mark.asyncio

async def test_integration_runtime_nodes_delete(client):
    """Test case for integration_runtime_nodes_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/integrationRuntimes/{integration_runtime_name}/nodes/{node_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', integration_runtime_name='integration_runtime_name_example', node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_runtime_nodes_get_ip_address(client):
    """Test case for integration_runtime_nodes_get_ip_address

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/integrationRuntimes/{integration_runtime_name}/nodes/{node_name}/ipAddress'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', integration_runtime_name='integration_runtime_name_example', node_name='node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_runtime_nodes_update(client):
    """Test case for integration_runtime_nodes_update

    
    """
    update_integration_runtime_node_request = {"concurrentJobsLimit":1}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/integrationRuntimes/{integration_runtime_name}/nodes/{node_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', integration_runtime_name='integration_runtime_name_example', node_name='node_name_example'),
        headers=headers,
        json=update_integration_runtime_node_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

