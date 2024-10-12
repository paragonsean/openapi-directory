# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.condition_details import ConditionDetails
from openapi_server.models.condition_public import ConditionPublic


pytestmark = pytest.mark.asyncio

async def test_get_all_conditions(client):
    """Test case for get_all_conditions

    List all conditions
    """
    params = [('age.value', 18),
                    ('age.unit', year),
                    ('enable_triage_5', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/conditions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_condition(client):
    """Test case for get_condition

    Get condition by id
    """
    params = [('age.value', 18),
                    ('age.unit', year),
                    ('enable_triage_5', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/conditions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

