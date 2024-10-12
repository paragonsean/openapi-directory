# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_field import CustomField
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError


pytestmark = pytest.mark.asyncio

async def test_get_custom_field(client):
    """Test case for get_custom_field

    Retrieve a Custom Field
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/custom-fields/{resource}/{name}'.format(resource='resource_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_field_collection(client):
    """Test case for get_custom_field_collection

    Retrieve Custom Fields
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/custom-fields/{resource}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_custom_field(client):
    """Test case for put_custom_field

    Create or alter a Custom Field
    """
    body = {"_links":[{"rel":"self"},{"rel":"self"}],"additionalSchema":"","name":"name","description":"description","type":"array"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/custom-fields/{resource}/{name}'.format(resource='resource_example', name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

