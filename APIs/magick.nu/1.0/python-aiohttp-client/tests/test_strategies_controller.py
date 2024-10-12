# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_strategies_strategy_id_strategy_id(client):
    """Test case for get_strategies_strategy_id_strategy_id

    Get Strategy by ID
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/rest/strategies/strategyId/{strategy_id}'.format(strategy_id='strategy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_strategies_templates(client):
    """Test case for get_strategies_templates

    Get all Template Strategies
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/rest/strategies/templates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

