# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_setlist import JsonSetlist


pytestmark = pytest.mark.asyncio

async def test_resource10_setlist_setlist_id_get_setlist_get(client):
    """Test case for resource10_setlist_setlist_id_get_setlist_get

    .
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/1.0/setlist/{setlist_id}'.format(setlist_id='setlist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

