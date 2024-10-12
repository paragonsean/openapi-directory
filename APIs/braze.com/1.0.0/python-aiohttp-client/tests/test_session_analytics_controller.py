# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_app_sessions_by_time_0(client):
    """Test case for app_sessions_by_time_0

    App Sessions by Time
    """
    params = [('length', '14'),
                    ('unit', 'day'),
                    ('ending_at', '2018-06-28T23:59:59-5:00'),
                    ('app_id', '{{app_identifier}}'),
                    ('segment_id', '{{segment_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/sessions/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

