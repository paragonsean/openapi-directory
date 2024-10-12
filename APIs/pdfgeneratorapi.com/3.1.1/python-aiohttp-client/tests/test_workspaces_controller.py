# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_template200_response import DeleteTemplate200Response
from openapi_server.models.get_templates401_response import GetTemplates401Response
from openapi_server.models.get_templates403_response import GetTemplates403Response
from openapi_server.models.get_templates404_response import GetTemplates404Response
from openapi_server.models.get_templates422_response import GetTemplates422Response
from openapi_server.models.get_templates500_response import GetTemplates500Response
from openapi_server.models.get_workspace200_response import GetWorkspace200Response


pytestmark = pytest.mark.asyncio

async def test_delete_workspace(client):
    """Test case for delete_workspace

    Delete workspace
    """
    params = [('workspaceId', 'demo.example@actualreports.com')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/workspaces/workspaceId',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workspace(client):
    """Test case for get_workspace

    Get workspace
    """
    params = [('workspaceId', 'demo.example@actualreports.com')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/workspaces/workspaceId',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

