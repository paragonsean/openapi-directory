# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_facets(client):
    """Test case for facets

    View the facet information corresponding to a search
    """
    params = [('searchTerms', 'search_terms_example'),
                    ('count', 25),
                    ('startIndex', 1),
                    ('spatial', '-180.0,-90.0,180.0,90.0'),
                    ('sortKeys', score,,desc),
                    ('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20'),
                    ('facetFilters', 'facet_filters_example'),
                    ('source', NSIDC)]
    headers = { 
        'Accept': 'application/nsidcfacets+xml',
    }
    response = await client.request(
        method='GET',
        path='/api/dataset/2/Facets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id(client):
    """Test case for id

    Suggest search terms based on a partial query
    """
    params = [('q', 'q_example'),
                    ('source', NSIDC)]
    headers = { 
        'Accept': 'application/x-suggestions+json',
    }
    response = await client.request(
        method='GET',
        path='/api/dataset/2/suggest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_open_search(client):
    """Test case for open_search

    Search documents using the OpenSearch 1.1 Specification
    """
    params = [('searchTerms', 'search_terms_example'),
                    ('count', 25),
                    ('startIndex', 1),
                    ('spatial', '-180.0,-90.0,180.0,90.0'),
                    ('sortKeys', score,,desc),
                    ('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20'),
                    ('facetFilters', 'facet_filters_example'),
                    ('source', NSIDC)]
    headers = { 
        'Accept': 'application/atom+xml',
    }
    response = await client.request(
        method='GET',
        path='/api/dataset/2/OpenSearch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_opensearch_description(client):
    """Test case for opensearch_description

    Describes the web interface of NSIDC's data search engine
    """
    headers = { 
        'Accept': 'application/opensearchdescription+xml',
    }
    response = await client.request(
        method='GET',
        path='/api/dataset/2/OpenSearchDescription',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

