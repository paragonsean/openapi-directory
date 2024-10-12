# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.typeahead_for_workspace200_response import TypeaheadForWorkspace200Response


pytestmark = pytest.mark.asyncio

async def test_typeahead_for_workspace(client):
    """Test case for typeahead_for_workspace

    Get objects via typeahead
    """
    params = [('resource_type', user),
                    ('type', user),
                    ('query', 'Greg'),
                    ('count', 20),
                    ('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/workspaces/{workspace_gid}/typeahead'.format(workspace_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

