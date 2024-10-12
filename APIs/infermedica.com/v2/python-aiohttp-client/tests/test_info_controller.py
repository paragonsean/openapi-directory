# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.info_public import InfoPublic


pytestmark = pytest.mark.asyncio

async def test_get_database_info(client):
    """Test case for get_database_info

    Get database information
    """
    params = [('age.value', 18),
                    ('age.unit', year)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

