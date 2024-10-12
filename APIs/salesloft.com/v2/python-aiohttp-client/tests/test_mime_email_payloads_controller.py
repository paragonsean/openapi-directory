# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.mime_email_payload import MimeEmailPayload


pytestmark = pytest.mark.asyncio

async def test_v2_mime_email_payloads_id_json_get(client):
    """Test case for v2_mime_email_payloads_id_json_get

    Fetch the MIME content for email
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/mime_email_payloads/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

