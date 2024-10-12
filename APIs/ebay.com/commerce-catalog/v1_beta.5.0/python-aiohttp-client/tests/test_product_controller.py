# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product import Product


pytestmark = pytest.mark.asyncio

async def test_get_product(client):
    """Test case for get_product

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/commerce/catalog/v1_beta/product/{epid}'.format(epid='epid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

