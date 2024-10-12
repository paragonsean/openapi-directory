# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.plan_information_model import PlanInformationModel


pytestmark = pytest.mark.asyncio

async def test_plan_information_get_by_planid(client):
    """Test case for plan_information_get_by_planid

    Retrieve plan information
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/PlanInformation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

