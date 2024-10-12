# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_link_repository_v1_delete_by_id_delete(client):
    """Test case for catalog_product_link_repository_v1_delete_by_id_delete

    products/{sku}/links/{type}/{linkedProductSku}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/products/{sku}/links/{type}/{linked_product_sku}'.format(sku='sku_example', type='type_example', linked_product_sku='linked_product_sku_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

