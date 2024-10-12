# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contact_custom_field_attributes_contact_custom_field_attribute_id_get200_response import ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response
from openapi_server.models.contact_custom_field_attributes_get200_response import ContactCustomFieldAttributesGet200Response
from openapi_server.models.error_not_found import ErrorNotFound


pytestmark = pytest.mark.asyncio

async def test_contact_custom_field_attributes_contact_custom_field_attribute_id_get(client):
    """Test case for contact_custom_field_attributes_contact_custom_field_attribute_id_get

    Details of 1 contact custom field attribute
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/contact_custom_field_attributes/{contact_custom_field_attribute_id}'.format(contact_custom_field_attribute_id='contact_custom_field_attribute_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contact_custom_field_attributes_get(client):
    """Test case for contact_custom_field_attributes_get

    Get a list of contact custom field attributes
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/contact_custom_field_attributes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

