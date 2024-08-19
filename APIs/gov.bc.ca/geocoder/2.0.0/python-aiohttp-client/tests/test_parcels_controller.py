# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_parcels_pids_site_id_output_format_get(client):
    """Test case for parcels_pids_site_id_output_format_get

    Get a comma-separated string of all pids for a given site
    """
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/parcels/pids/{site_id_output_format}'.format(site_id='site_id_example', output_format=json),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

