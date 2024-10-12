# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.query_definition import QueryDefinition
from openapi_server.models.query_result import QueryResult


pytestmark = pytest.mark.asyncio

async def test_query_usage(client):
    """Test case for query_usage

    
    """
    parameters = {"timeframe":"MonthToDate","timePeriod":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"type":"Usage","dataset":{"filter":{"or":[null,null],"and":[null,null],"tag":{"values":["values","values"],"name":"name","operator":"In"},"dimension":{"values":["values","values"],"name":"name","operator":"In"}},"configuration":{"columns":["columns","columns"]},"granularity":"Daily","aggregation":{"key":{"function":"Sum","name":"name"}},"grouping":[{"name":"name","type":"Tag"},{"name":"name","type":"Tag"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{scope}/providers/Microsoft.CostManagement/query'.format(scope='scope_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

