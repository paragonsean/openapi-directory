# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact import Artifact
from openapi_server.models.artifact_list import ArtifactList


pytestmark = pytest.mark.asyncio

async def test_published_artifacts_get(client):
    """Test case for published_artifacts_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{management_group_name}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}/versions/{version_id}/artifacts/{artifact_name}'.format(management_group_name='management_group_name_example', blueprint_name='blueprint_name_example', version_id='version_id_example', artifact_name='artifact_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_published_artifacts_list(client):
    """Test case for published_artifacts_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{management_group_name}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}/versions/{version_id}/artifacts'.format(management_group_name='management_group_name_example', blueprint_name='blueprint_name_example', version_id='version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

