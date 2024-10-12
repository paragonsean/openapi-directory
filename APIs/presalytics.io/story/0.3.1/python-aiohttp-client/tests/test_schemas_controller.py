# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_detail import ProblemDetail


pytestmark = pytest.mark.asyncio

async def test_story_outline_schema(client):
    """Test case for story_outline_schema

    Story Outline Schema
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/outline-schema/{schema_version}/story-outline.json'.format(schema_version='schema_version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

