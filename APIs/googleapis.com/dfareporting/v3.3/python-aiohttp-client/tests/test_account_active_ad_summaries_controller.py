# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_active_ad_summary import AccountActiveAdSummary


pytestmark = pytest.mark.asyncio

async def test_dfareporting_account_active_ad_summaries_get(client):
    """Test case for dfareporting_account_active_ad_summaries_get

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dfareporting/v3.3/userprofiles/{profile_id}/accountActiveAdSummaries/{summary_account_id}'.format(profile_id='profile_id_example', summary_account_id='summary_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

