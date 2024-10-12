# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_activities_response import ListActivitiesResponse


pytestmark = pytest.mark.asyncio

async def test_appsactivity_activities_list(client):
    """Test case for appsactivity_activities_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('drive.ancestorId', 'drive_ancestor_id_example'),
                    ('drive.fileId', 'drive_file_id_example'),
                    ('groupingStrategy', 'grouping_strategy_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('source', 'source_example'),
                    ('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/appsactivity/v1/activities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

