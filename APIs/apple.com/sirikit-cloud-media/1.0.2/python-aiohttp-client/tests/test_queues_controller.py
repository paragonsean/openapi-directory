# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.play_media_request import PlayMediaRequest
from openapi_server.models.queue import Queue
from openapi_server.models.update_activity_request import UpdateActivityRequest
from openapi_server.models.update_activity_response import UpdateActivityResponse


pytestmark = pytest.mark.asyncio

async def test_play_media_on_queue(client):
    """Test case for play_media_on_queue

    playMedia
    """
    body = {"userActivity":{"userInfo":"{}","persistentIdentifier":"persistentIdentifier","activityType":"com.mediastreamingservice.playmedia","title":"title","version":"version"},"constraints":{"maximumQueueSegmentItemCount":126,"allowExplicitContent":True,"updateUserTasteProfile":True},"version":"version"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_applecloudextension_session_id': 'x_applecloudextension_session_id_example',
        'x_applecloudextension_retry_count': 3.4,
        'user_agent': 'user_agent_example',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='POST',
        path='/api/queues/playMedia',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_activity_on_queue(client):
    """Test case for update_activity_on_queue

    updateActivity
    """
    body = {"report":"local.playing.elapsed","nowPlaying":{"playbackSpeed":0.8008281904610115,"activityIdentifier":"activityIdentifier","queueIdentifier":"u104823q8201","contentIdentifier":"j15f8A3cuU0GG","offsetInMillis":10942},"userActivity":{"userInfo":"{}","persistentIdentifier":"persistentIdentifier","activityType":"com.mediastreamingservice.playmedia","title":"title","version":"version"},"constraints":{"maximumQueueSegmentItemCount":126,"allowExplicitContent":True,"updateUserTasteProfile":True},"version":"version","previouslyPlaying":{"playbackSpeed":0.8008281904610115,"activityIdentifier":"activityIdentifier","queueIdentifier":"u104823q8201","contentIdentifier":"j15f8A3cuU0GG","offsetInMillis":10942},"timestamp":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_applecloudextension_session_id': 'x_applecloudextension_session_id_example',
        'x_applecloudextension_retry_count': 3.4,
        'user_agent': 'user_agent_example',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='POST',
        path='/api/queues/updateActivity',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

