# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.availability_response import AvailabilityResponse
from openapi_server.models.event_schema import EventSchema
from openapi_server.models.get_event_schema_request import GetEventSchemaRequest
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_result_page import QueryResultPage
from openapi_server.models.tsi_error import TsiError


pytestmark = pytest.mark.asyncio

async def test_query_execute(client):
    """Test case for query_execute

    
    """
    parameters = {"getEvents":{"filter":{"tsx":"tsx"},"take":0,"searchSpan":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"projectedProperties":[{"name":"name","type":"Bool"},{"name":"name","type":"Bool"}],"timeSeriesId":["{}","{}"]},"getSeries":{"filter":{"tsx":"tsx"},"projectedVariables":["projectedVariables","projectedVariables"],"take":6,"searchSpan":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"timeSeriesId":["{}","{}"],"inlineVariables":{"key":{"filter":{"tsx":"tsx"},"kind":"kind"}}},"aggregateSeries":{"filter":{"tsx":"tsx"},"projectedVariables":["projectedVariables","projectedVariables"],"searchSpan":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"timeSeriesId":["{}","{}"],"inlineVariables":{"key":{"filter":{"tsx":"tsx"},"kind":"kind"}},"interval":"interval"}}
    params = [('api-version', '2018-11-01-preview'),
                    ('storeType', 'store_type_example')]
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
        path='/timeseries/query',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_get_availability(client):
    """Test case for query_get_availability

    
    """
    params = [('api-version', '2018-11-01-preview'),
                    ('storeType', 'store_type_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ms_client_request_id': 'x_ms_client_request_id_example',
        'x_ms_client_session_id': 'x_ms_client_session_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/availability',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_get_event_schema(client):
    """Test case for query_get_event_schema

    
    """
    parameters = {"searchSpan":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', '2018-11-01-preview'),
                    ('storeType', 'store_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ms_client_request_id': 'x_ms_client_request_id_example',
        'x_ms_client_session_id': 'x_ms_client_session_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/eventSchema',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

