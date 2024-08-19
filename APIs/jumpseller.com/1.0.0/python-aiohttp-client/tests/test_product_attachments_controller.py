# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attachment import Attachment
from openapi_server.models.attachment_edit import AttachmentEdit
from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_products_id_attachments_attachment_id_json_delete(client):
    """Test case for products_id_attachments_attachment_id_json_delete

    Delete a Product Attachment.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/products/{id}/attachments/{attachment_id_jso}'.format(id=56, attachment_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_attachments_attachment_id_json_get(client):
    """Test case for products_id_attachments_attachment_id_json_get

    Retrieve a single Product Attachment.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/attachments/{attachment_id_jso}'.format(id=56, attachment_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_attachments_count_json_get(client):
    """Test case for products_id_attachments_count_json_get

    Count all Product Attachments.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/attachments/count.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_attachments_json_get(client):
    """Test case for products_id_attachments_json_get

    Retrieve all Product Attachments.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/attachments.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_attachments_json_post(client):
    """Test case for products_id_attachments_json_post

    Create a new Product Attachment.
    """
    body = {"attachment":{"filename":"filename","url":"url"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/products/{id}/attachments.json'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

