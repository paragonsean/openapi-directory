# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auto_forward import AutoForward
from openapi_server.models.auto_reply import AutoReply
from openapi_server.models.create_mailbox_request import CreateMailboxRequest
from openapi_server.models.mailbox import Mailbox
from openapi_server.models.mailbox_detail import MailboxDetail
from openapi_server.models.update_mailbox_password_request import UpdateMailboxPasswordRequest


pytestmark = pytest.mark.asyncio

async def test_change_mailbox_password(client):
    """Test case for change_mailbox_password

    Change password for mailbox
    """
    body = {"password":"password"}
    params = [('mailbox_name', 'mailbox_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/mailboxes/{mailbox_name}/password'.format(mailbox_name2='mailbox_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configure_mailbox_auto_forward(client):
    """Test case for configure_mailbox_auto_forward

    Configure auto-forward for mailbox
    """
    body = {"email_addresses":["email_addresses","email_addresses"],"copy_to_myself":True,"enabled":True}
    params = [('mailbox_name', 'mailbox_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/mailboxes/{mailbox_name}/autoforward'.format(mailbox_name2='mailbox_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configure_mailbox_auto_reply(client):
    """Test case for configure_mailbox_auto_reply

    Configure auto-reply for mailbox
    """
    body = {"subject":"subject","message":"message","enabled":True}
    params = [('mailbox_name', 'mailbox_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/mailboxes/{mailbox_name}/autoreply'.format(mailbox_name2='mailbox_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_mailbox(client):
    """Test case for create_mailbox

    Create a new mailbox.
    """
    body = {"password":"password","account_id":0,"email_address":"email_address"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/mailboxes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_mailbox(client):
    """Test case for delete_mailbox

    Delete a mailbox
    """
    params = [('mailbox_name', 'mailbox_name_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/mailboxes/{mailbox_name}'.format(mailbox_name2='mailbox_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mailbox(client):
    """Test case for get_mailbox

    Get a specific mailbox
    """
    params = [('mailbox_name', 'mailbox_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/mailboxes/{mailbox_name}'.format(mailbox_name2='mailbox_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mailboxes(client):
    """Test case for get_mailboxes

    Gets your mailboxes.
    """
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/mailboxes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

