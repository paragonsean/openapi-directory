# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bundle_product_option_management_v1_save_post_request import BundleProductOptionManagementV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bundle_product_option_management_v1_save_put(client):
    """Test case for bundle_product_option_management_v1_save_put

    bundle-products/options/{optionId}
    """
    body = openapi_server.BundleProductOptionManagementV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/bundle-products/options/{option_id}'.format(option_id='option_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

