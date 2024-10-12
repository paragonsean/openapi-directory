# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.template_post200_response import TemplatePost200Response
from openapi_server.models.template_post_request import TemplatePostRequest
from openapi_server.models.template_post_request1 import TemplatePostRequest1
from openapi_server.models.template_template_id_delete200_response import TemplateTemplateIdDelete200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_template_post(client):
    """Test case for template_post

    Upload a template.
    """
    body = openapi_server.TemplatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'carbone_version': 4,
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/template',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_template_template_id_delete(client):
    """Test case for template_template_id_delete

    Delete a template from a template ID
    """
    headers = { 
        'Accept': 'application/json',
        'carbone_version': 4,
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/template/{template_id}'.format(template_id='template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_template_template_id_get(client):
    """Test case for template_template_id_get

    Download a template from a template ID
    """
    headers = { 
        'Accept': 'application/json',
        'carbone_version': 4,
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/template/{template_id}'.format(template_id='template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

