# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.media_graph import MediaGraph
from openapi_server.models.media_graph_collection import MediaGraphCollection
from openapi_server.models.media_graph_operation_status import MediaGraphOperationStatus


pytestmark = pytest.mark.asyncio

async def test_media_graphs_create_or_update(client):
    """Test case for media_graphs_create_or_update

    Create or update a Media Graph
    """
    parameters = {"properties":{"sources":[{"@odata.type":"@odata.type","name":"name"},{"@odata.type":"@odata.type","name":"name"}],"sinks":[{"@odata.type":"@odata.type","inputs":["inputs","inputs"],"name":"name"},{"@odata.type":"@odata.type","inputs":["inputs","inputs"],"name":"name"}],"created":"2000-01-23T04:56:07.000+00:00","description":"description","lastModified":"2000-01-23T04:56:07.000+00:00","state":"Running"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/mediaGraphs/{media_graph_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', media_graph_name='media_graph_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_graphs_delete(client):
    """Test case for media_graphs_delete

    Delete a Media Graph
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/mediaGraphs/{media_graph_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', media_graph_name='media_graph_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_graphs_get(client):
    """Test case for media_graphs_get

    Get a Media Graph
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/mediaGraphs/{media_graph_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', media_graph_name='media_graph_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_graphs_list(client):
    """Test case for media_graphs_list

    List Media Graphs
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/mediaGraphs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_graphs_start(client):
    """Test case for media_graphs_start

    Start a Media Graph
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/mediaGraphs/{media_graph_name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', media_graph_name='media_graph_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_graphs_stop(client):
    """Test case for media_graphs_stop

    Stop a Media Graph
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/mediaGraphs/{media_graph_name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', media_graph_name='media_graph_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operation_results_get(client):
    """Test case for operation_results_get

    Get the operation result
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/mediaGraphs/{media_graph_name}/operationResults/{operation_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', media_graph_name='media_graph_name_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_status_get(client):
    """Test case for operations_status_get

    Get the operation status
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/mediaGraphs/{media_graph_name}/operationsStatus/{operation_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', media_graph_name='media_graph_name_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

