# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.form import Form
from openapi_server.models.form_response import FormResponse
from openapi_server.models.form_response_submission import FormResponseSubmission
from openapi_server.models.form_submission import FormSubmission


pytestmark = pytest.mark.asyncio

async def test_form_responses_get(client):
    """Test case for form_responses_get

    List form responses
    """
    params = [('user', 'user_example'),
                    ('form', 'form_example'),
                    ('contribution', 'contribution_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/form-responses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_form_responses_id_get(client):
    """Test case for form_responses_id_get

    Get a single form response by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/form-responses/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_form_responses_post(client):
    """Test case for form_responses_post

    Submit a response to a form
    """
    body = {"contribution":"contribution","form":"form","responses":{"key":"responses"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/form-responses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_get(client):
    """Test case for forms_get

    List forms
    """
    params = [('ownedBy', 'owned_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/forms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_id_delete(client):
    """Test case for forms_id_delete

    Delete this form and all of it's responses.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/1/forms/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_id_get(client):
    """Test case for forms_id_get

    Get a single form by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/forms/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_post(client):
    """Test case for forms_post

    Create a form
    """
    body = {"noCss":True,"cssUrl":"cssUrl","heading":"heading","name":"name","fields":[{"public":True,"name":"name","options":["options","options"],"description":"description","label":"label","type":"type","required":True},{"public":True,"name":"name","options":["options","options"],"description":"description","label":"label","type":"type","required":True}],"callToAction":"callToAction","tags":[{"tagSet":{"name":"name","id":"id"},"colour":"#0061a6","urlWords":"urlWords","name":"name","id":"id"},{"tagSet":{"name":"name","id":"id"},"colour":"#0061a6","urlWords":"urlWords","name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/forms',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

