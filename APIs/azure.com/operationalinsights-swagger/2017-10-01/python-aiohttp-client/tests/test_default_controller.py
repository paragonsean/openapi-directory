# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.query_body import QueryBody
from openapi_server.models.query_results import QueryResults


pytestmark = pytest.mark.asyncio

async def test_query_execute(client):
    """Test case for query_execute

    Execute an Analytics query
    """
    body = openapi_server.QueryBody()
    params = [('apiVersion', '2017-10-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/query'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_get(client):
    """Test case for query_get

    Execute an Analytics query
    """
    params = [('query', 'query_example'),
                    ('timespan', 'timespan_example'),
                    ('apiVersion', '2017-10-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/query'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

