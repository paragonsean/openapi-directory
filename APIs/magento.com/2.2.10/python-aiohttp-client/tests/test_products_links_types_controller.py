# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_link_type_interface import CatalogDataProductLinkTypeInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_link_type_list_v1_get_items_get(client):
    """Test case for catalog_product_link_type_list_v1_get_items_get

    products/links/types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/links/types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

