# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.video_v1_recording_settings import VideoV1RecordingSettings


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_recording_settings(client):
    """Test case for create_recording_settings

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'aws_credentials_sid': 'aws_credentials_sid_example',
        'aws_s3_url': 'aws_s3_url_example',
        'aws_storage_enabled': True,
        'encryption_enabled': True,
        'encryption_key_sid': 'encryption_key_sid_example',
        'friendly_name': 'friendly_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/RecordingSettings/Default',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_recording_settings(client):
    """Test case for fetch_recording_settings

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/RecordingSettings/Default',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

