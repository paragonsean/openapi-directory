# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_system_pub_facets_category_category_id_get200_response_inner import ApiCatalogSystemPubFacetsCategoryCategoryIdGet200ResponseInner
from openapi_server.models.facetscategory200_response import Facetscategory200Response


pytestmark = pytest.mark.asyncio

async def test_api_catalog_system_pub_facets_category_category_id_get(client):
    """Test case for api_catalog_system_pub_facets_category_category_id_get

    Get Category Facets
    """
    params = [('_from', '1'),
                    ('_to', '50')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/facets/category/{category_id}'.format(category_id='1'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_facetscategory(client):
    """Test case for facetscategory

    Search by Store Facets
    """
    params = [('map', 'c'),
                    ('_from', '1'),
                    ('_to', '50')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/facets/search/{term}'.format(term='2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

