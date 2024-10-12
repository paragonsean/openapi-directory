# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_attribute_management_v1_unassign_delete(client):
    """Test case for catalog_product_attribute_management_v1_unassign_delete

    products/attribute-sets/{attributeSetId}/attributes/{attributeCode}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/products/attribute-sets/{attribute_set_id}/attributes/{attribute_code}'.format(attribute_set_id='attribute_set_id_example', attribute_code='attribute_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

