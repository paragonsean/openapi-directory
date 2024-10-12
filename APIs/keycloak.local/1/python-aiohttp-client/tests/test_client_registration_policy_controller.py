# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.component_type_representation import ComponentTypeRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_client_registration_policy_providers_get(client):
    """Test case for realm_client_registration_policy_providers_get

    Base path for retrieve providers with the configProperties properly filled
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-registration-policy/providers'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

