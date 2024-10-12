# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.recordings_list_for_training import RecordingsListForTraining


pytestmark = pytest.mark.asyncio

async def test_get_recording_download_by_id(client):
    """Test case for get_recording_download_by_id

    Get Download for Online Recordings
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/trainings/{training_key}/recordings/{recording_id}'.format(training_key=56, recording_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recordings_for_training(client):
    """Test case for get_recordings_for_training

    Get Online Recordings for Training
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/trainings/{training_key}/recordings'.format(training_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

