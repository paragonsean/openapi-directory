# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset_response import AssetResponse
from openapi_server.models.create_asset_request import CreateAssetRequest
from openapi_server.models.create_playback_id_request import CreatePlaybackIDRequest
from openapi_server.models.create_playback_id_response import CreatePlaybackIDResponse
from openapi_server.models.create_track_request import CreateTrackRequest
from openapi_server.models.create_track_response import CreateTrackResponse
from openapi_server.models.get_asset_input_info_response import GetAssetInputInfoResponse
from openapi_server.models.get_asset_playback_id_response import GetAssetPlaybackIDResponse
from openapi_server.models.list_assets_response import ListAssetsResponse
from openapi_server.models.update_asset_mp4_support_request import UpdateAssetMP4SupportRequest
from openapi_server.models.update_asset_master_access_request import UpdateAssetMasterAccessRequest
from openapi_server.models.update_asset_request import UpdateAssetRequest


pytestmark = pytest.mark.asyncio

async def test_create_asset(client):
    """Test case for create_asset

    Create an asset
    """
    body = {"input":[{"generated_subtitles":[{"language_code":"en","name":"name","passthrough":"passthrough"},{"language_code":"en","name":"name","passthrough":"passthrough"}],"language_code":"language_code","overlay_settings":{"horizontal_margin":"horizontal_margin","vertical_align":"top","horizontal_align":"left","width":"width","opacity":"opacity","height":"height","vertical_margin":"vertical_margin"},"start_time":6.027456183070403,"text_type":"subtitles","end_time":0.8008281904610115,"name":"name","passthrough":"passthrough","closed_captions":True,"type":"video","url":"url"},{"generated_subtitles":[{"language_code":"en","name":"name","passthrough":"passthrough"},{"language_code":"en","name":"name","passthrough":"passthrough"}],"language_code":"language_code","overlay_settings":{"horizontal_margin":"horizontal_margin","vertical_align":"top","horizontal_align":"left","width":"width","opacity":"opacity","height":"height","vertical_margin":"vertical_margin"},"start_time":6.027456183070403,"text_type":"subtitles","end_time":0.8008281904610115,"name":"name","passthrough":"passthrough","closed_captions":True,"type":"video","url":"url"}],"test":True,"max_resolution_tier":"1080p","encoding_tier":"smart","normalize_audio":False,"passthrough":"passthrough","playback_policy":["public","public"],"master_access":"none","mp4_support":"none","per_title_encode":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/assets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_asset_playback_id(client):
    """Test case for create_asset_playback_id

    Create a playback ID
    """
    body = {"policy":"public"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/assets/{asset_id}/playback-ids'.format(asset_id='asset_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_asset_track(client):
    """Test case for create_asset_track

    Create an asset track
    """
    body = {"language_code":"language_code","text_type":"subtitles","name":"name","passthrough":"passthrough","closed_captions":True,"type":"text","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/assets/{asset_id}/tracks'.format(asset_id='asset_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_asset(client):
    """Test case for delete_asset

    Delete an asset
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/video/v1/assets/{asset_id}'.format(asset_id='asset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_asset_playback_id(client):
    """Test case for delete_asset_playback_id

    Delete a playback ID
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/video/v1/assets/{asset_id}/playback-ids/{playback_id}'.format(asset_id='asset_id_example', playback_id='playback_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_asset_track(client):
    """Test case for delete_asset_track

    Delete an asset track
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/video/v1/assets/{asset_id}/tracks/{track_id}'.format(asset_id='asset_id_example', track_id='track_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset(client):
    """Test case for get_asset

    Retrieve an asset
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/assets/{asset_id}'.format(asset_id='asset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset_input_info(client):
    """Test case for get_asset_input_info

    Retrieve asset input info
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/assets/{asset_id}/input-info'.format(asset_id='asset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset_playback_id(client):
    """Test case for get_asset_playback_id

    Retrieve a playback ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/assets/{asset_id}/playback-ids/{playback_id}'.format(asset_id='asset_id_example', playback_id='playback_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_assets(client):
    """Test case for list_assets

    List assets
    """
    params = [('limit', 25),
                    ('page', 1),
                    ('live_stream_id', 'live_stream_id_example'),
                    ('upload_id', 'upload_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/assets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_asset(client):
    """Test case for update_asset

    Update an Asset
    """
    body = {"passthrough":"passthrough"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/video/v1/assets/{asset_id}'.format(asset_id='asset_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_asset_master_access(client):
    """Test case for update_asset_master_access

    Update master access
    """
    body = {"master_access":"temporary"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/video/v1/assets/{asset_id}/master-access'.format(asset_id='asset_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_asset_mp4_support(client):
    """Test case for update_asset_mp4_support

    Update MP4 support
    """
    body = {"mp4_support":"standard"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/video/v1/assets/{asset_id}/mp4-support'.format(asset_id='asset_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

