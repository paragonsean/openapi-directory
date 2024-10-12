# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contact_types_contact_type_id_get200_response import ContactTypesContactTypeIdGet200Response
from openapi_server.models.contact_types_get200_response import ContactTypesGet200Response
from openapi_server.models.error_not_found import ErrorNotFound


pytestmark = pytest.mark.asyncio

async def test_contact_types_contact_type_id_get(client):
    """Test case for contact_types_contact_type_id_get

    Get details about one contact type
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/contact_types/{contact_type_id}'.format(contact_type_id='contact_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_types_get(client):
    """Test case for contact_types_get

    Get list of contact types supported in Apacta
    """
    params = [('identifier', 'identifier_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/contact_types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

