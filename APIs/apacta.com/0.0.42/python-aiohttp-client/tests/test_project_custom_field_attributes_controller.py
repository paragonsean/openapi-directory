# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.project_custom_field_attributes_get200_response import ProjectCustomFieldAttributesGet200Response
from openapi_server.models.project_custom_field_attributes_project_custom_field_attribute_id_get200_response import ProjectCustomFieldAttributesProjectCustomFieldAttributeIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_project_custom_field_attributes_get(client):
    """Test case for project_custom_field_attributes_get

    Get a list of project custom field attributes
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project_custom_field_attributes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_custom_field_attributes_project_custom_field_attribute_id_get(client):
    """Test case for project_custom_field_attributes_project_custom_field_attribute_id_get

    Details of 1 project custom field attribute
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project_custom_field_attributes/{project_custom_field_attribute_id}'.format(project_custom_field_attribute_id='project_custom_field_attribute_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

