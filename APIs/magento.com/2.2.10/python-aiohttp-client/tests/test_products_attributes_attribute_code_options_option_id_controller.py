# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_attribute_option_management_v1_delete_delete(client):
    """Test case for catalog_product_attribute_option_management_v1_delete_delete

    products/attributes/{attributeCode}/options/{optionId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/products/attributes/{attribute_code}/options/{option_id}'.format(attribute_code='attribute_code_example', option_id='option_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

