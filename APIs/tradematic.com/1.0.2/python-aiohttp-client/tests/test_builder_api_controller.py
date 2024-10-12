# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.rule import Rule


pytestmark = pytest.mark.asyncio

async def test_builder_rules_get(client):
    """Test case for builder_rules_get

    Get strategy builder rules list
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/builder/rules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builder_rules_ruleid_get(client):
    """Test case for builder_rules_ruleid_get

    Get strategy builder rules by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/builder/rules/{ruleid}'.format(ruleid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

