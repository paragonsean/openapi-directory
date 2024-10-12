# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.webhook_test_entity import WebhookTestEntity


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_webhook_tests(client):
    """Test case for post_webhook_tests

    Create Webhook Test
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('action', 'action_example')
    data.add_field('body', None)
    data.add_field('encoding', 'encoding_example')
    data.add_field('file_as_body', True)
    data.add_field('file_form_field', 'file_form_field_example')
    data.add_field('headers', None)
    data.add_field('method', 'method_example')
    data.add_field('raw_body', 'raw_body_example')
    data.add_field('url', 'url_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/webhook_tests',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

