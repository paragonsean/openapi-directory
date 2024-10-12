# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_interface import CatalogDataProductInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_configurable_product_link_management_v1_get_children_get(client):
    """Test case for configurable_product_link_management_v1_get_children_get

    configurable-products/{sku}/children
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/configurable-products/{sku}/children'.format(sku='sku_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

