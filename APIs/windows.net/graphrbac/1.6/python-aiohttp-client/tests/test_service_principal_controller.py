# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server.models.service_principal import ServicePrincipal
from openapi_server.models.service_principal_create_parameters import ServicePrincipalCreateParameters
from openapi_server.models.service_principal_list_result import ServicePrincipalListResult
from openapi_server.models.service_principal_update_parameters import ServicePrincipalUpdateParameters


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_service_principals_create(client):
    """Test case for service_principals_create

    
    """
    body = {"appId":"appId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{tenant_id}/servicePrincipals'.format(tenant_id='tenant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_principals_delete(client):
    """Test case for service_principals_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{tenant_id}/servicePrincipals/{object_id}'.format(object_id='object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_principals_get(client):
    """Test case for service_principals_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/servicePrincipals/{object_id}'.format(object_id='object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_principals_list(client):
    """Test case for service_principals_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/servicePrincipals'.format(tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_service_principals_update(client):
    """Test case for service_principals_update

    
    """
    body = {"servicePrincipalType":"servicePrincipalType","keyCredentials":[{"customKeyIdentifier":"customKeyIdentifier","endDate":"2000-01-23T04:56:07.000+00:00","usage":"usage","keyId":"keyId","type":"type","value":"value","startDate":"2000-01-23T04:56:07.000+00:00"},{"customKeyIdentifier":"customKeyIdentifier","endDate":"2000-01-23T04:56:07.000+00:00","usage":"usage","keyId":"keyId","type":"type","value":"value","startDate":"2000-01-23T04:56:07.000+00:00"}],"appRoleAssignmentRequired":True,"accountEnabled":True,"passwordCredentials":[{"customKeyIdentifier":"customKeyIdentifier","endDate":"2000-01-23T04:56:07.000+00:00","keyId":"keyId","value":"value","startDate":"2000-01-23T04:56:07.000+00:00"},{"customKeyIdentifier":"customKeyIdentifier","endDate":"2000-01-23T04:56:07.000+00:00","keyId":"keyId","value":"value","startDate":"2000-01-23T04:56:07.000+00:00"}],"tags":["tags","tags"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/{tenant_id}/servicePrincipals/{object_id}'.format(object_id='object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

