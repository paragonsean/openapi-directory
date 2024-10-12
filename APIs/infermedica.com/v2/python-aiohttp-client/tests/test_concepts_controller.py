# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.concept_item_model_public import ConceptItemModelPublic


pytestmark = pytest.mark.asyncio

async def test_get_concept(client):
    """Test case for get_concept

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/concepts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_concepts(client):
    """Test case for get_concepts

    
    """
    params = [('ids', 'ids_example'),
                    ('types', 'types_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/concepts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

