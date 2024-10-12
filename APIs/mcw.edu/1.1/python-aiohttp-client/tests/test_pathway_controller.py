# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pathway import Pathway


pytestmark = pytest.mark.asyncio

async def test_get_pathways_with_diagrams_for_category_using_get(client):
    """Test case for get_pathways_with_diagrams_for_category_using_get

    Return a list of pathways based on category provided
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/pathways/diagramsForCategory/{category}'.format(category='category_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_pathways_using_get(client):
    """Test case for search_pathways_using_get

    Return a list of pathways based on search term
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rgdws/pathways/diagrams/search/{search_string}'.format(search_string='search_string_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

