# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_category_interface import CatalogDataCategoryInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_category_repository_v1_delete_by_identifier_delete(client):
    """Test case for catalog_category_repository_v1_delete_by_identifier_delete

    categories/{categoryId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/categories/{category_id}'.format(category_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_category_repository_v1_get_get(client):
    """Test case for catalog_category_repository_v1_get_get

    categories/{categoryId}
    """
    params = [('storeId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/categories/{category_id}'.format(category_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

