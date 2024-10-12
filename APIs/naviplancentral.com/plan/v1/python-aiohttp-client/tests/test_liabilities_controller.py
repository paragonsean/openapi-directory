# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.liabilities_model import LiabilitiesModel
from openapi_server.models.liability_model import LiabilityModel


pytestmark = pytest.mark.asyncio

async def test_liabilities_get_by_id_planid(client):
    """Test case for liabilities_get_by_id_planid

    Retrieve a liability
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/Liabilities/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_liabilities_get_by_planid(client):
    """Test case for liabilities_get_by_planid

    Retrieve liabilities
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/Liabilities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

