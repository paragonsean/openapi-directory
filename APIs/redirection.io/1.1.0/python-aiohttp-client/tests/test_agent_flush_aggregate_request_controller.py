# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.agent_flush_aggregate_request import AgentFlushAggregateRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_agent_flush_aggregate_request_collection(client):
    """Test case for post_agent_flush_aggregate_request_collection

    Creates a AgentFlushAggregateRequest resource.
    """
    agent_flush_aggregate_request = {"instanceName":"{}","instanceTime":"{}","logs":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/agent-flush-aggregate-requests',
        headers=headers,
        json=agent_flush_aggregate_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

