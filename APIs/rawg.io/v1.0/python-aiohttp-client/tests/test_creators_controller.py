# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.creators_list200_response import CreatorsList200Response
from openapi_server.models.person_single import PersonSingle


pytestmark = pytest.mark.asyncio

async def test_creators_list(client):
    """Test case for creators_list

    Get a list of game creators.
    """
    params = [('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/creators',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_creators_read(client):
    """Test case for creators_read

    Get details of the creator.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/creators/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

