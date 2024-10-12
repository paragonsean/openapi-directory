# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audio_renders_list_results import AudioRendersListResults
from openapi_server.models.create_audio_renders_request import CreateAudioRendersRequest
from openapi_server.models.descriptors_list_result import DescriptorsListResult
from openapi_server.models.instruments_list_result import InstrumentsListResult


pytestmark = pytest.mark.asyncio

async def test_create_audio_renders(client):
    """Test case for create_audio_renders

    Create rendered audio
    """
    body = {"audio_renders":[{"filename":"My Project.mp3","preset":"MASTER_MP3","timeline":{"spans":[{"id":111,"instrument_groups":[{"instrument_group":"roomy_kit","statuses":[{"beat":12,"status":"active"}]}],"regions":[{"beat":12,"descriptor":"cinematic_minimal_tense","end_type":{"beat":24,"event":"ending","type":"ringout"},"id":222,"key":{"tonic_note":"c","tonic_quality":"major"},"region":"music"}],"span_type":"metered","tempo":76,"tempo_changes":[{"tempo":86,"time":5}],"time":5},{"span_type":"unmetered","time":20}]}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/ai/audio/renders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_renders(client):
    """Test case for fetch_renders

    Get details about audio renders
    """
    params = [('id', ['[\"L2w7h9VNFlkzpllSUunSYayenKjN\",\"BeHx3UNXzMBB4dGsC9aa6VxnpcWl\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/ai/audio/renders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_custom_descriptors(client):
    """Test case for list_custom_descriptors

    List computer audio descriptors
    """
    params = [('render_speed_over', 5),
                    ('band_id', 'Corporate Folk Bonfire Band 1'),
                    ('band_name', 'Documentary Underscore Heartfelt Band 1'),
                    ('page', 1),
                    ('per_page', 20),
                    ('id', ['documentary_underscore_heartfelt']),
                    ('instrument_name', 'Precision Bass - Full'),
                    ('instrument_id', 'direct_fluorescent_synth_lead'),
                    ('tempo', 90),
                    ('tempo_to', 120),
                    ('tempo_from', 60),
                    ('name', 'Corporate Pop Inspirational High Energy'),
                    ('tag', 'Cinematic')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/ai/audio/descriptors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_custom_instruments(client):
    """Test case for list_custom_instruments

    List computer audio instruments
    """
    params = [('id', ['wood_blocks']),
                    ('per_page', 20),
                    ('page', 1),
                    ('name', 'Precision Bass - Full'),
                    ('tag', 'Percussion')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/ai/audio/instruments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

