# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bundle_data_option_interface import BundleDataOptionInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_bundle_product_option_repository_v1_delete_by_id_delete(client):
    """Test case for bundle_product_option_repository_v1_delete_by_id_delete

    bundle-products/{sku}/options/{optionId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/bundle-products/{sku}/options/{option_id}'.format(sku='sku_example', option_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundle_product_option_repository_v1_get_get(client):
    """Test case for bundle_product_option_repository_v1_get_get

    bundle-products/{sku}/options/{optionId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/bundle-products/{sku}/options/{option_id}'.format(sku='sku_example', option_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

