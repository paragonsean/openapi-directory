# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.who_is_blueprint_contract import WhoIsBlueprintContract


pytestmark = pytest.mark.asyncio

async def test_assignments_who_is_blueprint(client):
    """Test case for assignments_who_is_blueprint

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignment_name}/WhoIsBlueprint'.format(scope='scope_example', assignment_name='assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

