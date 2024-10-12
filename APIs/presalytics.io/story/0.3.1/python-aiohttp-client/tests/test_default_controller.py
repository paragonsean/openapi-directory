# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_detail import ProblemDetail


pytestmark = pytest.mark.asyncio

async def test_get_environment(client):
    """Test case for get_environment

    Environment: Get
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/environment/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spec_no_tags(client):
    """Test case for spec_no_tags

    Specification: No tags
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/no_tags_spec',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

