# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.insights_v1_conference_conference_participant import InsightsV1ConferenceConferenceParticipant
from openapi_server.models.list_conference_participant_response import ListConferenceParticipantResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_conference_participant(client):
    """Test case for fetch_conference_participant

    
    """
    params = [('Events', 'events_example'),
                    ('Metrics', 'metrics_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conferences/{conference_sid}/Participants/{participant_sid}'.format(conference_sid='conference_sid_example', participant_sid='participant_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_conference_participant(client):
    """Test case for list_conference_participant

    
    """
    params = [('ParticipantSid', 'participant_sid_example'),
                    ('Label', 'label_example'),
                    ('Events', 'events_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Conferences/{conference_sid}/Participants'.format(conference_sid='conference_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

