# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rule_read import RuleRead


pytestmark = pytest.mark.asyncio

async def test_agent_legacy_complex_rule_collection(client):
    """Test case for agent_legacy_complex_rule_collection

    Retrieves the collection of Rule resources.
    """
    params = [('projectId', 'project_id_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/agent-rule-complexes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agent_legacy_straight_rule_collection(client):
    """Test case for agent_legacy_straight_rule_collection

    Retrieves the collection of Rule resources.
    """
    params = [('projectId', 'project_id_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/agent-rule-straights',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agent_rule_collection(client):
    """Test case for agent_rule_collection

    Retrieves the collection of Rule resources.
    """
    params = [('projectId', 'project_id_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/agent-rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_rule_collection(client):
    """Test case for export_rule_collection

    Retrieves the collection of Rule resources.
    """
    params = [('projectId', 'project_id_example'),
                    ('sort[id]', 'sort_id_example'),
                    ('sort[viewCount]', 'sort_view_count_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/export-rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule_collection(client):
    """Test case for get_rule_collection

    Retrieves the collection of Rule resources.
    """
    params = [('projectId', 'project_id_example'),
                    ('sort[id]', 'sort_id_example'),
                    ('sort[viewCount]', 'sort_view_count_example'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule_item(client):
    """Test case for get_rule_item

    Retrieves a Rule resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rules/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

