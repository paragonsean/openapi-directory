# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rule_set_version import RuleSetVersion
from openapi_server.models.rule_set_version_read import RuleSetVersionRead


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_clear_rule_set_version_item(client):
    """Test case for clear_rule_set_version_item

    Clear a version
    """
    rule_set_version = {"createdAt":"2000-01-23T04:56:07.000+00:00","current":True,"mergedRulesCount":6,"publishedAt":"2000-01-23T04:56:07.000+00:00","name":"name","working":True,"id":"id","isSnapshot":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rule-set-versions/{id}/clear'.format(id='id_example'),
        headers=headers,
        json=rule_set_version,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule_set_version_collection(client):
    """Test case for get_rule_set_version_collection

    Retrieves the collection of RuleSetVersion resources.
    """
    params = [('projectId', 'project_id_example'),
                    ('sort[createdAt]', 'sort_created_at_example'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rule-set-versions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule_set_version_item(client):
    """Test case for get_rule_set_version_item

    Retrieves a RuleSetVersion resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rule-set-versions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_publish_rule_set_version_item(client):
    """Test case for publish_rule_set_version_item

    Publish a version
    """
    rule_set_version = {"createdAt":"2000-01-23T04:56:07.000+00:00","current":True,"mergedRulesCount":6,"publishedAt":"2000-01-23T04:56:07.000+00:00","name":"name","working":True,"id":"id","isSnapshot":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rule-set-versions/{id}/publish'.format(id='id_example'),
        headers=headers,
        json=rule_set_version,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

