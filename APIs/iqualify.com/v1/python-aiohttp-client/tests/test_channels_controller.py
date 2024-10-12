# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.channel_required import ChannelRequired
from openapi_server.models.channel_response import ChannelResponse
from openapi_server.models.comment import Comment
from openapi_server.models.error import Error
from openapi_server.models.http_post import HttpPost
from openapi_server.models.offerings_offering_id_channels_channel_id_learners_post_request import OfferingsOfferingIdChannelsChannelIdLearnersPostRequest


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_channels_channel_id_comments_get(client):
    """Test case for offerings_offering_id_analytics_channels_channel_id_comments_get

    Find comments
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/channels/{channel_id}/comments'.format(offering_id='offering_id_example', channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_channels_channel_id_posts_get(client):
    """Test case for offerings_offering_id_analytics_channels_channel_id_posts_get

    Find posts
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/channels/{channel_id}/posts'.format(offering_id='offering_id_example', channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_channels_channel_id_replies_get(client):
    """Test case for offerings_offering_id_analytics_channels_channel_id_replies_get

    Find replies
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/channels/{channel_id}/replies'.format(offering_id='offering_id_example', channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_channels_channel_id_learners_delete(client):
    """Test case for offerings_offering_id_channels_channel_id_learners_delete

    Remove learners from a group channel
    """
    body = openapi_server.OfferingsOfferingIdChannelsChannelIdLearnersPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/offerings/{offering_id}/channels/{channel_id}/learners'.format(offering_id='offering_id_example', channel_id='channel_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_channels_channel_id_learners_get(client):
    """Test case for offerings_offering_id_channels_channel_id_learners_get

    Find learners in a group channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/channels/{channel_id}/learners'.format(offering_id='offering_id_example', channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_channels_channel_id_learners_post(client):
    """Test case for offerings_offering_id_channels_channel_id_learners_post

    Add learners to a group channel
    """
    body = openapi_server.OfferingsOfferingIdChannelsChannelIdLearnersPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/offerings/{offering_id}/channels/{channel_id}/learners'.format(offering_id='offering_id_example', channel_id='channel_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_channels_channel_id_patch(client):
    """Test case for offerings_offering_id_channels_channel_id_patch

    Update channel
    """
    body = {"isBroadcastOnly":True,"groupDiscussion":True,"privateSupport":True,"title":"title","group":{"autoAssign":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/offerings/{offering_id}/channels/{channel_id}'.format(offering_id='offering_id_example', channel_id='channel_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_channels_get(client):
    """Test case for offerings_offering_id_channels_get

    Find channels
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/channels'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_channels_post(client):
    """Test case for offerings_offering_id_channels_post

    Add channel
    """
    body = {"isBroadcastOnly":False,"title":"title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/offerings/{offering_id}/channels'.format(offering_id='offering_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

