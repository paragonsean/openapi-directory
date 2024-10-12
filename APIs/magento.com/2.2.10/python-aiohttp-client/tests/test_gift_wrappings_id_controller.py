# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_wrapping_data_wrapping_interface import GiftWrappingDataWrappingInterface


pytestmark = pytest.mark.asyncio

async def test_gift_wrapping_wrapping_repository_v1_delete_by_id_delete(client):
    """Test case for gift_wrapping_wrapping_repository_v1_delete_by_id_delete

    gift-wrappings/{id}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/gift-wrappings/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gift_wrapping_wrapping_repository_v1_get_get(client):
    """Test case for gift_wrapping_wrapping_repository_v1_get_get

    gift-wrappings/{id}
    """
    params = [('storeId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/gift-wrappings/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

