# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_user_activity_request import SearchUserActivityRequest
from openapi_server.models.search_user_activity_response import SearchUserActivityResponse


pytestmark = pytest.mark.asyncio

async def test_analyticsreporting_user_activity_search(client):
    """Test case for analyticsreporting_user_activity_search

    
    """
    body = {"viewId":"viewId","dateRange":{"endDate":"endDate","startDate":"startDate"},"pageSize":0,"pageToken":"pageToken","user":{"type":"USER_ID_TYPE_UNSPECIFIED","userId":"userId"},"activityTypes":["ACTIVITY_TYPE_UNSPECIFIED","ACTIVITY_TYPE_UNSPECIFIED"]}
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
        path='/v4/userActivity:search',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

