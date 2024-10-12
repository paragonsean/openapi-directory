# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.shared_fill_map import SharedFillMap


pytestmark = pytest.mark.asyncio

async def test_shared_fillmap_get_id(client):
    """Test case for shared_fillmap_get_id

    FillMap: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/FillMap/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

