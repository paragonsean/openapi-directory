# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.shared_effects import SharedEffects


pytestmark = pytest.mark.asyncio

async def test_shared_effects_get_id(client):
    """Test case for shared_effects_get_id

    Effects: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Shared/Effects/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

