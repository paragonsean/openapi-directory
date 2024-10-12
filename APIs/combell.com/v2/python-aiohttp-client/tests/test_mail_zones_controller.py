# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_alias_request import CreateAliasRequest
from openapi_server.models.create_catch_all_request import CreateCatchAllRequest
from openapi_server.models.create_smtp_domain_request import CreateSmtpDomainRequest
from openapi_server.models.mail_zone import MailZone
from openapi_server.models.update_alias_request import UpdateAliasRequest
from openapi_server.models.update_anti_spam_request import UpdateAntiSpamRequest
from openapi_server.models.update_smtp_domain_request import UpdateSmtpDomainRequest


pytestmark = pytest.mark.asyncio

async def test_configure_alias(client):
    """Test case for configure_alias

    Configure a alias
    """
    body = {"destinations":["destinations","destinations"]}
    params = [('domain_name', 'domain_name_example'),
                    ('email_address', 'email_address_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/mailzones/{domain_name}/aliases/{email_address}'.format(domain_name2='domain_name_example', email_address2='email_address_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configure_anti_spam(client):
    """Test case for configure_anti_spam

    Configure anti-spam for mail zone
    """
    body = {"type":"none"}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/mailzones/{domain_name}/antispam'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configure_smtp_domain(client):
    """Test case for configure_smtp_domain

    Configure an extra smtp domain
    """
    body = {"enabled":True}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/mailzones/{domain_name}/smtpdomains/{hostname}'.format(hostname='hostname_example', domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_alias(client):
    """Test case for create_alias

    Create a new alias
    """
    body = {"email_address":"email_address","destinations":["destinations","destinations"]}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/mailzones/{domain_name}/aliases'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_catch_all(client):
    """Test case for create_catch_all

    Create a catch-all on the mail zone
    """
    body = {"email_address":"email_address"}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/mailzones/{domain_name}/catchall'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_smtp_domain(client):
    """Test case for create_smtp_domain

    Create an extra smtp domain
    """
    body = {"hostname":"hostname"}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/mailzones/{domain_name}/smtpdomains'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_alias(client):
    """Test case for delete_alias

    Delete a alias
    """
    params = [('domain_name', 'domain_name_example'),
                    ('email_address', 'email_address_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/mailzones/{domain_name}/aliases/{email_address}'.format(domain_name2='domain_name_example', email_address2='email_address_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_catch_all(client):
    """Test case for delete_catch_all

    Delete a catch-all on the mail zone
    """
    params = [('domain_name', 'domain_name_example'),
                    ('email_address', 'email_address_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/mailzones/{domain_name}/catchall/{email_address}'.format(domain_name2='domain_name_example', email_address2='email_address_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_smtp_domain(client):
    """Test case for delete_smtp_domain

    Delete an extra smtp domain
    """
    params = [('domain_name', 'domain_name_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/mailzones/{domain_name}/smtpdomains/{hostname}'.format(hostname='hostname_example', domain_name2='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mail_zone(client):
    """Test case for get_mail_zone

    Get the mail zone.
    """
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/mailzones/{domain_name}'.format(domain_name2='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

