# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_app_catalogs_mapping_schema_product200_response import GetAppCatalogsMappingSchemaProduct200Response
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_delete_app_catalogs_mapping_schema_product(client):
    """Test case for delete_app_catalogs_mapping_schema_product

    Delete the product mapping schema related to a catalog
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/catalogs/{id}/mapping-schemas/product'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_app_catalogs_mapping_schema_product(client):
    """Test case for get_app_catalogs_mapping_schema_product

    Get the product mapping schema related to a catalog
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/catalogs/{id}/mapping-schemas/product'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_put_app_catalogs_mapping_schema_product(client):
    """Test case for put_app_catalogs_mapping_schema_product

    Create or update the product mapping schema related to a catalog
    """
    body = openapi_server.GetAppCatalogsMappingSchemaProduct200Response()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/rest/v1/catalogs/{id}/mapping-schemas/product'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

