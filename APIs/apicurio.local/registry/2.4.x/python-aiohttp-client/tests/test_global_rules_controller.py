# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.rule import Rule
from openapi_server.models.rule_type import RuleType


pytestmark = pytest.mark.asyncio

async def test_create_global_rule(client):
    """Test case for create_global_rule

    Create global rule
    """
    body = {"config":"FULL","type":"VALIDITY"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/admin/rules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_all_global_rules(client):
    """Test case for delete_all_global_rules

    Delete all global rules
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/admin/rules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_global_rule(client):
    """Test case for delete_global_rule

    Delete global rule
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/admin/rules/{rule}'.format(rule=openapi_server.RuleType()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_global_rule_config(client):
    """Test case for get_global_rule_config

    Get global rule configuration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/rules/{rule}'.format(rule=openapi_server.RuleType()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_global_rules(client):
    """Test case for list_global_rules

    List global rules
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/admin/rules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_global_rule_config(client):
    """Test case for update_global_rule_config

    Update global rule configuration
    """
    body = {"config":"FULL","type":"VALIDITY"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/admin/rules/{rule}'.format(rule=openapi_server.RuleType()),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

