# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ast_response import ASTResponse
from openapi_server.models.analyze_query_response import AnalyzeQueryResponse
from openapi_server.models.error import Error
from openapi_server.models.flux_suggestion import FluxSuggestion
from openapi_server.models.flux_suggestions import FluxSuggestions
from openapi_server.models.language_request import LanguageRequest
from openapi_server.models.post_query_request import PostQueryRequest
from openapi_server.models.query import Query


pytestmark = pytest.mark.asyncio

async def test_get_query_suggestions(client):
    """Test case for get_query_suggestions

    Retrieve query suggestions
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/query/suggestions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_query_suggestions_name(client):
    """Test case for get_query_suggestions_name

    Retrieve query suggestions for a branching suggestion
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/query/suggestions/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_query(client):
    """Test case for post_query

    Query InfluxDB
    """
    body = openapi_server.PostQueryRequest()
    params = [('org', 'org_example'),
                    ('orgID', 'org_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
        'accept_encoding': identity,
        'content_type': 'content_type_example',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/query',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_query_analyze(client):
    """Test case for post_query_analyze

    Analyze an InfluxQL or Flux query
    """
    body = {"dialect":{"commentPrefix":"#","dateTimeFormat":"RFC3339","delimiter":",","annotations":["group","group"],"header":True},"now":"2000-01-23T04:56:07.000+00:00","query":"query","extern":{"imports":[{"path":{"type":"type","value":"value"},"as":{"name":"name","type":"type"},"type":"type"},{"path":{"type":"type","value":"value"},"as":{"name":"name","type":"type"},"type":"type"}],"package":{"name":{"name":"name","type":"type"},"type":"type"},"name":"name","body":[{"text":"text","type":"type"},{"text":"text","type":"type"}],"type":"type"},"params":{"key":""},"type":"flux"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
        'content_type': 'content_type_example',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/query/analyze',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_query_ast(client):
    """Test case for post_query_ast

    Generate an Abstract Syntax Tree (AST) from a query
    """
    body = {"query":"query"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
        'content_type': 'content_type_example',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/query/ast',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

