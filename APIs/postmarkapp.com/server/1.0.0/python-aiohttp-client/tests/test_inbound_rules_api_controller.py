# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_inbound_rule200_response import CreateInboundRule200Response
from openapi_server.models.create_inbound_rule_request import CreateInboundRuleRequest
from openapi_server.models.list_inbound_rules200_response import ListInboundRules200Response
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse


pytestmark = pytest.mark.asyncio

async def test_create_inbound_rule(client):
    """Test case for create_inbound_rule

    Create an inbound rule trigger
    """
    body = {"Rule":"Rule"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='POST',
        path='/triggers/inboundrules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_inbound_rule(client):
    """Test case for delete_inbound_rule

    Delete a single trigger
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='DELETE',
        path='/triggers/inboundrules/{triggerid}'.format(triggerid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_inbound_rules(client):
    """Test case for list_inbound_rules

    List inbound rule triggers
    """
    params = [('count', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/triggers/inboundrules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

