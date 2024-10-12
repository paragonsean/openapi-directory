# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association import Association


pytestmark = pytest.mark.asyncio

async def test_get_individual(client):
    """Test case for get_individual

    Returns list of matches
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/individual/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pedigree(client):
    """Test case for get_pedigree

    Returns list of matches
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/individual/pedigree/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

