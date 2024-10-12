# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.forms_form_id_get200_response import FormsFormIdGet200Response
from openapi_server.models.forms_get200_response import FormsGet200Response
from openapi_server.models.forms_post_request import FormsPostRequest


pytestmark = pytest.mark.asyncio

async def test_forms_form_id_delete(client):
    """Test case for forms_form_id_delete

    Delete a form
    """
    headers = { 
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/forms/{form_id}'.format(form_id='form_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_form_id_get(client):
    """Test case for forms_form_id_get

    View form
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/forms/{form_id}'.format(form_id='form_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_form_id_put(client):
    """Test case for forms_form_id_put

    Edit a form
    """
    headers = { 
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/forms/{form_id}'.format(form_id='form_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_get(client):
    """Test case for forms_get

    Retrieve array of forms
    """
    params = [('extended', 'extended_example'),
                    ('date_from', 'date_from_example'),
                    ('date_to', 'date_to_example'),
                    ('show', 'show_example'),
                    ('project_id', 'project_id_example'),
                    ('created_by_id', 'created_by_id_example'),
                    ('form_template_id', ['form_template_id_example']),
                    ('form_template_type', 'form_template_type_example'),
                    ('employee_name', 'employee_name_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/forms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_post(client):
    """Test case for forms_post

    Add new form
    """
    body = openapi_server.FormsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/forms',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_undelete_form_id_get(client):
    """Test case for forms_undelete_form_id_get

    Undelete form and related entities to it
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/forms/undelete/{form_id}'.format(form_id='form_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_view_time_form_pdf_form_id_get(client):
    """Test case for forms_view_time_form_pdf_form_id_get

    Generate time form pdf
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/forms/view_time_form_pdf/{form_id}'.format(form_id='form_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

