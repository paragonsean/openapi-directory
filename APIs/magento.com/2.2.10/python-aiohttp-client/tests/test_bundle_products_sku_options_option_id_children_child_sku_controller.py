# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_bundle_product_link_management_v1_remove_child_delete(client):
    """Test case for bundle_product_link_management_v1_remove_child_delete

    bundle-products/{sku}/options/{optionId}/children/{childSku}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/bundle-products/{sku}/options/{option_id}/children/{child_sku}'.format(sku='sku_example', option_id=56, child_sku='child_sku_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

