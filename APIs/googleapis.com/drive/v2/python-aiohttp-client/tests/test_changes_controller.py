# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.change import Change
from openapi_server.models.change_list import ChangeList
from openapi_server.models.channel import Channel
from openapi_server.models.start_page_token import StartPageToken


pytestmark = pytest.mark.asyncio

async def test_drive_changes_get(client):
    """Test case for drive_changes_get

    
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
                    ('driveId', 'drive_id_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('teamDriveId', 'team_drive_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v2/changes/{change_id}'.format(change_id='change_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_changes_get_start_page_token(client):
    """Test case for drive_changes_get_start_page_token

    
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
                    ('driveId', 'drive_id_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('teamDriveId', 'team_drive_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v2/changes/startPageToken',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_changes_list(client):
    """Test case for drive_changes_list

    
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
                    ('driveId', 'drive_id_example'),
                    ('includeCorpusRemovals', True),
                    ('includeDeleted', True),
                    ('includeItemsFromAllDrives', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('includeSubscribed', True),
                    ('includeTeamDriveItems', True),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('spaces', 'spaces_example'),
                    ('startChangeId', 'start_change_id_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('teamDriveId', 'team_drive_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/drive/v2/changes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_changes_watch(client):
    """Test case for drive_changes_watch

    
    """
    body = {"resourceId":"resourceId","address":"address","payload":True,"kind":"api#channel","expiration":"expiration","id":"id","resourceUri":"resourceUri","params":{"key":"params"},"type":"type","token":"token"}
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
                    ('driveId', 'drive_id_example'),
                    ('includeCorpusRemovals', True),
                    ('includeDeleted', True),
                    ('includeItemsFromAllDrives', True),
                    ('includeLabels', 'include_labels_example'),
                    ('includePermissionsForView', 'include_permissions_for_view_example'),
                    ('includeSubscribed', True),
                    ('includeTeamDriveItems', True),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('spaces', 'spaces_example'),
                    ('startChangeId', 'start_change_id_example'),
                    ('supportsAllDrives', True),
                    ('supportsTeamDrives', True),
                    ('teamDriveId', 'team_drive_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/drive/v2/changes/watch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

