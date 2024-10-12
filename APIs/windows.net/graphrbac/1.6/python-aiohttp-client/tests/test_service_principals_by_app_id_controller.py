# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server.models.service_principal_object_result import ServicePrincipalObjectResult


pytestmark = pytest.mark.asyncio

async def test_applications_get_service_principals_id_by_app_id(client):
    """Test case for applications_get_service_principals_id_by_app_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/servicePrincipalsByAppId/{application_id}/objectId'.format(tenant_id='tenant_id_example', application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

