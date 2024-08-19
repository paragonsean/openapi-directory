# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.intact_interactions import IntactInteractions


pytestmark = pytest.mark.asyncio

async def test_get_intact_using_get(client):
    """Test case for get_intact_using_get

    Molecular Interactions collected from IntAct
    """
    params = [('accession', ['accession_example']),
                    ('confidence', 3.4),
                    ('gene', ['gene_example']),
                    ('limit', 10),
                    ('page', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/intact',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

