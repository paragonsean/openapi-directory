# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.country_specifications import CountrySpecifications
from openapi_server.models.discoverable_participant import DiscoverableParticipant
from openapi_server.models.discovered_participant import DiscoveredParticipant
from openapi_server.models.error_model import ErrorModel


pytestmark = pytest.mark.asyncio

async def test_discovery_exists(client):
    """Test case for discovery_exists

    Discover Network Participant Existence
    """
    body = {"identifier":"identifier","scheme":"scheme","metaScheme":"iso6523-actorid-upis","documentTypes":["invoice","invoice"],"network":"peppol"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/discovery/exists',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discovery_identifiers(client):
    """Test case for discovery_identifiers

    Discover Country Identifiers ** EXPERIMENTAL
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/discovery/identifiers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discovery_receives(client):
    """Test case for discovery_receives

    Disover Network Participant
    """
    body = {"identifier":"identifier","scheme":"scheme","metaScheme":"iso6523-actorid-upis","documentTypes":["invoice","invoice"],"network":"peppol"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/discovery/receives',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

