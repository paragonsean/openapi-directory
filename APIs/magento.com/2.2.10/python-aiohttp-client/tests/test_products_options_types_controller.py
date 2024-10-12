# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_custom_option_type_interface import CatalogDataProductCustomOptionTypeInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_custom_option_type_list_v1_get_items_get(client):
    """Test case for catalog_product_custom_option_type_list_v1_get_items_get

    products/options/types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/options/types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

