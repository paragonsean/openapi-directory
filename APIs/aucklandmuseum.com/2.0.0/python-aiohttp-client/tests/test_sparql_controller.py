# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_sparql(client):
    """Test case for get_sparql

    Auckland Museum SPARQL endpoint
    """
    params = [('query', 'query_example'),
                    ('callback', 'callback'),
                    ('infer', True)]
    headers = { 
        'Accept': 'application/javascript',
    }
    response = await client.request(
        method='GET',
        path='/sparql',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_post_sparql(client):
    """Test case for post_sparql

    Auckland Museum SPARQL endpoint
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'query': 'query_example',
        'infer': True
        }
    response = await client.request(
        method='POST',
        path='/sparql',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

