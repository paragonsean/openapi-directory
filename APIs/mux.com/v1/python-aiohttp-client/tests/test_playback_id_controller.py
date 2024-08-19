# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_asset_or_live_stream_id_response import GetAssetOrLiveStreamIdResponse


pytestmark = pytest.mark.asyncio

async def test_get_asset_or_livestream_id(client):
    """Test case for get_asset_or_livestream_id

    Retrieve an Asset or Live Stream ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/playback-ids/{playback_id}'.format(playback_id='playback_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

