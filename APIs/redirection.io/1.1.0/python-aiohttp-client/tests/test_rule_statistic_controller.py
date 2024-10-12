# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rule_statistic import RuleStatistic


pytestmark = pytest.mark.asyncio

async def test_get_rule_statistic_collection(client):
    """Test case for get_rule_statistic_collection

    Retrieves the collection of RuleStatistic resources.
    """
    params = [('projectId', 'project_id_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rule-statistics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rule_statistic_item(client):
    """Test case for get_rule_statistic_item

    Retrieves a RuleStatistic resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rule-statistics/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

