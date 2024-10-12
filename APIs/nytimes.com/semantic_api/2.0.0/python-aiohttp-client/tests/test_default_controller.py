# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.name_concept_type_specific_concept_json_get200_response import NameConceptTypeSpecificConceptJsonGet200Response
from openapi_server.models.search_json_get200_response import SearchJsonGet200Response


pytestmark = pytest.mark.asyncio

async def test_name_concept_type_specific_concept_json_get(client):
    """Test case for name_concept_type_specific_concept_json_get

    
    """
    params = [('fields', 'fields_example'),
                    ('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/semantic/v2/concept/name/{concept_type}/{specific_concept_jso}'.format(concept_type='concept_type_example', specific_concept='specific_concept_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_json_get(client):
    """Test case for search_json_get

    
    """
    params = [('query', 'query_example'),
                    ('offset', 10),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/semantic/v2/concept/search.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

