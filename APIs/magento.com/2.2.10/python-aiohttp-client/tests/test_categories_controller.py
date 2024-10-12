# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_category_repository_v1_save_post_request import CatalogCategoryRepositoryV1SavePostRequest
from openapi_server.models.catalog_data_category_interface import CatalogDataCategoryInterface
from openapi_server.models.catalog_data_category_tree_interface import CatalogDataCategoryTreeInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_category_management_v1_get_tree_get(client):
    """Test case for catalog_category_management_v1_get_tree_get

    categories
    """
    params = [('rootCategoryId', 56),
                    ('depth', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_category_repository_v1_save_post(client):
    """Test case for catalog_category_repository_v1_save_post

    categories
    """
    body = openapi_server.CatalogCategoryRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/categories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

