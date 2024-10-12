# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pending_email import PendingEmail


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_pending_emails_id_json_put(client):
    """Test case for v2_pending_emails_id_json_put

    Updates the status of an email sent by an External Email Client
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'error_message': 'error_message_example',
        'message_id': 'message_id_example',
        'sent_at': 'sent_at_example',
        'status': 'status_example'
        }
    response = await client.request(
        method='PUT',
        path='/v2/pending_emails/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_pending_emails_json_get(client):
    """Test case for v2_pending_emails_json_get

    Fetches a list of emails ready to be sent by an external email service. Only emails sent with an External Email Client will appear here.
    """
    params = [('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('limit_paging_counts', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/pending_emails.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

