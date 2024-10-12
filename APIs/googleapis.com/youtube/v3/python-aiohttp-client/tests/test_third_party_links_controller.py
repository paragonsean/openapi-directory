# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.third_party_link import ThirdPartyLink
from openapi_server.models.third_party_link_list_response import ThirdPartyLinkListResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_third_party_links_delete(client):
    """Test case for youtube_third_party_links_delete

    
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
                    ('linkingToken', 'linking_token_example'),
                    ('type', 'type_example'),
                    ('externalChannelId', 'external_channel_id_example'),
                    ('part', ['part_example'])]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/youtube/v3/thirdPartyLinks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_third_party_links_insert(client):
    """Test case for youtube_third_party_links_insert

    
    """
    body = {"snippet":{"type":"linkUnspecified","channelToStoreLink":{"billingDetails":{"billingStatus":"billingStatusUnspecified"},"merchantId":"merchantId","storeUrl":"storeUrl","storeName":"storeName"}},"kind":"youtube#thirdPartyLink","linkingToken":"linkingToken","etag":"etag","status":{"linkStatus":"unknown"}}
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
                    ('part', ['part_example']),
                    ('externalChannelId', 'external_channel_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/thirdPartyLinks',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_third_party_links_list(client):
    """Test case for youtube_third_party_links_list

    
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
                    ('part', ['part_example']),
                    ('externalChannelId', 'external_channel_id_example'),
                    ('linkingToken', 'linking_token_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/youtube/v3/thirdPartyLinks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_third_party_links_update(client):
    """Test case for youtube_third_party_links_update

    
    """
    body = {"snippet":{"type":"linkUnspecified","channelToStoreLink":{"billingDetails":{"billingStatus":"billingStatusUnspecified"},"merchantId":"merchantId","storeUrl":"storeUrl","storeName":"storeName"}},"kind":"youtube#thirdPartyLink","linkingToken":"linkingToken","etag":"etag","status":{"linkStatus":"unknown"}}
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
                    ('part', ['part_example']),
                    ('externalChannelId', 'external_channel_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/youtube/v3/thirdPartyLinks',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

