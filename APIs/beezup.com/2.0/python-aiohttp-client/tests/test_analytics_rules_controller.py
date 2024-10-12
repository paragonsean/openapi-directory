# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.create_rule_request import CreateRuleRequest
from openapi_server.models.rule import Rule
from openapi_server.models.rule_execution_reportings import RuleExecutionReportings
from openapi_server.models.rule_list import RuleList
from openapi_server.models.update_rule_request import UpdateRuleRequest


pytestmark = pytest.mark.asyncio

async def test_create_rule(client):
    """Test case for create_rule

    Rule creation
    """
    body = openapi_server.CreateRuleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/rules'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_rule(client):
    """Test case for delete_rule

    Delete Rule
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/user/analytics/{store_id}/rules/{rule_id}'.format(store_id='store_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_rule(client):
    """Test case for disable_rule

    Disable rule
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/rules/{rule_id}/disable'.format(store_id='store_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_rule(client):
    """Test case for enable_rule

    Enable rule
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/rules/{rule_id}/enable'.format(store_id='store_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule(client):
    """Test case for get_rule

    Gets the rule
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/{store_id}/rules/{rule_id}'.format(store_id='store_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rules(client):
    """Test case for get_rules

    Gets the list of rules for a given store
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/{store_id}/rules'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rules_executions(client):
    """Test case for get_rules_executions

    Get the rules execution history
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/{store_id}/rules/executions'.format(store_id='store_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_down_rule(client):
    """Test case for move_down_rule

    Move the rule down
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/rules/{rule_id}/movedown'.format(store_id='store_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_up_rule(client):
    """Test case for move_up_rule

    Move the rule up
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/rules/{rule_id}/moveup'.format(store_id='store_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_rule(client):
    """Test case for run_rule

    Run rule
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/rules/{rule_id}/run'.format(store_id='store_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_rules(client):
    """Test case for run_rules

    Run all rules for this store
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/rules/run'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_rule(client):
    """Test case for update_rule

    Update Rule
    """
    body = openapi_server.UpdateRuleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/user/analytics/{store_id}/rules/{rule_id}'.format(store_id='store_id_example', rule_id='rule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

