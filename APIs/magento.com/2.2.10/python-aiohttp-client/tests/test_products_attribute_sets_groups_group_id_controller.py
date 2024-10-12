# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_attribute_group_repository_v1_delete_by_id_delete(client):
    """Test case for catalog_product_attribute_group_repository_v1_delete_by_id_delete

    products/attribute-sets/groups/{groupId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/products/attribute-sets/groups/{group_id}'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

