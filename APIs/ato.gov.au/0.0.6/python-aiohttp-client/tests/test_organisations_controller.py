# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.failed_precondition import FailedPrecondition
from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.not_found import NotFound
from openapi_server.models.organisation import Organisation
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_organisations_get(client):
    """Test case for organisations_get

    Retrieve a list of organisations
    """
    params = [('registeredIdentifier', 'registered_identifier_example'),
                    ('identifier', 'identifier_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/organisations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_delete(client):
    """Test case for organisations_party_id_delete

    Delete an organisation
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/organisations/{party_id}'.format(party_id='party_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_get(client):
    """Test case for organisations_party_id_get

    Retrieve an organisation
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/organisations/{party_id}'.format(party_id='party_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_put(client):
    """Test case for organisations_party_id_put

    Update an organisation
    """
    body = openapi_server.Organisation()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/organisations/{party_id}'.format(party_id='party_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_post(client):
    """Test case for organisations_post

    Create an organisation
    """
    body = openapi_server.Organisation()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/organisations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

