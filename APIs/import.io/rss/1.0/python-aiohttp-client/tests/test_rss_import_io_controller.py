# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError


pytestmark = pytest.mark.asyncio

async def test_extractor_extractor_id_runs_get(client):
    """Test case for extractor_extractor_id_runs_get

    Get a feed of the runs performed on an extractor
    """
    headers = { 
        'Accept': 'application/xml',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/extractor/{extractor_id}/runs'.format(extractor_id='extractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

