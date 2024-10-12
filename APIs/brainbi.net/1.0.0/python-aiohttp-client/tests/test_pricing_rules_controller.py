# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_rule_data(client):
    """Test case for rule_data

    Rule Data
    """
    params = [('', '')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/rule/ruleData/1',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rule_data_latest(client):
    """Test case for rule_data_latest

    Rule Data Latest
    """
    params = [('', '')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/rule/ruleData/1/latest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rules(client):
    """Test case for rules

    Rules
    """
    params = [('', '')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/rule',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

