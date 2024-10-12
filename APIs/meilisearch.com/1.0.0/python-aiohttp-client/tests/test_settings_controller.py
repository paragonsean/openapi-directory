# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_faceting_request import UpdateFacetingRequest
from openapi_server.models.update_pagination_request import UpdatePaginationRequest
from openapi_server.models.update_settings_request import UpdateSettingsRequest
from openapi_server.models.update_synonyms_request import UpdateSynonymsRequest
from openapi_server.models.update_typo_tolerance_request import UpdateTypoToleranceRequest


pytestmark = pytest.mark.asyncio

async def test_get_all_settings(client):
    """Test case for get_all_settings

    Get all settings
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_displayed_attributes(client):
    """Test case for get_displayed_attributes

    Get displayed attributes
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings/displayed-attributes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_distinct_attribute(client):
    """Test case for get_distinct_attribute

    Get distinct attribute
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings/distinct-attribute',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_faceting(client):
    """Test case for get_faceting

    Get faceting
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings/faceting',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_filterable_attributes(client):
    """Test case for get_filterable_attributes

    Get filterable attributes
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings/filterable-attributes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pagination(client):
    """Test case for get_pagination

    Get pagination
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings/pagination',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ranking_rules(client):
    """Test case for get_ranking_rules

    Get ranking rules
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings/ranking-rules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_searchable_attributes(client):
    """Test case for get_searchable_attributes

    Get searchable attributes
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings/searchable-attributes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sortable_attributes(client):
    """Test case for get_sortable_attributes

    Get sortable attributes
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings/sortable-attributes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stop_words(client):
    """Test case for get_stop_words

    Get stop-words
    """
    body = ["the"]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings/stop-words',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_synonyms(client):
    """Test case for get_synonyms

    Get synonyms
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings/synonyms',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_typo_tolerance(client):
    """Test case for get_typo_tolerance

    Get typo-tolerance
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/settings/typo-tolerance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_all_settings(client):
    """Test case for reset_all_settings

    Reset all settings
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_displayed_attributes(client):
    """Test case for reset_displayed_attributes

    Reset displayed attributes
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings/displayed-attributes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_distinct_attribute(client):
    """Test case for reset_distinct_attribute

    Reset distinct attribute
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings/distinct-attribute',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_faceting(client):
    """Test case for reset_faceting

    Reset faceting
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings/faceting',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_filterable_attributes(client):
    """Test case for reset_filterable_attributes

    Reset filterable attributes
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings/filterable-attributes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_pagination(client):
    """Test case for reset_pagination

    Reset pagination
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings/pagination',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_ranking_rules(client):
    """Test case for reset_ranking_rules

    Reset ranking rules
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings/ranking-rules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_searchable_attributes(client):
    """Test case for reset_searchable_attributes

    Reset searchable attributes
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings/searchable-attributes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_sortable_attributes(client):
    """Test case for reset_sortable_attributes

    Reset sortable attributes
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings/sortable-attributes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_stop_words(client):
    """Test case for reset_stop_words

    Reset stop-words
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings/stop-words',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_reset_synonyms(client):
    """Test case for reset_synonyms

    Reset synonyms
    """
    headers = { 
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings/synonyms',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_typo_tolerance(client):
    """Test case for reset_typo_tolerance

    Reset typo-tolerance
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/settings/typo-tolerance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_displayed_attributes(client):
    """Test case for update_displayed_attributes

    Update displayed attributes
    """
    body = ["title"]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/indexes/books/settings/displayed-attributes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_update_distinct_attribute(client):
    """Test case for update_distinct_attribute

    Update distinct attribute
    """
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='PUT',
        path='/indexes/books/settings/distinct-attribute',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_faceting(client):
    """Test case for update_faceting

    Update faceting
    """
    body = {"maxValuesPerFacet":3000}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/indexes/books/settings/faceting',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_filterable_attributes(client):
    """Test case for update_filterable_attributes

    Update filterable attributes
    """
    body = ["genre"]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/indexes/books/settings/filterable-attributes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_pagination(client):
    """Test case for update_pagination

    Update pagination
    """
    body = {"maxTotalHits":2000}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/indexes/books/settings/pagination',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_ranking_rules(client):
    """Test case for update_ranking_rules

    Update ranking rules
    """
    body = ["typo"]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/indexes/books/settings/ranking-rules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_searchable_attributes(client):
    """Test case for update_searchable_attributes

    Update searchable attributes
    """
    body = ["title","author"]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/indexes/books/settings/searchable-attributes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_settings(client):
    """Test case for update_settings

    Update settings
    """
    body = {"displayedAttributes":["title","author","genre","price"],"filterableAttributes":["genre","price"],"searchableAttributes":["title","author"],"sortableAttributes":["price"],"stopWords":["of","the"]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/indexes/books/settings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_sortable_attributes(client):
    """Test case for update_sortable_attributes

    Update sortable attributes
    """
    body = ["price"]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/indexes/books/settings/sortable-attributes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_stop_words(client):
    """Test case for update_stop_words

    Update stop-words
    """
    body = ["the","of"]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/indexes/books/settings/stop-words',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_synonyms(client):
    """Test case for update_synonyms

    Update synonyms
    """
    body = {"harry potter":["hp"],"hp":["harry potter"]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/indexes/books/settings/synonyms',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_typo_tolerance(client):
    """Test case for update_typo_tolerance

    Update typo-tolerance
    """
    body = {"disableOnAttributes":["genre"],"disableOnWords":["Prince"],"minWordSizeForTypos":{"oneTypo":2,"twoTypos":11}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/indexes/books/settings/typo-tolerance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

