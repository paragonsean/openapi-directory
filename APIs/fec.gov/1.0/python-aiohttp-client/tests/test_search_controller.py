# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.candidate_search_list import CandidateSearchList
from openapi_server.models.committee_search_list import CommitteeSearchList


pytestmark = pytest.mark.asyncio

async def test_names_candidates_get(client):
    """Test case for names_candidates_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('q', ['q_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/names/candidates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_committees_get(client):
    """Test case for names_committees_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('q', ['q_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/names/committees/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

