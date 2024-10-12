# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_core_dto_click_stream_hit_list_page import ApiCoreDtoClickStreamHitListPage


pytestmark = pytest.mark.asyncio

async def test_hits_get_hits(client):
    """Test case for hits_get_hits

    Retrieve the list of events related to this account.
    """
    params = [('timeframe', 'timeframe_example'),
                    ('limit', 56),
                    ('offset', 'offset_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/hits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

