# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.taxonomy import Taxonomy


pytestmark = pytest.mark.asyncio

async def test_taxonomies_list(client):
    """Test case for taxonomies_list

    List all taxonomies
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/taxonomies/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taxonomies_read(client):
    """Test case for taxonomies_read

    Retrieve a taxonomy
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/taxonomies/{taxonomy_id}'.format(taxonomy_id='taxonomy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

