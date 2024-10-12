# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.campaign_creative_association import CampaignCreativeAssociation
from openapi_server.models.campaign_creative_associations_list_response import CampaignCreativeAssociationsListResponse


pytestmark = pytest.mark.asyncio

async def test_dfareporting_campaign_creative_associations_insert(client):
    """Test case for dfareporting_campaign_creative_associations_insert

    
    """
    body = {"kind":"kind","creativeId":"creativeId"}
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
        path='/dfareporting/v3.3/userprofiles/{profile_id}/campaigns/{campaign_id}/campaignCreativeAssociations'.format(profile_id='profile_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfareporting_campaign_creative_associations_list(client):
    """Test case for dfareporting_campaign_creative_associations_list

    
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
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example'),
                    ('sortOrder', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/campaigns/{campaign_id}/campaignCreativeAssociations'.format(profile_id='profile_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

