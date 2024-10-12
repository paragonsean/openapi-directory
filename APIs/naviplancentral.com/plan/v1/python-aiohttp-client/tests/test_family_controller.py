# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.family_model import FamilyModel


pytestmark = pytest.mark.asyncio

async def test_family_get_by_planid(client):
    """Test case for family_get_by_planid

    Retrieve family
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/Family',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

