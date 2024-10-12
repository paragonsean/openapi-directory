# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.change_password200_response import ChangePassword200Response
from openapi_server.models.create_template_request import CreateTemplateRequest
from openapi_server.models.delete_template_request import DeleteTemplateRequest
from openapi_server.models.get_template_categories_authorized_request import GetTemplateCategoriesAuthorizedRequest
from openapi_server.models.get_template_detail_request import GetTemplateDetailRequest
from openapi_server.models.get_templatess_authorized_request import GetTemplatessAuthorizedRequest
from openapi_server.models.template import Template
from openapi_server.models.template_category import TemplateCategory
from openapi_server.models.update_template_request import UpdateTemplateRequest


pytestmark = pytest.mark.asyncio

async def test_create_template(client):
    """Test case for create_template

    Creates a New Template in the User’s Account
    """
    body = openapi_server.CreateTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/templates/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_template(client):
    """Test case for delete_template

    Deletes a users template
    """
    body = openapi_server.DeleteTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/templates/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_template_categories(client):
    """Test case for get_template_categories

    List template categories
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/templateCategories/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_template_categories_authorized(client):
    """Test case for get_template_categories_authorized

    List template categories
    """
    body = openapi_server.GetTemplateCategoriesAuthorizedRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/templateCategories/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_template_detail(client):
    """Test case for get_template_detail

    Get all info on a template
    """
    body = openapi_server.GetTemplateDetailRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/templates/view',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_templates(client):
    """Test case for get_templates

    List template categories
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/templates/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_templatess_authorized(client):
    """Test case for get_templatess_authorized

    List template categories
    """
    body = openapi_server.GetTemplatessAuthorizedRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/templates/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_template(client):
    """Test case for update_template

    Updates an Existing Template in the User’s Account
    """
    body = openapi_server.UpdateTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/templates/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

