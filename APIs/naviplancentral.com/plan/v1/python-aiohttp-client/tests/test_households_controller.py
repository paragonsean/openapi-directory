# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.households_model import HouseholdsModel


pytestmark = pytest.mark.asyncio

async def test_households_get_by_householdid(client):
    """Test case for households_get_by_householdid

    Retrieve all Households associated with the user
    """
    params = [('householdId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/Households',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

