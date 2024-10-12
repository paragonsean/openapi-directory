# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rsa_mfa_server_config import RsaMfaServerConfig
from openapi_server.models.rsa_mfa_server_config_update import RsaMfaServerConfigUpdate
from openapi_server.models.rsa_mfa_server_detail import RsaMfaServerDetail
from openapi_server.models.rsa_mfa_server_detail_list_response import RsaMfaServerDetailListResponse


pytestmark = pytest.mark.asyncio

async def test_create_rsa_mfa_server(client):
    """Test case for create_rsa_mfa_server

    Register a new RSA server
    """
    body = {"baseUrl":"baseUrl","clientId":"clientId","certificateId":"certificateId","name":"name","restApiAccessId":"restApiAccessId","ldapUsernameAttribute":"ldapUsernameAttribute","restApiKey":"restApiKey","timeout":0,"assurancePolicyName":"assurancePolicyName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mfa/rsa/server',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_rsa_mfa_server(client):
    """Test case for delete_rsa_mfa_server

    Delete RSA server
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/mfa/rsa/server/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rsa_mfa_server(client):
    """Test case for get_rsa_mfa_server

    Get RSA server configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mfa/rsa/server/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_rsa_mfa_servers(client):
    """Test case for query_rsa_mfa_servers

    Get RSA server configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mfa/rsa/server',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_rsa_mfa_server(client):
    """Test case for update_rsa_mfa_server

    Update RSA server configuration
    """
    body = {"baseUrl":"baseUrl","clientId":"clientId","certificateId":"certificateId","name":"name","restApiAccessId":"restApiAccessId","ldapUsernameAttribute":"ldapUsernameAttribute","restApiKey":"restApiKey","assurancePolicyName":"assurancePolicyName","timeout":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/mfa/rsa/server/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

