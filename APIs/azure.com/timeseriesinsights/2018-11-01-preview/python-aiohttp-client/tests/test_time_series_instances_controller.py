# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_instances_page import GetInstancesPage
from openapi_server.models.instances_batch_request import InstancesBatchRequest
from openapi_server.models.instances_batch_response import InstancesBatchResponse
from openapi_server.models.instances_suggest_request import InstancesSuggestRequest
from openapi_server.models.instances_suggest_response import InstancesSuggestResponse
from openapi_server.models.search_instances_request import SearchInstancesRequest
from openapi_server.models.search_instances_response_page import SearchInstancesResponsePage
from openapi_server.models.tsi_error import TsiError


pytestmark = pytest.mark.asyncio

async def test_time_series_instances_execute_batch(client):
    """Test case for time_series_instances_execute_batch

    
    """
    parameters = {"get":{"timeSeriesIds":[["{}","{}"],["{}","{}"]],"names":["names","names"]},"update":[{"hierarchyIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","timeSeriesId":["{}","{}"],"description":"description","typeId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","instanceFields":{"key":"{}"}},{"hierarchyIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","timeSeriesId":["{}","{}"],"description":"description","typeId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","instanceFields":{"key":"{}"}}],"delete":{"timeSeriesIds":[["{}","{}"],["{}","{}"]],"names":["names","names"]},"put":[{"hierarchyIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","timeSeriesId":["{}","{}"],"description":"description","typeId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","instanceFields":{"key":"{}"}},{"hierarchyIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","timeSeriesId":["{}","{}"],"description":"description","typeId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","instanceFields":{"key":"{}"}}]}
    params = [('api-version', '2018-11-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ms_client_request_id': 'x_ms_client_request_id_example',
        'x_ms_client_session_id': 'x_ms_client_session_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/timeseries/instances/$batch',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_series_instances_get(client):
    """Test case for time_series_instances_get

    
    """
    params = [('api-version', '2018-11-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'x_ms_continuation': 'x_ms_continuation_example',
        'x_ms_client_request_id': 'x_ms_client_request_id_example',
        'x_ms_client_session_id': 'x_ms_client_session_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/timeseries/instances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_series_instances_search(client):
    """Test case for time_series_instances_search

    
    """
    parameters = {"path":["path","path"],"searchString":"searchString","hierarchies":{"expand":{"kind":"UntilChildren"},"pageSize":0,"sort":{"by":"CumulativeInstanceCount"}},"instances":{"highlights":True,"pageSize":6,"sort":{"by":"Rank"},"recursive":True}}
    params = [('api-version', '2018-11-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ms_continuation': 'x_ms_continuation_example',
        'x_ms_client_request_id': 'x_ms_client_request_id_example',
        'x_ms_client_session_id': 'x_ms_client_session_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/timeseries/instances/search',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_series_instances_suggest(client):
    """Test case for time_series_instances_suggest

    
    """
    parameters = {"take":0,"searchString":"searchString"}
    params = [('api-version', '2018-11-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ms_client_request_id': 'x_ms_client_request_id_example',
        'x_ms_client_session_id': 'x_ms_client_session_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/timeseries/instances/suggest',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

