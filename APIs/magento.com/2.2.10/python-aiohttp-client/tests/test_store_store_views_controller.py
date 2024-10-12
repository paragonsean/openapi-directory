# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.store_data_store_interface import StoreDataStoreInterface


pytestmark = pytest.mark.asyncio

async def test_store_store_repository_v1_get_list_get(client):
    """Test case for store_store_repository_v1_get_list_get

    store/storeViews
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/store/storeViews',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

