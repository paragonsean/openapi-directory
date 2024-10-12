# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_link_interface import CatalogDataProductLinkInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_link_management_v1_get_linked_items_by_type_get(client):
    """Test case for catalog_product_link_management_v1_get_linked_items_by_type_get

    products/{sku}/links/{type}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/{sku}/links/{type}'.format(sku='sku_example', type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

