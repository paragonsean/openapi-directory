# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.demote_to_node200_response import DemoteToNode200Response
from openapi_server.models.promote_to_relay200_response import PromoteToRelay200Response


pytestmark = pytest.mark.asyncio

async def test_demote_to_node(client):
    """Test case for demote_to_node

    Demote a relay to simple node
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/scaleoutrelay/demote/{node_id}'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_promote_to_relay(client):
    """Test case for promote_to_relay

    Promote a node to relay
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/scaleoutrelay/promote/{node_id}'.format(node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

