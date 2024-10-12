# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.registration_schema import RegistrationSchema


pytestmark = pytest.mark.asyncio

async def test_registration_schema_read(client):
    """Test case for registration_schema_read

    Retrieve a Registration Schema
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/schemas/registrations/{registration_schema_id}'.format(registration_schema_id='registration_schema_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registration_schemas_list(client):
    """Test case for registration_schemas_list

    Retrieve a list of Registration Schemas
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/schemas/registrations/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

