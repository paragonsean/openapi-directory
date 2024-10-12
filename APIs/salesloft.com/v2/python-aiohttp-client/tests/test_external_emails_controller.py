# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.external_email import ExternalEmail


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_external_emails_json_post(client):
    """Test case for v2_external_emails_json_post

    Create an External Email
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'mailbox': 'mailbox_example',
        'raw': 'raw_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/external_emails.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

