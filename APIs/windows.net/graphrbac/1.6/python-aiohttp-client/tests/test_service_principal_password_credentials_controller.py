# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server.models.password_credential_list_result import PasswordCredentialListResult
from openapi_server.models.password_credentials_update_parameters import PasswordCredentialsUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_service_principals_list_password_credentials(client):
    """Test case for service_principals_list_password_credentials

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/servicePrincipals/{object_id}/passwordCredentials'.format(object_id='object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_service_principals_update_password_credentials(client):
    """Test case for service_principals_update_password_credentials

    
    """
    body = {"value":[{"customKeyIdentifier":"customKeyIdentifier","endDate":"2000-01-23T04:56:07.000+00:00","keyId":"keyId","value":"value","startDate":"2000-01-23T04:56:07.000+00:00"},{"customKeyIdentifier":"customKeyIdentifier","endDate":"2000-01-23T04:56:07.000+00:00","keyId":"keyId","value":"value","startDate":"2000-01-23T04:56:07.000+00:00"}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/{tenant_id}/servicePrincipals/{object_id}/passwordCredentials'.format(object_id='object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

