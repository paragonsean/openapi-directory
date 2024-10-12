# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.campaigns_remove200_response import CampaignsRemove200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.template_request import TemplateRequest
from openapi_server.models.template_response import TemplateResponse
from openapi_server.models.templates_response import TemplatesResponse


pytestmark = pytest.mark.asyncio

async def test_templates_create(client):
    """Test case for templates_create

    Create template
    """
    body = {"template":"Hi {{{firstName}}}. Grab 20% off today only at ABC Shoes","name":"name","type":"SMS"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/accounts/{account_id}/templates'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_templates_fetch(client):
    """Test case for templates_fetch

    Fetch template by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/templates/{template_id}'.format(account_id='account_id_example', template_id='template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_templates_fetch_all(client):
    """Test case for templates_fetch_all

    Fetch templates
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/templates'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_templates_remove(client):
    """Test case for templates_remove

    Deletes a template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/accounts/{account_id}/templates/{template_id}'.format(account_id='account_id_example', template_id='template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_templates_update(client):
    """Test case for templates_update

    Updates a template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/accounts/{account_id}/templates/{template_id}'.format(account_id='account_id_example', template_id='template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

