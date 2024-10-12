# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.query_drive_activity_request import QueryDriveActivityRequest
from openapi_server.models.query_drive_activity_response import QueryDriveActivityResponse


pytestmark = pytest.mark.asyncio

async def test_driveactivity_activity_query(client):
    """Test case for driveactivity_activity_query

    
    """
    body = {"consolidationStrategy":{"legacy":"{}","none":"{}"},"filter":"filter","itemName":"itemName","ancestorName":"ancestorName","pageSize":0,"pageToken":"pageToken"}
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
        path='/v2/activity:query',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

