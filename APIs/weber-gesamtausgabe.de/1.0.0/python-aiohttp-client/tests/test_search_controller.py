# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_search_entity_get(client):
    """Test case for search_entity_get

    Search for a WeGA entity
    """
    params = [('docType', ['doc_type_example']),
                    ('q', 'q_example'),
                    ('offset', 1),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/exist/apps/WeGA-WebApp/api/v1/search/entity',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

