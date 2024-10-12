# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.render_template_id_post200_response import RenderTemplateIdPost200Response
from openapi_server.models.render_template_id_post_request import RenderTemplateIdPostRequest


pytestmark = pytest.mark.asyncio

async def test_render_render_id_get(client):
    """Test case for render_render_id_get

    Retreive a generated document from a render ID.
    """
    headers = { 
        'Accept': 'application/json',
        'carbone_version': 4,
    }
    response = await client.request(
        method='GET',
        path='/render/{render_id}'.format(render_id='render_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_render_template_id_post(client):
    """Test case for render_template_id_post

    Generate a document from a template ID, and a JSON data-set
    """
    body = openapi_server.RenderTemplateIdPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'carbone_version': 4,
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/render/{template_id}'.format(template_id='template_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

