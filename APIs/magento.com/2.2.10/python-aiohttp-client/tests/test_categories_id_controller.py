# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_category_repository_v1_save_post_request import CatalogCategoryRepositoryV1SavePostRequest
from openapi_server.models.catalog_data_category_interface import CatalogDataCategoryInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_category_repository_v1_save_put(client):
    """Test case for catalog_category_repository_v1_save_put

    categories/{id}
    """
    body = openapi_server.CatalogCategoryRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/categories/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

