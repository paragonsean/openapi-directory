# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain_registration_provider_list_operations200_response import DomainRegistrationProviderListOperations200Response
from openapi_server.models.domain_registration_provider_list_operations_default_response import DomainRegistrationProviderListOperationsDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_domain_registration_provider_list_operations(client):
    """Test case for domain_registration_provider_list_operations

    Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.DomainRegistration/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

