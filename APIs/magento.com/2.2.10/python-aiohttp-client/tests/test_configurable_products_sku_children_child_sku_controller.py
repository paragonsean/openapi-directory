# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_configurable_product_link_management_v1_remove_child_delete(client):
    """Test case for configurable_product_link_management_v1_remove_child_delete

    configurable-products/{sku}/children/{childSku}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/configurable-products/{sku}/children/{child_sku}'.format(sku='sku_example', child_sku='child_sku_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

