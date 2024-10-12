# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sites_response import ListSitesResponse


pytestmark = pytest.mark.asyncio

async def test_list_sites(client):
    """Test case for list_sites

    ListSites
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/sites',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

