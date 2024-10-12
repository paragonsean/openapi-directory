# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_owner_parameters import AddOwnerParameters
from openapi_server.models.directory_object_list_result import DirectoryObjectListResult
from openapi_server.models.graph_error import GraphError


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_applications_add_owner(client):
    """Test case for applications_add_owner

    
    """
    body = {"url":"url"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{tenant_id}/applications/{application_object_id}/$links/owners'.format(application_object_id='application_object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_list_owners(client):
    """Test case for applications_list_owners

    Directory objects that are owners of the application.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/applications/{application_object_id}/owners'.format(application_object_id='application_object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_remove_owner(client):
    """Test case for applications_remove_owner

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{tenant_id}/applications/{application_object_id}/$links/owners/{owner_object_id}'.format(application_object_id='application_object_id_example', owner_object_id='owner_object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

