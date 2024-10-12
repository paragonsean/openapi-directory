# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.web_service_template import WebServiceTemplate
from openapi_server.models.web_service_templates import WebServiceTemplates


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_templates_all_get(client):
    """Test case for api_rest_v1_templates_all_get

    all
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/templates/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_templates_template_id_delete(client):
    """Test case for api_rest_v1_templates_template_id_delete

    delete
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/app/api/rest/v1/templates/{template_id}'.format(template_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_templates_template_id_get(client):
    """Test case for api_rest_v1_templates_template_id_get

    get
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/templates/{template_id}'.format(template_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

