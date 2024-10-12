# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_customer_customer_group_config_v1_set_default_customer_group_put(client):
    """Test case for customer_customer_group_config_v1_set_default_customer_group_put

    customerGroups/default/{id}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/customerGroups/default/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

