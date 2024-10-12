# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_website_link_repository_v1_delete_by_id_delete(client):
    """Test case for catalog_product_website_link_repository_v1_delete_by_id_delete

    products/{sku}/websites/{websiteId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/products/{sku}/websites/{website_id}'.format(sku='sku_example', website_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

