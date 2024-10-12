# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.download_accesses import DownloadAccesses
from openapi_server.models.request_access_data import RequestAccessData
from openapi_server.models.usersettings import Usersettings
from openapi_server.models.volumes import Volumes


pytestmark = pytest.mark.asyncio

async def test_books_myconfig_get_user_settings(client):
    """Test case for books_myconfig_get_user_settings

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/myconfig/getUserSettings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_myconfig_release_download_access(client):
    """Test case for books_myconfig_release_download_access

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('cpksver', 'cpksver_example'),
                    ('volumeIds', ['volume_ids_example']),
                    ('locale', 'locale_example'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/myconfig/releaseDownloadAccess',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_myconfig_request_access(client):
    """Test case for books_myconfig_request_access

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('cpksver', 'cpksver_example'),
                    ('nonce', 'nonce_example'),
                    ('source', 'source_example'),
                    ('volumeId', 'volume_id_example'),
                    ('licenseTypes', 'license_types_example'),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/myconfig/requestAccess',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_myconfig_sync_volume_licenses(client):
    """Test case for books_myconfig_sync_volume_licenses

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('cpksver', 'cpksver_example'),
                    ('nonce', 'nonce_example'),
                    ('source', 'source_example'),
                    ('features', ['features_example']),
                    ('includeNonComicsSeries', True),
                    ('locale', 'locale_example'),
                    ('showPreorders', True),
                    ('volumeIds', ['volume_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/myconfig/syncVolumeLicenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_myconfig_update_user_settings(client):
    """Test case for books_myconfig_update_user_settings

    
    """
    body = {"notification":{"rewardExpirations":{"opted_state":"opted_state"},"matchMyInterests":{"opted_state":"opted_state"},"moreFromSeries":{"opted_state":"opted_state"},"moreFromAuthors":{"opted_state":"opted_state"},"priceDrop":{"opted_state":"opted_state"}},"notesExport":{"isEnabled":True,"folderName":"folderName"},"kind":"kind"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/myconfig/updateUserSettings',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

