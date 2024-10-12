# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rule import Rule
from openapi_server.models.rule_full_response import RuleFullResponse
from openapi_server.models.rule_short_response import RuleShortResponse


pytestmark = pytest.mark.asyncio

async def test_add_rule(client):
    """Test case for add_rule

    
    """
    rule_object = {"actionIds":"actionIds","triggerIds":"triggerIds","name":"name","description":"description","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rules',
        headers=headers,
        json=rule_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule(client):
    """Test case for get_rule

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rules/{rule_id}'.format(rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_rules(client):
    """Test case for list_rules

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_rule(client):
    """Test case for remove_rule

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rules/{rule_id}'.format(rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_rule(client):
    """Test case for run_rule

    
    """
    initial_data = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rules/{rule_id}/run'.format(rule_id='rule_id_example'),
        headers=headers,
        json=initial_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_rule(client):
    """Test case for update_rule

    
    """
    rule_object = {"actionIds":"actionIds","triggerIds":"triggerIds","name":"name","description":"description","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rules/{rule_id}'.format(rule_id='rule_id_example'),
        headers=headers,
        json=rule_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

