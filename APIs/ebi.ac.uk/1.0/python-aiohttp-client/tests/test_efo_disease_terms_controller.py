# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.efo_entities import EFOEntities


pytestmark = pytest.mark.asyncio

async def test_get_efo_using_get(client):
    """Test case for get_efo_using_get

    Get EFO diseases data
    """
    params = [('doid', ['doid_example']),
                    ('label', ['label_example']),
                    ('limit', 10),
                    ('mesh', ['mesh_example']),
                    ('oboId', ['obo_id_example']),
                    ('omimId', ['omim_id_example']),
                    ('page', 0),
                    ('synonym', ['synonym_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/efo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

