# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deletion_incident import DeletionIncident
from openapi_server.models.get_additions400_response import GetAdditions400Response
from openapi_server.models.get_additions_page_parameter import GetAdditionsPageParameter
from openapi_server.models.incident import Incident
from openapi_server.models.non_deletion_incident import NonDeletionIncident
from openapi_server.models.videogame_idor_slug import VideogameIDOrSlug


pytestmark = pytest.mark.asyncio

async def test_get_additions(client):
    """Test case for get_additions

    List additions
    """
    params = [('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50),
                    ('type', ['type_example']),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('videogame', [openapi_server.VideogameIDOrSlug()])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/additions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_changes(client):
    """Test case for get_changes

    List changes
    """
    params = [('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50),
                    ('type', ['type_example']),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('videogame', [openapi_server.VideogameIDOrSlug()])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/changes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deletions(client):
    """Test case for get_deletions

    List deletions
    """
    params = [('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50),
                    ('type', ['type_example']),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('videogame', [openapi_server.VideogameIDOrSlug()])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/deletions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_incidents(client):
    """Test case for get_incidents

    List changes, additions and deletions
    """
    params = [('page', openapi_server.GetAdditionsPageParameter()),
                    ('per_page', 50),
                    ('type', ['type_example']),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('videogame', [openapi_server.VideogameIDOrSlug()])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'QueryToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/incidents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

