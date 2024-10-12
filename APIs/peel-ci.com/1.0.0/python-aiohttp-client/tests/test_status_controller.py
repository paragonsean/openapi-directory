# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_statuses(client):
    """Test case for get_statuses

    Gets the last 100 statuses for this show.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/status/{show_id}'.format(show_id='show_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

