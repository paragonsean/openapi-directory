# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_software_plan_register(client):
    """Test case for software_plan_register

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.SoftwarePlan/register'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

