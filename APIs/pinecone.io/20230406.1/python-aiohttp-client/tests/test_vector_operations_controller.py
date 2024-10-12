# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_request import DeleteRequest
from openapi_server.models.describe_index_stats_request import DescribeIndexStatsRequest
from openapi_server.models.describe_index_stats_response import DescribeIndexStatsResponse
from openapi_server.models.fetch_request import FetchRequest
from openapi_server.models.fetch_response import FetchResponse
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_response import QueryResponse
from openapi_server.models.update_request import UpdateRequest
from openapi_server.models.upsert_request import UpsertRequest
from openapi_server.models.upsert_response import UpsertResponse


pytestmark = pytest.mark.asyncio

async def test_delete(client):
    """Test case for delete

    Delete
    """
    body = {"filter":{"hello":["alpha","bravo"]},"deleteAll":False,"namespace":"namespace-0","ids":["vector-0","vector-0"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vectors/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_index_stats(client):
    """Test case for describe_index_stats

    Describe Index Stats
    """
    body = {"filter":{"hello":["alpha","bravo"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/describe_index_stats',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch(client):
    """Test case for fetch

    Fetch
    """
    body = {"namespace":"namespace-0","ids":["vector-0","vector-0"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vectors/fetch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query(client):
    """Test case for query

    Query
    """
    body = {"filter":{"hello":["alpha","bravo"]},"topK":800,"includeMetadata":False,"includeValues":False,"sparseVector":{"indices":[1],"values":[2]},"namespace":"namespace-0","vector":[1,2,3],"id":"vector-0"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update(client):
    """Test case for update

    Fetch
    """
    body = {"setMetadata":{"hello":"alpha"},"values":[1,2,3],"namespace":"namespace-0","id":"id","sparseValues":{"indices":[1],"values":[2]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vectors/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert(client):
    """Test case for upsert

    Upsert
    """
    body = {"vectors":[{"metadata":{"hello":"alpha"},"values":[1,2,3],"id":"vector-0","sparseValues":{"indices":[1],"values":[2]}},{"metadata":{"hello":"alpha"},"values":[1,2,3],"id":"vector-0","sparseValues":{"indices":[1],"values":[2]}}],"namespace":"namespace-0"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vectors/upsert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

