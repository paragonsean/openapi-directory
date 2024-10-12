# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bundle_data_option_interface import BundleDataOptionInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_bundle_product_option_repository_v1_get_list_get(client):
    """Test case for bundle_product_option_repository_v1_get_list_get

    bundle-products/{sku}/options/all
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/bundle-products/{sku}/options/all'.format(sku='sku_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

