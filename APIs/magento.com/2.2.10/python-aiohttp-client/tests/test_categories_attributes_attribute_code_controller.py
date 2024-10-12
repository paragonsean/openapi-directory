# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_category_attribute_interface import CatalogDataCategoryAttributeInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_category_attribute_repository_v1_get_get(client):
    """Test case for catalog_category_attribute_repository_v1_get_get

    categories/attributes/{attributeCode}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/categories/attributes/{attribute_code}'.format(attribute_code='attribute_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

