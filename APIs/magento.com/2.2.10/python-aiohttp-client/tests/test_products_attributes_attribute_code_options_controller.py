# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_product_attribute_option_management_v1_add_post_request import CatalogProductAttributeOptionManagementV1AddPostRequest
from openapi_server.models.eav_data_attribute_option_interface import EavDataAttributeOptionInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_attribute_option_management_v1_add_post(client):
    """Test case for catalog_product_attribute_option_management_v1_add_post

    products/attributes/{attributeCode}/options
    """
    body = openapi_server.CatalogProductAttributeOptionManagementV1AddPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/attributes/{attribute_code}/options'.format(attribute_code='attribute_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_product_attribute_option_management_v1_get_items_get(client):
    """Test case for catalog_product_attribute_option_management_v1_get_items_get

    products/attributes/{attributeCode}/options
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/attributes/{attribute_code}/options'.format(attribute_code='attribute_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

