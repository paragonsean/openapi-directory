# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact import Artifact
from openapi_server.models.artifact_list import ArtifactList


pytestmark = pytest.mark.asyncio

async def test_artifacts_create_or_update(client):
    """Test case for artifacts_create_or_update

    
    """
    artifact = {"kind":"template"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}/artifacts/{artifact_name}'.format(scope='scope_example', blueprint_name='blueprint_name_example', artifact_name='artifact_name_example'),
        headers=headers,
        json=artifact,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_delete(client):
    """Test case for artifacts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}/artifacts/{artifact_name}'.format(scope='scope_example', blueprint_name='blueprint_name_example', artifact_name='artifact_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_get(client):
    """Test case for artifacts_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}/artifacts/{artifact_name}'.format(scope='scope_example', blueprint_name='blueprint_name_example', artifact_name='artifact_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_list(client):
    """Test case for artifacts_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Blueprint/blueprints/{blueprint_name}/artifacts'.format(scope='scope_example', blueprint_name='blueprint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

