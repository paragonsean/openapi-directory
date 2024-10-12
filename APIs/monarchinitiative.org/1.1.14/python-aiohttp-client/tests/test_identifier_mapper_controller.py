# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association import Association


pytestmark = pytest.mark.asyncio

async def test_get_identifier_mapper(client):
    """Test case for get_identifier_mapper

    TODO maps a list of identifiers from a source to a target
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/identifier/mapper/{source}/{target}'.format(source='source_example', target='target_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

