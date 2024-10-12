# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_rule200_response import CreateRule200Response
from openapi_server.models.create_rule_category200_response import CreateRuleCategory200Response
from openapi_server.models.delete_rule200_response import DeleteRule200Response
from openapi_server.models.delete_rule_category200_response import DeleteRuleCategory200Response
from openapi_server.models.get_rule_category_details200_response import GetRuleCategoryDetails200Response
from openapi_server.models.get_rule_tree200_response import GetRuleTree200Response
from openapi_server.models.list_rules200_response import ListRules200Response
from openapi_server.models.rule_category import RuleCategory
from openapi_server.models.rule_category_update import RuleCategoryUpdate
from openapi_server.models.rule_details200_response import RuleDetails200Response
from openapi_server.models.rule_new import RuleNew
from openapi_server.models.rule_with_category import RuleWithCategory
from openapi_server.models.update_rule200_response import UpdateRule200Response
from openapi_server.models.update_rule_category200_response import UpdateRuleCategory200Response


pytestmark = pytest.mark.asyncio

async def test_create_rule(client):
    """Test case for create_rule

    Create a rule
    """
    body = openapi_server.RuleNew()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rudder/api/latest/rules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_rule_category(client):
    """Test case for create_rule_category

    Create a rule category
    """
    body = openapi_server.RuleCategory()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rudder/api/latest/rules/categories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_rule(client):
    """Test case for delete_rule

    Delete a rule
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/rules/{rule_id}'.format(rule_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_rule_category(client):
    """Test case for delete_rule_category

    Delete group category
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/rules/categories/{rule_category_id}'.format(rule_category_id='e0a311fa-f7b2-4f9e-89a9-db517b9c6b90'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule_category_details(client):
    """Test case for get_rule_category_details

    Get rule category details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/rules/categories/{rule_category_id}'.format(rule_category_id='e0a311fa-f7b2-4f9e-89a9-db517b9c6b90'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule_tree(client):
    """Test case for get_rule_tree

    Get rules tree
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/rules/tree',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_rules(client):
    """Test case for list_rules

    List all rules
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/rules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rule_details(client):
    """Test case for rule_details

    Get a rule details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/rules/{rule_id}'.format(rule_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_rule(client):
    """Test case for update_rule

    Update a rule details
    """
    body = openapi_server.RuleWithCategory()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/rules/{rule_id}'.format(rule_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_rule_category(client):
    """Test case for update_rule_category

    Update rule category details
    """
    body = openapi_server.RuleCategoryUpdate()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/rules/categories/{rule_category_id}'.format(rule_category_id='e0a311fa-f7b2-4f9e-89a9-db517b9c6b90'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

