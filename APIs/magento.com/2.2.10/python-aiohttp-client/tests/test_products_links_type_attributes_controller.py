# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_link_attribute_interface import CatalogDataProductLinkAttributeInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_link_type_list_v1_get_item_attributes_get(client):
    """Test case for catalog_product_link_type_list_v1_get_item_attributes_get

    products/links/{type}/attributes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/links/{type}/attributes'.format(type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

