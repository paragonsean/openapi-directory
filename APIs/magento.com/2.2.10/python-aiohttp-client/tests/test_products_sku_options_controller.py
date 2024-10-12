# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_custom_option_interface import CatalogDataProductCustomOptionInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_custom_option_repository_v1_get_list_get(client):
    """Test case for catalog_product_custom_option_repository_v1_get_list_get

    products/{sku}/options
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/{sku}/options'.format(sku='sku_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

