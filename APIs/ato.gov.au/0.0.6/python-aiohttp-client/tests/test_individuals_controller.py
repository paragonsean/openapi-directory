# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.failed_precondition import FailedPrecondition
from openapi_server.models.individual import Individual
from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_individuals_get(client):
    """Test case for individuals_get

    Retrieve a list of individuals
    """
    params = [('dateOfBirth', 'date_of_birth_example'),
                    ('placeOfBirth', 'place_of_birth_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/individuals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_delete(client):
    """Test case for individuals_party_id_delete

    Delete an individual
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/individuals/{party_id}'.format(party_id='party_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_get(client):
    """Test case for individuals_party_id_get

    Retrieve an individual
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/individuals/{party_id}'.format(party_id='party_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_party_id_put(client):
    """Test case for individuals_party_id_put

    Update an individual
    """
    body = openapi_server.Individual()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/individuals/{party_id}'.format(party_id='party_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individuals_post(client):
    """Test case for individuals_post

    Create an individual
    """
    body = openapi_server.Individual()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/individuals',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

