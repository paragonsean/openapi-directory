# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_interface import CatalogDataProductInterface
from openapi_server.models.configurable_product_configurable_product_management_v1_generate_variation_put_request import ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_configurable_product_configurable_product_management_v1_generate_variation_put(client):
    """Test case for configurable_product_configurable_product_management_v1_generate_variation_put

    configurable-products/variation
    """
    body = openapi_server.ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/configurable-products/variation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

