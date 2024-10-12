# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_metadata_get(client):
    """Test case for metadata_get

    This endpoint returns metadata for the most recent data loads of SAM and FPDS data
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

