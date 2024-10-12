# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_attribute_interface import CatalogDataProductAttributeInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_attribute_management_v1_get_attributes_get(client):
    """Test case for catalog_product_attribute_management_v1_get_attributes_get

    products/attribute-sets/{attributeSetId}/attributes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/attribute-sets/{attribute_set_id}/attributes'.format(attribute_set_id='attribute_set_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

