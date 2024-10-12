# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.graph_ql_request import GraphQLRequest
from openapi_server.models.graph_ql_response import GraphQLResponse


pytestmark = pytest.mark.asyncio

async def test_get_documentation(client):
    """Test case for get_documentation

    Return this API document in JSON format
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/openapi.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_graph_ql(client):
    """Test case for post_graph_ql

    Perform a GraphQL Query
    """
    body = {"variables":"{}","query":"{}","operationName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='//api/catalog-inventory/v1.0/graphql',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

