# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rule_change_read import RuleChangeRead
from openapi_server.models.rule_change_write import RuleChangeWrite


pytestmark = pytest.mark.asyncio

async def test_delete_rule_change_item(client):
    """Test case for delete_rule_change_item

    Removes the RuleChange resource.
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rule-changes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule_change_collection(client):
    """Test case for get_rule_change_collection

    Retrieves the collection of RuleChange resources.
    """
    params = [('versionId', 'version_id_example'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rule-changes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule_change_item(client):
    """Test case for get_rule_change_item

    Retrieves a RuleChange resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rule-changes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_rule_change_collection(client):
    """Test case for post_rule_change_collection

    Creates a RuleChange resource.
    """
    rule_change = openapi_server.RuleChangeWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rule-changes',
        headers=headers,
        json=rule_change,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

