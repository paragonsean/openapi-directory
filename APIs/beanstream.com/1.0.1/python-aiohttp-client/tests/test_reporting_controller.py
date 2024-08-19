# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beanstream_exception import BeanstreamException
from openapi_server.models.search_query import SearchQuery
from openapi_server.models.search_result import SearchResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_reports_post(client):
    """Test case for reports_post

    Search Query
    """
    search_query = openapi_server.SearchQuery()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/reports',
        headers=headers,
        json=search_query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

