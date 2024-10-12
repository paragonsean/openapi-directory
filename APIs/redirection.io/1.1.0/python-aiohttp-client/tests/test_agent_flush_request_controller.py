# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.agent_flush_request import AgentFlushRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_agent_flush_requests_post(client):
    """Test case for agent_flush_requests_post

    Creates a AgentFlushRequest resource.
    """
    agent_flush_request = {"instanceName":"{}","instanceTime":0,"logs":["logs","logs"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/agent-flush-requests',
        headers=headers,
        json=agent_flush_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_logs_post(client):
    """Test case for post_logs_post

    Creates a AgentFlushRequest resource.
    """
    agent_flush_request = {"instanceName":"{}","instanceTime":0,"logs":["logs","logs"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/post-logs',
        headers=headers,
        json=agent_flush_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

