# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.configurable_product_option_repository_v1_save_post_request import ConfigurableProductOptionRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_configurable_product_option_repository_v1_save_post(client):
    """Test case for configurable_product_option_repository_v1_save_post

    configurable-products/{sku}/options
    """
    body = openapi_server.ConfigurableProductOptionRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/configurable-products/{sku}/options'.format(sku='sku_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

