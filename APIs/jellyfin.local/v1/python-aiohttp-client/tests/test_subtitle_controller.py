# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.font_file import FontFile
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.remote_subtitle_info import RemoteSubtitleInfo
from openapi_server.models.upload_subtitle_dto import UploadSubtitleDto


pytestmark = pytest.mark.asyncio

async def test_delete_subtitle(client):
    """Test case for delete_subtitle

    Deletes an external subtitle file.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Videos/{item_id}/Subtitles/{index}'.format(item_id='item_id_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_remote_subtitles(client):
    """Test case for download_remote_subtitles

    Downloads a remote subtitle.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/{item_id}/RemoteSearch/Subtitles/{subtitle_id}'.format(item_id='item_id_example', subtitle_id='subtitle_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fallback_font(client):
    """Test case for get_fallback_font

    Gets a fallback font file.
    """
    headers = { 
        'Accept': 'font/*',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/FallbackFont/Fonts/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fallback_font_list(client):
    """Test case for get_fallback_font_list

    Gets a list of available fallback font files.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/FallbackFont/Fonts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_subtitles(client):
    """Test case for get_remote_subtitles

    Gets the remote subtitles.
    """
    headers = { 
        'Accept': 'text/*',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Providers/Subtitles/Subtitles/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subtitle(client):
    """Test case for get_subtitle

    Gets subtitles in a specified format.
    """
    params = [('endPositionTicks', 56),
                    ('copyTimestamps', False),
                    ('addVttTimeMap', False),
                    ('startPositionTicks', 0)]
    headers = { 
        'Accept': 'text/*',
    }
    response = await client.request(
        method='GET',
        path='/Videos/{item_id}/{media_source_id}/Subtitles/{index}/Stream.{format}'.format(item_id='item_id_example', media_source_id='media_source_id_example', index=56, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subtitle_playlist(client):
    """Test case for get_subtitle_playlist

    Gets an HLS subtitle playlist.
    """
    params = [('segmentLength', 56)]
    headers = { 
        'Accept': 'application/x-mpegURL',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Videos/{item_id}/{media_source_id}/Subtitles/{index}/subtitles.m3u8'.format(item_id='item_id_example', index=56, media_source_id='media_source_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subtitle_with_ticks(client):
    """Test case for get_subtitle_with_ticks

    Gets subtitles in a specified format.
    """
    params = [('endPositionTicks', 56),
                    ('copyTimestamps', False),
                    ('addVttTimeMap', False)]
    headers = { 
        'Accept': 'text/*',
    }
    response = await client.request(
        method='GET',
        path='/Videos/{item_id}/{media_source_id}/Subtitles/{index}/{start_position_ticks}/Stream.{format}'.format(item_id='item_id_example', media_source_id='media_source_id_example', index=56, start_position_ticks=56, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_remote_subtitles(client):
    """Test case for search_remote_subtitles

    Search remote subtitles.
    """
    params = [('isPerfectMatch', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/RemoteSearch/Subtitles/{language}'.format(item_id='item_id_example', language='language_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_upload_subtitle(client):
    """Test case for upload_subtitle

    Upload an external subtitle file.
    """
    body = {"Format":"Format","IsForced":True,"Language":"Language","Data":"Data"}
    headers = { 
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/Videos/{item_id}/Subtitles'.format(item_id='item_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

