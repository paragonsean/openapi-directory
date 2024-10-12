# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_v1_email_disposable_get(client):
    """Test case for v1_email_disposable_get

    
    """
    params = [('format', 'format_example'),
                    ('email', 'email_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/mailboxvalidator/MailboxValidator-Disposable-Email-Checker/1.0.0/v1/email/disposable',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

