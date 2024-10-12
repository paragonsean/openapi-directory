# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_entity_set_anatomy_slimmer(client):
    """Test case for get_entity_set_anatomy_slimmer

    For a given gene(s), summarize its annotations over a defined set of slim
    """
    params = [('subject', ['subject_example']),
                    ('slim', ['slim_example']),
                    ('exclude_automatic_assertions', False),
                    ('rows', 100),
                    ('start', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentityset/slimmer/anatomy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_entity_set_function_slimmer(client):
    """Test case for get_entity_set_function_slimmer

    For a given gene(s), summarize its annotations over a defined set of slim
    """
    params = [('relationship_type', acts_upstream_of_or_within),
                    ('subject', ['subject_example']),
                    ('slim', ['slim_example']),
                    ('exclude_automatic_assertions', False),
                    ('rows', 100),
                    ('start', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentityset/slimmer/function',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_entity_set_phenotype_slimmer(client):
    """Test case for get_entity_set_phenotype_slimmer

    For a given gene(s), summarize its annotations over a defined set of slim
    """
    params = [('subject', ['subject_example']),
                    ('slim', ['slim_example']),
                    ('exclude_automatic_assertions', False),
                    ('rows', 100),
                    ('start', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/bioentityset/slimmer/phenotype',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

