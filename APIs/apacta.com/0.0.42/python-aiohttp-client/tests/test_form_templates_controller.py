# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.form_templates_form_template_id_get200_response import FormTemplatesFormTemplateIdGet200Response
from openapi_server.models.form_templates_get200_response import FormTemplatesGet200Response


pytestmark = pytest.mark.asyncio

async def test_form_templates_form_template_id_get(client):
    """Test case for form_templates_form_template_id_get

    View one form template
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/form_templates/{form_template_id}'.format(form_template_id='form_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_form_templates_get(client):
    """Test case for form_templates_get

    Get array of form_templates for your company
    """
    params = [('name', 'name_example'),
                    ('identifier', 'identifier_example'),
                    ('pdf_template_identifier', 'pdf_template_identifier_example'),
                    ('description', 'description_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/form_templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

