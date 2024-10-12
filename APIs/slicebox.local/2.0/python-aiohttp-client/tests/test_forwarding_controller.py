# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.forwardingrule import Forwardingrule


pytestmark = pytest.mark.asyncio

async def test_forwarding_rule_id_delete(client):
    """Test case for forwarding_rule_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/forwarding/rule/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forwarding_rules_get(client):
    """Test case for forwarding_rules_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/forwarding/rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forwarding_rules_post(client):
    """Test case for forwarding_rules_post

    
    """
    fowarding_rule = openapi_server.Forwardingrule()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/forwarding/rules',
        headers=headers,
        json=fowarding_rule,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

