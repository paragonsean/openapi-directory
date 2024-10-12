# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.music_export_error_response import MusicExportErrorResponse
from openapi_server.models.music_export_job import MusicExportJob
from openapi_server.models.music_export_preferences import MusicExportPreferences
from openapi_server.models.music_export_preferences_response import MusicExportPreferencesResponse
from openapi_server.models.music_export_success import MusicExportSuccess


pytestmark = pytest.mark.asyncio

async def test_delete_music_preferences_export(client):
    """Test case for delete_music_preferences_export

    Music Export Preferences
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/my/music/preferences/export',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_music_preferences_export_vendor(client):
    """Test case for delete_music_preferences_export_vendor

    Music Export Vendor Preferences
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/my/music/preferences/export/{vendor}'.format(vendor='vendor_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_export(client):
    """Test case for get_music_export

    Music Exports
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/music/export',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_export_jobs(client):
    """Test case for get_music_export_jobs

    Music Export Jobs
    """
    params = [('over16', True),
                    ('vendor', 'vendor_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/music/exports/jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_export_tracks(client):
    """Test case for get_music_export_tracks

    Music Export Tracks
    """
    params = [('over16', True),
                    ('offset', 56),
                    ('limit', 56),
                    ('vendor', 'vendor_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/music/exports/tracks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_preferences_export(client):
    """Test case for get_music_preferences_export

    Music Export Preferences
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/music/preferences/export',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_preferences_export_vendor(client):
    """Test case for get_music_preferences_export_vendor

    Music Export Vendor Preferences
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/music/preferences/export/{vendor}'.format(vendor='vendor_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_music_export_job(client):
    """Test case for post_music_export_job

    Music Export Jobs
    """
    body = {"job_id":"job_id","vendor":"vendor","created_at":"created_at","id":"id","status":"status"}
    params = [('over16', True),
                    ('vendor', 'vendor_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/music/exports/jobs',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_music_preferences_export(client):
    """Test case for post_music_preferences_export

    Music Export Preferences
    """
    body = {"access_token":"access_token","refresh_token":"refresh_token","last_export":"last_export","partner_id":"partner_id","terms":True,"authorization_code":"authorization_code","vendor":"vendor","add_plus_export":True,"access_expires_at":"access_expires_at","legacy_state":"legacy_state"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/music/preferences/export',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_music_preferences_export_vendor(client):
    """Test case for post_music_preferences_export_vendor

    Music Export Vendor Preferences
    """
    body = {"access_token":"access_token","refresh_token":"refresh_token","last_export":"last_export","partner_id":"partner_id","terms":True,"authorization_code":"authorization_code","vendor":"vendor","add_plus_export":True,"access_expires_at":"access_expires_at","legacy_state":"legacy_state"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/music/preferences/export/{vendor}'.format(vendor='vendor_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_music_preferences_export_vendor(client):
    """Test case for put_music_preferences_export_vendor

    Music Export Vendor Preferences
    """
    body = {"access_token":"access_token","refresh_token":"refresh_token","last_export":"last_export","partner_id":"partner_id","terms":True,"authorization_code":"authorization_code","vendor":"vendor","add_plus_export":True,"access_expires_at":"access_expires_at","legacy_state":"legacy_state"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/my/music/preferences/export/{vendor}'.format(vendor='vendor_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

