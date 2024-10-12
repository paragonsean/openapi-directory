# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.abuse_report import AbuseReport


pytestmark = pytest.mark.asyncio

async def test_youtube_abuse_reports_insert(client):
    """Test case for youtube_abuse_reports_insert

    
    """
    body = {"subject":{"typeId":"typeId","id":"id","url":"url"},"description":"description","relatedEntities":[{"entity":{"typeId":"typeId","id":"id","url":"url"}},{"entity":{"typeId":"typeId","id":"id","url":"url"}}],"abuseTypes":[{"id":"id"},{"id":"id"}]}
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
                    ('part', ['part_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/abuseReports',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

