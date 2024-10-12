# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_advanced_moon_phase_data200_response import GetAdvancedMoonPhaseData200Response
from openapi_server.models.get_basic_moon_phase_data200_response import GetBasicMoonPhaseData200Response


pytestmark = pytest.mark.asyncio

async def test_get_advanced_moon_phase_data(client):
    """Test case for get_advanced_moon_phase_data

    Get Advanced Moon Phase Data
    """
    params = [('filters', 'moon.phase_name,moon.stage,moon_phases.full_moon.next')]
    headers = { 
        'Accept': 'application/json',
        'x_rapidapi_key': '{{Rapidapi-Key}}',
    }
    response = await client.request(
        method='GET',
        path='/advanced',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_basic_moon_phase_data(client):
    """Test case for get_basic_moon_phase_data

    Get Basic Moon Phase Data
    """
    headers = { 
        'Accept': 'application/json',
        'x_rapidapi_key': '{{Rapidapi-Key}}',
    }
    response = await client.request(
        method='GET',
        path='/basic',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_emoji_of_moon_phase(client):
    """Test case for get_emoji_of_moon_phase

    Get Emoji of Moon Phase
    """
    headers = { 
        'Accept': 'text/plain',
        'x_rapidapi_key': '{{Rapidapi-Key}}',
    }
    response = await client.request(
        method='GET',
        path='/emoji',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lunar_calendar(client):
    """Test case for get_lunar_calendar

    Get Lunar Calendar
    """
    params = [('filters', 'moon.phase_name,moon.stage,moon_phases.full_moon.next')]
    headers = { 
        'Accept': 'text/plain',
        'x_rapidapi_key': '{{Rapidapi-Key}}',
    }
    response = await client.request(
        method='GET',
        path='/calendar',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_plain_text_moon_phase_data(client):
    """Test case for get_plain_text_moon_phase_data

    Get Plain Text Moon Phase Data
    """
    headers = { 
        'Accept': 'text/plain',
        'x_rapidapi_key': '{{Rapidapi-Key}}',
    }
    response = await client.request(
        method='GET',
        path='/plain-text',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

