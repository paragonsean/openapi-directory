# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_core_dto_accounting_plan import ApiCoreDtoAccountingPlan
from openapi_server.models.api_core_dto_accounting_user import ApiCoreDtoAccountingUser


pytestmark = pytest.mark.asyncio

async def test_me_get_me(client):
    """Test case for me_get_me

    Retrieve current account data
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_get_me_plan(client):
    """Test case for me_get_me_plan

    Retrieve current account plan
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/plan',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

