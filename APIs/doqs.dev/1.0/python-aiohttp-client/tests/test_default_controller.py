# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_template_request import CreateOrUpdateTemplateRequest
from openapi_server.models.generate_pdf_payload import GeneratePDFPayload
from openapi_server.models.preview_model import PreviewModel
from openapi_server.models.response_error import ResponseError
from openapi_server.models.response_ok_designer_template import ResponseOkDesignerTemplate
from openapi_server.models.response_ok_list_fillr_entities_designer_template_designer_template import ResponseOkListFillrEntitiesDesignerTemplateDesignerTemplate
from openapi_server.models.response_ok_none_type import ResponseOkNoneType
from openapi_server.models.response_ok_preview_response import ResponseOkPreviewResponse


pytestmark = pytest.mark.asyncio

async def test_create_template_designer_templates_post(client):
    """Test case for create_template_designer_templates_post

    Create Template
    """
    body = {"components":["{}","{}"],"css":"css","header_html":"header_html","margin":"","orientation":"landscape","format":"a0","name":"name","footer_html":"footer_html","preview_payload":"{}","template_html":"template_html"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/designer/templates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_designer_templates_id_delete(client):
    """Test case for delete_designer_templates_id_delete

    Delete
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/designer/templates/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_pdf_designer_templates_id_generate_post(client):
    """Test case for generate_pdf_designer_templates_id_generate_post

    Generate Pdf
    """
    body = {"data":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/designer/templates/{id}/generate'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_templates_designer_templates_get(client):
    """Test case for list_templates_designer_templates_get

    List Templates
    """
    params = [('limit', 100),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/designer/templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_templates_designer_templates_id_get(client):
    """Test case for list_templates_designer_templates_id_get

    List Templates
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/designer/templates/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preview_designer_templates_preview_post(client):
    """Test case for preview_designer_templates_preview_post

    Preview
    """
    body = {"css":"css","header_html":"header_html","data":"{}","footer_html":"footer_html","template_html":"template_html"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/designer/templates/preview',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_template_designer_templates_id_put(client):
    """Test case for update_template_designer_templates_id_put

    Update Template
    """
    body = {"components":["{}","{}"],"css":"css","header_html":"header_html","margin":"","orientation":"landscape","format":"a0","name":"name","footer_html":"footer_html","preview_payload":"{}","template_html":"template_html"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/designer/templates/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

