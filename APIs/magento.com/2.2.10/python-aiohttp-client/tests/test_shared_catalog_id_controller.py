# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.shared_catalog_shared_catalog_repository_v1_save_post_request import SharedCatalogSharedCatalogRepositoryV1SavePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_shared_catalog_shared_catalog_repository_v1_save_put(client):
    """Test case for shared_catalog_shared_catalog_repository_v1_save_put

    sharedCatalog/{id}
    """
    body = openapi_server.SharedCatalogSharedCatalogRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/sharedCatalog/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

