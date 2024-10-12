# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channels import Channels
from openapi_server.models.channels_post_request import ChannelsPostRequest
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.several_channels_patch_request import SeveralChannelsPatchRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_channels_patch(client):
    """Test case for channels_patch

    Update/create a channel
    """
    body = openapi_server.ChannelsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/channels/{code}'.format(code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_channels_post(client):
    """Test case for channels_post

    Create a new channel
    """
    body = openapi_server.ChannelsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/channels',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channels(client):
    """Test case for get_channels

    Get a list of channels
    """
    params = [('page', 1),
                    ('limit', 10),
                    ('with_count', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channels_code(client):
    """Test case for get_channels_code

    Get a channel
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/channels/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_several_channels_patch(client):
    """Test case for several_channels_patch

    Update/create several channels
    """
    body = openapi_server.SeveralChannelsPatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/channels',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

