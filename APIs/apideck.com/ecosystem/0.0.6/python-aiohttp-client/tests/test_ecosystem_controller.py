# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_ecosystem_response import GetEcosystemResponse


pytestmark = pytest.mark.asyncio

async def test_ecosystems_one(client):
    """Test case for ecosystems_one

    Get ecosystem
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}'.format(ecosystem_id='ecosystem_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

