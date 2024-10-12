# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.game_summary_model import GameSummaryModel
from openapi_server.models.message_model import MessageModel


pytestmark = pytest.mark.asyncio

async def test_get_game_summary_using_get(client):
    """Test case for get_game_summary_using_get

    getGameSummary
    """
    params = [('stage', 'stage_example'),
                    ('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/notifications/summary'.format(api_key='api_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

