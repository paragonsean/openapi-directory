# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.public_channel_index import PublicChannelIndex
from openapi_server.models.public_channel_info_list import PublicChannelInfoList


pytestmark = pytest.mark.asyncio

async def test_get_channels(client):
    """Test case for get_channels

    The channel list for one country
    """
    headers = { 
        'Accept': 'application/json',
        'accept_encoding': ['accept_encoding_example'],
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/public/channels/{country_iso_code}'.format(country_iso_code='country_iso_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channels_index(client):
    """Test case for get_channels_index

    Get public channel index
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/public/channels/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

