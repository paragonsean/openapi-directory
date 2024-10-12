# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_meta_data import ArtifactMetaData
from openapi_server.models.editable_meta_data import EditableMetaData
from openapi_server.models.error import Error
from openapi_server.models.version_meta_data import VersionMetaData


pytestmark = pytest.mark.asyncio

async def test_delete_artifact_version_meta_data(client):
    """Test case for delete_artifact_version_meta_data

    Delete artifact version metadata
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/artifacts/{artifact_id}/versions/{version}/meta'.format(version=56, artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artifact_meta_data(client):
    """Test case for get_artifact_meta_data

    Get artifact metadata
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/artifacts/{artifact_id}/meta'.format(artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artifact_meta_data_by_content(client):
    """Test case for get_artifact_meta_data_by_content

    Get artifact metadata by content
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/artifacts/{artifact_id}/meta'.format(artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artifact_meta_data_by_global_id(client):
    """Test case for get_artifact_meta_data_by_global_id

    Get global artifact metadata
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ids/{global_id}/meta'.format(global_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artifact_version_meta_data(client):
    """Test case for get_artifact_version_meta_data

    Get artifact version metadata
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/artifacts/{artifact_id}/versions/{version}/meta'.format(version=56, artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_artifact_meta_data(client):
    """Test case for update_artifact_meta_data

    Update artifact metadata
    """
    body = openapi_server.EditableMetaData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/artifacts/{artifact_id}/meta'.format(artifact_id='artifact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_artifact_version_meta_data(client):
    """Test case for update_artifact_version_meta_data

    Update artifact version metadata
    """
    body = {"description":"The description of the artifact.","labels":["regional","global"],"name":"Artifact Name","properties":{"custom-1":"foo","custom-2":"bar"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/artifacts/{artifact_id}/versions/{version}/meta'.format(version=56, artifact_id='artifact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

