# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.url_channel import UrlChannel
from openapi_server.models.url_channels import UrlChannels


pytestmark = pytest.mark.asyncio

async def test_adsensehost_urlchannels_delete(client):
    """Test case for adsensehost_urlchannels_delete

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/adsensehost/v4.1/adclients/{ad_client_id}/urlchannels/{url_channel_id}'.format(ad_client_id='ad_client_id_example', url_channel_id='url_channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_urlchannels_insert(client):
    """Test case for adsensehost_urlchannels_insert

    
    """
    body = {"kind":"adsensehost#urlChannel","id":"id","urlPattern":"urlPattern"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/adsensehost/v4.1/adclients/{ad_client_id}/urlchannels'.format(ad_client_id='ad_client_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_urlchannels_list(client):
    """Test case for adsensehost_urlchannels_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/adclients/{ad_client_id}/urlchannels'.format(ad_client_id='ad_client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

