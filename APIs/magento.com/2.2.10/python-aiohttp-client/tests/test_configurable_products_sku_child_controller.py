# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.configurable_product_link_management_v1_add_child_post_request import ConfigurableProductLinkManagementV1AddChildPostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_configurable_product_link_management_v1_add_child_post(client):
    """Test case for configurable_product_link_management_v1_add_child_post

    configurable-products/{sku}/child
    """
    body = openapi_server.ConfigurableProductLinkManagementV1AddChildPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/configurable-products/{sku}/child'.format(sku='sku_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

