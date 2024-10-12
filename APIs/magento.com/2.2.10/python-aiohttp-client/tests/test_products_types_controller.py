# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_type_interface import CatalogDataProductTypeInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_type_list_v1_get_product_types_get(client):
    """Test case for catalog_product_type_list_v1_get_product_types_get

    products/types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

