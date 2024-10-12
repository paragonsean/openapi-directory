# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_data_group_interface import CustomerDataGroupInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_v1_customer_groups_default_store_id_get(client):
    """Test case for v1_customer_groups_default_store_id_get

    customerGroups/default/{storeId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/customerGroups/default/{store_id}'.format(store_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

