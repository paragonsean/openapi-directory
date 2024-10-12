# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.taxonomy_attractions200_response import TaxonomyAttractions200Response
from openapi_server.models.taxonomy_attractions_request import TaxonomyAttractionsRequest
from openapi_server.models.taxonomy_categories200_response import TaxonomyCategories200Response
from openapi_server.models.taxonomy_destinations200_response import TaxonomyDestinations200Response


pytestmark = pytest.mark.asyncio

async def test_taxonomy_attractions(client):
    """Test case for taxonomy_attractions

    /taxonomy/attractions
    """
    body = {"destId":684,"sortOrder":"SEO_PUBLISHED_DATE_D","topX":"1-3"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/taxonomy/attractions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taxonomy_categories(client):
    """Test case for taxonomy_categories

    /taxonomy/categories
    """
    params = [('destId', 684)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/taxonomy/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taxonomy_destinations(client):
    """Test case for taxonomy_destinations

    /taxonomy/destinations
    """
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/taxonomy/destinations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

