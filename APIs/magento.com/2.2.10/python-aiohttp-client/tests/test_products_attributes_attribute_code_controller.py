# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_attribute_interface import CatalogDataProductAttributeInterface
from openapi_server.models.catalog_product_attribute_repository_v1_save_post_request import CatalogProductAttributeRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_attribute_repository_v1_delete_by_id_delete(client):
    """Test case for catalog_product_attribute_repository_v1_delete_by_id_delete

    products/attributes/{attributeCode}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/products/attributes/{attribute_code}'.format(attribute_code='attribute_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_product_attribute_repository_v1_get_get(client):
    """Test case for catalog_product_attribute_repository_v1_get_get

    products/attributes/{attributeCode}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/attributes/{attribute_code}'.format(attribute_code='attribute_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_attribute_repository_v1_save_put(client):
    """Test case for catalog_product_attribute_repository_v1_save_put

    products/attributes/{attributeCode}
    """
    body = openapi_server.CatalogProductAttributeRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/products/attributes/{attribute_code}'.format(attribute_code='attribute_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

