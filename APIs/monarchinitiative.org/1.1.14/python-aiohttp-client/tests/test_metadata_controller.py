# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_metadata_for_datasets(client):
    """Test case for get_metadata_for_datasets

    Get metadata for all datasets from SciGraph
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/metadata/datasets',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

