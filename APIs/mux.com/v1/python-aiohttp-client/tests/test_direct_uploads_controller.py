# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_upload_request import CreateUploadRequest
from openapi_server.models.list_uploads_response import ListUploadsResponse
from openapi_server.models.upload_response import UploadResponse


pytestmark = pytest.mark.asyncio

async def test_cancel_direct_upload(client):
    """Test case for cancel_direct_upload

    Cancel a direct upload
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/video/v1/uploads/{upload_id}/cancel'.format(upload_id='abcd1234'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_direct_upload(client):
    """Test case for create_direct_upload

    Create a new direct upload URL
    """
    body = {"cors_origin":"cors_origin","test":True,"new_asset_settings":{"input":[{"generated_subtitles":[{"language_code":"en","name":"name","passthrough":"passthrough"},{"language_code":"en","name":"name","passthrough":"passthrough"}],"language_code":"language_code","overlay_settings":{"horizontal_margin":"horizontal_margin","vertical_align":"top","horizontal_align":"left","width":"width","opacity":"opacity","height":"height","vertical_margin":"vertical_margin"},"start_time":6.027456183070403,"text_type":"subtitles","end_time":0.8008281904610115,"name":"name","passthrough":"passthrough","closed_captions":True,"type":"video","url":"url"},{"generated_subtitles":[{"language_code":"en","name":"name","passthrough":"passthrough"},{"language_code":"en","name":"name","passthrough":"passthrough"}],"language_code":"language_code","overlay_settings":{"horizontal_margin":"horizontal_margin","vertical_align":"top","horizontal_align":"left","width":"width","opacity":"opacity","height":"height","vertical_margin":"vertical_margin"},"start_time":6.027456183070403,"text_type":"subtitles","end_time":0.8008281904610115,"name":"name","passthrough":"passthrough","closed_captions":True,"type":"video","url":"url"}],"test":True,"max_resolution_tier":"1080p","encoding_tier":"smart","normalize_audio":False,"passthrough":"passthrough","playback_policy":["public","public"],"master_access":"none","mp4_support":"none","per_title_encode":True},"timeout":48489}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/uploads',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_direct_upload(client):
    """Test case for get_direct_upload

    Retrieve a single direct upload's info
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/uploads/{upload_id}'.format(upload_id='abcd1234'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_direct_uploads(client):
    """Test case for list_direct_uploads

    List direct uploads
    """
    params = [('limit', 25),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/uploads',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

