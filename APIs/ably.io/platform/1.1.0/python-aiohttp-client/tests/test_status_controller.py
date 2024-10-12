# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel_details import ChannelDetails
from openapi_server.models.error import Error
from openapi_server.models.get_metadata_of_all_channels2_xx_response import GetMetadataOfAllChannels2XXResponse
from openapi_server.models.presence_message import PresenceMessage


pytestmark = pytest.mark.asyncio

async def test_get_metadata_of_all_channels(client):
    """Test case for get_metadata_of_all_channels

    Enumerate all active channels of the application
    """
    params = [('format', 'format_example'),
                    ('limit', 100),
                    ('prefix', 'prefix_example'),
                    ('by', 'by_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_metadata_of_channel(client):
    """Test case for get_metadata_of_channel

    Get metadata of a channel
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_presence_of_channel(client):
    """Test case for get_presence_of_channel

    Get presence of a channel
    """
    params = [('format', 'format_example'),
                    ('clientId', 'client_id_example'),
                    ('connectionId', 'connection_id_example'),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/presence'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

