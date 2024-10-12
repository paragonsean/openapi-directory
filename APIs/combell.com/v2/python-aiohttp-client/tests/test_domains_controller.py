# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server.models.domain_detail import DomainDetail
from openapi_server.models.edit_domain_will_renew_request import EditDomainWillRenewRequest
from openapi_server.models.edit_name_servers import EditNameServers
from openapi_server.models.register_domain import RegisterDomain
from openapi_server.models.transfer_domain import TransferDomain


pytestmark = pytest.mark.asyncio

async def test_configure_domain(client):
    """Test case for configure_domain

    Edit domain name renew state
    """
    body = {"will_renew":True}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/domains/{domain_name}/renew'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_name_servers(client):
    """Test case for edit_name_servers

    Edit domain name servers
    """
    body = {"domain_name":"domain_name","name_servers":["name_servers","name_servers"]}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/domains/{domain_name}/nameservers'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain(client):
    """Test case for get_domain

    Details of a domain
    """
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/domains/{domain_name}'.format(domain_name2='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domains(client):
    """Test case for get_domains

    Overviews of domains
    """
    params = [('skip', 56),
                    ('take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/domains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register(client):
    """Test case for register

    Register a domain
    """
    body = {"domain_name":"domain_name","name_servers":["name_servers","name_servers"],"registrant":{"address":"address","enterprise_number":"enterprise_number","city":"city","last_name":"last_name","country_code":"country_code","language_code":"language_code","phone":"phone","company_name":"company_name","extra_fields":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"fax":"fax","postal_code":"postal_code","first_name":"first_name","email":"email"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/domains/registrations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transfer(client):
    """Test case for transfer

    Transfer a domain
    """
    body = {"domain_name":"domain_name","name_servers":["name_servers","name_servers"],"registrant":{"address":"address","enterprise_number":"enterprise_number","city":"city","last_name":"last_name","country_code":"country_code","language_code":"language_code","phone":"phone","company_name":"company_name","extra_fields":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"fax":"fax","postal_code":"postal_code","first_name":"first_name","email":"email"},"auth_code":"auth_code"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/domains/transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

