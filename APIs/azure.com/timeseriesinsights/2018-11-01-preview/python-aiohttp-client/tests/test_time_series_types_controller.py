# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_types_page import GetTypesPage
from openapi_server.models.tsi_error import TsiError
from openapi_server.models.types_batch_request import TypesBatchRequest
from openapi_server.models.types_batch_response import TypesBatchResponse


pytestmark = pytest.mark.asyncio

async def test_time_series_types_execute_batch(client):
    """Test case for time_series_types_execute_batch

    
    """
    parameters = {"get":{"names":["names","names"],"typeIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]},"delete":{"names":["names","names"],"typeIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]},"put":[{"variables":"{}","name":"name","description":"description","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"variables":"{}","name":"name","description":"description","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}]}
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
        path='/timeseries/types/$batch',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_series_types_get(client):
    """Test case for time_series_types_get

    
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
        path='/timeseries/types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

