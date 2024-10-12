# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_series_summary_v1 import EventSeriesSummaryV1


pytestmark = pytest.mark.asyncio

async def test_query_event_series_by_id_v1(client):
    """Test case for query_event_series_by_id_v1

    Get all events and relevant information associated with an event series ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/event_series/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

