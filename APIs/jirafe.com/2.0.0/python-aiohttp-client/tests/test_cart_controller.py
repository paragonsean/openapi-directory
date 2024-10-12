# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cart import Cart


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_cart(client):
    """Test case for post_cart

    Send a cart for the given site
    """
    body = openapi_server.Cart()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/{site_id}/cart'.format(site_id='site_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

