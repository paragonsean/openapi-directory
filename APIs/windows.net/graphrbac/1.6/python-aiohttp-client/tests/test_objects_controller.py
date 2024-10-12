# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.directory_object_list_result import DirectoryObjectListResult
from openapi_server.models.get_objects_parameters import GetObjectsParameters


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_objects_get_objects_by_object_ids(client):
    """Test case for objects_get_objects_by_object_ids

    
    """
    body = {"types":["types","types"],"includeDirectoryObjectReferences":True,"objectIds":["objectIds","objectIds"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{tenant_id}/getObjectsByObjectIds'.format(tenant_id='tenant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

