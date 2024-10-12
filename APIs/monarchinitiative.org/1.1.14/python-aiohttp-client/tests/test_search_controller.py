# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autocomplete_results import AutocompleteResults
from openapi_server.models.lay_results import LayResults
from openapi_server.models.search_result import SearchResult


pytestmark = pytest.mark.asyncio

async def test_get_autocomplete(client):
    """Test case for get_autocomplete

    Returns list of matching concepts or entities using lexical search
    """
    params = [('fq', ['fq_example']),
                    ('category', ['category_example']),
                    ('prefix', ['prefix_example']),
                    ('include_eqs', False),
                    ('boost_fx', ['boost_fx_example']),
                    ('boost_q', ['boost_q_example']),
                    ('taxon', ['taxon_example']),
                    ('rows', 20),
                    ('start', '0'),
                    ('highlight_class', 'highlight_class_example'),
                    ('min_match', 'min_match_example'),
                    ('exclude_groups', False),
                    ('minimal_tokenizer', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/search/entity/autocomplete/{term}'.format(term='term_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_search_entities(client):
    """Test case for get_search_entities

    Returns list of matching concepts or entities using lexical search
    """
    params = [('fq', ['fq_example']),
                    ('category', ['category_example']),
                    ('prefix', ['prefix_example']),
                    ('include_eqs', False),
                    ('boost_fx', ['boost_fx_example']),
                    ('boost_q', ['boost_q_example']),
                    ('taxon', ['taxon_example']),
                    ('rows', 20),
                    ('start', '0'),
                    ('highlight_class', 'highlight_class_example'),
                    ('min_match', 'min_match_example'),
                    ('exclude_groups', False),
                    ('minimal_tokenizer', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/search/entity/{term}'.format(term='term_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_search_hpo_entities(client):
    """Test case for get_search_hpo_entities

    Returns list of matching concepts or entities using lexical search
    """
    params = [('rows', 10),
                    ('start', '0'),
                    ('phenotype_group', 'phenotype_group_example'),
                    ('phenotype_group_label', 'phenotype_group_label_example'),
                    ('anatomical_system', 'anatomical_system_example'),
                    ('anatomical_system_label', 'anatomical_system_label_example'),
                    ('highlight_class', 'highlight_class_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/search/entity/hpo-pl/{term}'.format(term='term_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

