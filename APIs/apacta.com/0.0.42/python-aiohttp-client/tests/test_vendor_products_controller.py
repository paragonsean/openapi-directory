# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.vendor_products_get200_response import VendorProductsGet200Response
from openapi_server.models.vendor_products_vendor_product_id_get200_response import VendorProductsVendorProductIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_vendor_products_get(client):
    """Test case for vendor_products_get

    List vendor products
    """
    params = [('name', 'name_example'),
                    ('product_number', 'product_number_example'),
                    ('barcode', 'barcode_example'),
                    ('vendor_id', 'vendor_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vendor_products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendor_products_vendor_product_id_get(client):
    """Test case for vendor_products_vendor_product_id_get

    View single vendor product
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vendor_products/{vendor_product_id}'.format(vendor_product_id='vendor_product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

