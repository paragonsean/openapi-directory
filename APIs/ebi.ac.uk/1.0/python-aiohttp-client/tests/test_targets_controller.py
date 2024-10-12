# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.targets import Targets


pytestmark = pytest.mark.asyncio

async def test_get_targets_using_get(client):
    """Test case for get_targets_using_get

    Get ChEMBL targets
    """
    params = [('accession', ['accession_example']),
                    ('limit', 10),
                    ('page', 0),
                    ('targetIds', ['target_ids_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/targets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

