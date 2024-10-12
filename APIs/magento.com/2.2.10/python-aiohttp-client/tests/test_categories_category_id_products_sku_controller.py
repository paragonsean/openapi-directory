# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_category_link_repository_v1_delete_by_ids_delete(client):
    """Test case for catalog_category_link_repository_v1_delete_by_ids_delete

    categories/{categoryId}/products/{sku}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/categories/{category_id}/products/{sku}'.format(category_id='category_id_example', sku='sku_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

