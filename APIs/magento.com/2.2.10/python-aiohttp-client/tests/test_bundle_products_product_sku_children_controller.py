# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bundle_data_link_interface import BundleDataLinkInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_bundle_product_link_management_v1_get_children_get(client):
    """Test case for bundle_product_link_management_v1_get_children_get

    bundle-products/{productSku}/children
    """
    params = [('optionId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/bundle-products/{product_sku}/children'.format(product_sku='product_sku_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

