# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association import Association


pytestmark = pytest.mark.asyncio

async def test_get_dl_query(client):
    """Test case for get_dl_query

    Placeholder - use OWLery for now
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/owl/ontology/dlquery/{query}'.format(query='query_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sparql_query(client):
    """Test case for get_sparql_query

    Placeholder - use direct SPARQL endpoint for now
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/owl/ontology/sparql/{query}'.format(query='query_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

