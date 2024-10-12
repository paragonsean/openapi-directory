# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.composition_enum_format import CompositionEnumFormat
from openapi_server.models.composition_enum_status import CompositionEnumStatus
from openapi_server.models.list_composition_response import ListCompositionResponse
from openapi_server.models.video_v1_composition import VideoV1Composition


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_composition(client):
    """Test case for create_composition

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'audio_sources': ['audio_sources_example'],
        'audio_sources_excluded': ['audio_sources_excluded_example'],
        'format': openapi_server.CompositionEnumFormat(),
        'resolution': 'resolution_example',
        'room_sid': 'room_sid_example',
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example',
        'trim': True,
        'video_layout': None
        }
    response = await client.request(
        method='POST',
        path='/v1/Compositions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_composition(client):
    """Test case for delete_composition

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Compositions/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_composition(client):
    """Test case for fetch_composition

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Compositions/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_composition(client):
    """Test case for list_composition

    
    """
    params = [('Status', openapi_server.CompositionEnumStatus()),
                    ('DateCreatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('DateCreatedBefore', '2013-10-20T19:20:30+01:00'),
                    ('RoomSid', 'room_sid_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Compositions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

