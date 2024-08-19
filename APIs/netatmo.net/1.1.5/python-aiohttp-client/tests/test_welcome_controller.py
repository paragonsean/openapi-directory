# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.na_welcome_event_response import NAWelcomeEventResponse
from openapi_server.models.na_welcome_home_data_response import NAWelcomeHomeDataResponse
from openapi_server.models.na_welcome_persons_away_response import NAWelcomePersonsAwayResponse
from openapi_server.models.na_welcome_persons_home_response import NAWelcomePersonsHomeResponse
from openapi_server.models.na_welcome_webhook_response import NAWelcomeWebhookResponse


pytestmark = pytest.mark.asyncio

async def test_addwebhook(client):
    """Test case for addwebhook

    
    """
    params = [('url', 'url_example'),
                    ('app_type', 'app_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/addwebhook',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dropwebhook(client):
    """Test case for dropwebhook

    
    """
    params = [('app_type', 'app_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dropwebhook',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getcamerapicture(client):
    """Test case for getcamerapicture

    
    """
    params = [('image_id', 'image_id_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/getcamerapicture',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geteventsuntil(client):
    """Test case for geteventsuntil

    
    """
    params = [('home_id', 'home_id_example'),
                    ('event_id', 'event_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/geteventsuntil',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gethomedata(client):
    """Test case for gethomedata

    
    """
    params = [('home_id', 'home_id_example'),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/gethomedata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getlasteventof(client):
    """Test case for getlasteventof

    
    """
    params = [('home_id', 'home_id_example'),
                    ('person_id', 'person_id_example'),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/getlasteventof',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getnextevents(client):
    """Test case for getnextevents

    
    """
    params = [('home_id', 'home_id_example'),
                    ('event_id', 'event_id_example'),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/getnextevents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setpersonsaway(client):
    """Test case for setpersonsaway

    
    """
    params = [('home_id', 'home_id_example'),
                    ('person_id', 'person_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/setpersonsaway',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setpersonshome(client):
    """Test case for setpersonshome

    
    """
    params = [('home_id', 'home_id_example'),
                    ('person_ids', 'person_ids_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/setpersonshome',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

