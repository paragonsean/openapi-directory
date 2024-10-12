# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bus_item import BusItem
from openapi_server.models.bus_pairing import BusPairing
from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.error_sub_entity import ErrorSubEntity
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.place import Place
from openapi_server.models.place_patch import PlacePatch


pytestmark = pytest.mark.asyncio

async def test_place_buses(client):
    """Test case for place_buses

    List Buses
    """
    params = [('withPairing', False)]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}/buses'.format(place_id='place_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_get_metadata(client):
    """Test case for place_get_metadata

    List metadata
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}/metadata'.format(place_id='place_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_open_pairing(client):
    """Test case for place_open_pairing

    Open/Close the pairing window
    """
    pairing = {"duration":0,"enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/places/{place_id}/buses/{bus_id}/pairing'.format(place_id='place_id_example', bus_id='bus_id_example'),
        headers=headers,
        json=pairing,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_pairing(client):
    """Test case for place_pairing

    State of the pairing window
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}/buses/{bus_id}/pairing'.format(place_id='place_id_example', bus_id='bus_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_patch(client):
    """Test case for place_patch

    Update a Place
    """
    place_patch = {"country":"FR","zipCode":"zipCode","name":"⌂ Home","timeZone":"Europe/Paris"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/places/{place_id}'.format(place_id='place_id_example'),
        headers=headers,
        json=place_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_patch_metadata(client):
    """Test case for place_patch_metadata

    Modify metadata
    """
    metadata_patch = {"add":{},"remove":[null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/places/{place_id}/metadata'.format(place_id='place_id_example'),
        headers=headers,
        json=metadata_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_places_get(client):
    """Test case for places_get

    Information about a Place
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}'.format(place_id='place_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

