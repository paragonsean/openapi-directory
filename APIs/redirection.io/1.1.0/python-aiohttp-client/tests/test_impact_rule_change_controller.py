# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.impact_rule_change_read import ImpactRuleChangeRead
from openapi_server.models.impact_rule_change_write import ImpactRuleChangeWrite


pytestmark = pytest.mark.asyncio

async def test_get_impact_rule_change_item(client):
    """Test case for get_impact_rule_change_item

    Retrieves a ImpactRuleChange resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/impact-rule-changes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_impact_rule_change_collection(client):
    """Test case for post_impact_rule_change_collection

    Creates a ImpactRuleChange resource.
    """
    impact_rule_change = openapi_server.ImpactRuleChangeWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/impact-rule-changes',
        headers=headers,
        json=impact_rule_change,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

