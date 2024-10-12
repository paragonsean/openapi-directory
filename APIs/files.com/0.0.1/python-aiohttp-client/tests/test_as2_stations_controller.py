# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.as2_station_entity import As2StationEntity


pytestmark = pytest.mark.asyncio

async def test_delete_as2_stations_id(client):
    """Test case for delete_as2_stations_id

    Delete As2 Station
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/as2_stations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_as2_stations(client):
    """Test case for get_as2_stations

    List As2 Stations
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/as2_stations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_as2_stations_id(client):
    """Test case for get_as2_stations_id

    Show As2 Station
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/as2_stations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_as2_stations_id(client):
    """Test case for patch_as2_stations_id

    Update As2 Station
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('name', 'name_example')
    data.add_field('private_key', 'private_key_example')
    data.add_field('private_key_password', 'private_key_password_example')
    data.add_field('public_certificate', 'public_certificate_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/as2_stations/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_as2_stations(client):
    """Test case for post_as2_stations

    Create As2 Station
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('name', 'name_example')
    data.add_field('private_key', 'private_key_example')
    data.add_field('private_key_password', 'private_key_password_example')
    data.add_field('public_certificate', 'public_certificate_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/as2_stations',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

