# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.institution import Institution
from openapi_server.models.node import Node
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_institutions_detail(client):
    """Test case for institutions_detail

    Retrieve an institution
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/institutions/{institution_id}'.format(institution_id='institution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_institutions_list(client):
    """Test case for institutions_list

    List all institutions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/institutions/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_institutions_node_list(client):
    """Test case for institutions_node_list

    List all affiliated nodes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/institutions/{institution_id}/nodes'.format(institution_id='institution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_institutions_registration_list(client):
    """Test case for institutions_registration_list

    List all affiliated registrations
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/institutions/{institution_id}/registrations'.format(institution_id='institution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_institutions_users_list(client):
    """Test case for institutions_users_list

    List all affiliated users
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/institutions/{institution_id}/users'.format(institution_id='institution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

