# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.license_lifecycle_state import LicenseLifecycleState
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_classifications_license_lifecycle_states_get(client):
    """Test case for classifications_license_lifecycle_states_get

    Retrieve a list of license lifecycle states
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/classifications/license-lifecycle-states',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

