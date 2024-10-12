# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_setlist import JsonSetlist


pytestmark = pytest.mark.asyncio

async def test_resource10_setlist_version_version_id_get_setlist_version_get(client):
    """Test case for resource10_setlist_version_version_id_get_setlist_version_get

    .
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/1.0/setlist/version/{version_id}'.format(version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

