# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.shared_catalog_data_shared_catalog_interface import SharedCatalogDataSharedCatalogInterface


pytestmark = pytest.mark.asyncio

async def test_shared_catalog_shared_catalog_repository_v1_delete_by_id_delete(client):
    """Test case for shared_catalog_shared_catalog_repository_v1_delete_by_id_delete

    sharedCatalog/{sharedCatalogId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/sharedCatalog/{shared_catalog_id}'.format(shared_catalog_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_catalog_shared_catalog_repository_v1_get_get(client):
    """Test case for shared_catalog_shared_catalog_repository_v1_get_get

    sharedCatalog/{sharedCatalogId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/sharedCatalog/{shared_catalog_id}'.format(shared_catalog_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

