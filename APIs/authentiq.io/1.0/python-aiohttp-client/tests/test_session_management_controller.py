# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_authorize_iframe(client):
    """Test case for authorize_iframe

    Include a session iframe
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{client_id}/iframe'.format(client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

