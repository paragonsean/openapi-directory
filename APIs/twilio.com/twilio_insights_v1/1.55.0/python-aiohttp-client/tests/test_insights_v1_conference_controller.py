# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.insights_v1_conference import InsightsV1Conference
from openapi_server.models.list_conference_response import ListConferenceResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_conference(client):
    """Test case for fetch_conference

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conferences/{conference_sid}'.format(conference_sid='conference_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_conference(client):
    """Test case for list_conference

    
    """
    params = [('ConferenceSid', 'conference_sid_example'),
                    ('FriendlyName', 'friendly_name_example'),
                    ('Status', 'status_example'),
                    ('CreatedAfter', 'created_after_example'),
                    ('CreatedBefore', 'created_before_example'),
                    ('MixerRegion', 'mixer_region_example'),
                    ('Tags', 'tags_example'),
                    ('Subaccount', 'subaccount_example'),
                    ('DetectedIssues', 'detected_issues_example'),
                    ('EndReason', 'end_reason_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conferences',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

