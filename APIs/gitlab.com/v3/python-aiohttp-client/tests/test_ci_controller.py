# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post_v3_ci_lint_request import PostV3CiLintRequest


pytestmark = pytest.mark.asyncio

async def test_post_v3_ci_lint(client):
    """Test case for post_v3_ci_lint

    Validation of .gitlab-ci.yml content
    """
    body = openapi_server.PostV3CiLintRequest()
    headers = { 
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/ci/lint',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

