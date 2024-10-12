# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.eav_data_attribute_option_interface import EavDataAttributeOptionInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_category_attribute_option_management_v1_get_items_get(client):
    """Test case for catalog_category_attribute_option_management_v1_get_items_get

    categories/attributes/{attributeCode}/options
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/categories/attributes/{attribute_code}/options'.format(attribute_code='attribute_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

