# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_content import ArtifactContent
from openapi_server.models.artifact_meta_data import ArtifactMetaData
from openapi_server.models.artifact_owner import ArtifactOwner
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
        path='/groups/{group_id}/artifacts/{artifact_id}/versions/{version}/meta'.format(group_id='group_id_example', artifact_id='artifact_id_example', version='version_example'),
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
        path='/groups/{group_id}/artifacts/{artifact_id}/meta'.format(group_id='group_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artifact_owner(client):
    """Test case for get_artifact_owner

    Get artifact owner
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}/artifacts/{artifact_id}/owner'.format(group_id='group_id_example', artifact_id='artifact_id_example'),
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
        path='/groups/{group_id}/artifacts/{artifact_id}/versions/{version}/meta'.format(group_id='group_id_example', artifact_id='artifact_id_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_artifact_version_meta_data_by_content(client):
    """Test case for get_artifact_version_meta_data_by_content

    Get artifact version metadata by content
    """
    body = {"components":{"schemas":{"Widget":{"description":"A sample data type.","example":{"property-1":"value1","property-2":true},"properties":{"property-1":{"type":"string"},"property-2":{"type":"boolean"}},"title":"Root Type for Widget","type":"object"}}},"info":{"description":"An example API design using OpenAPI.","title":"Empty API","version":"1.0.7"},"openapi":"3.0.2","paths":{"/widgets":{"get":{"responses":{"200":{"content":{"application/json":{"schema":{"items":{"type":"string"},"type":"array"}}},"description":"All widgets"}},"summary":"Get widgets"}}}}
    params = [('canonical', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/get.extended+json',
    }
    response = await client.request(
        method='POST',
        path='/groups/{group_id}/artifacts/{artifact_id}/meta'.format(group_id='group_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_artifact_meta_data(client):
    """Test case for update_artifact_meta_data

    Update artifact metadata
    """
    body = {"description":"The description of the artifact.","labels":["regional","global"],"name":"Artifact Name","properties":{"custom-1":"foo","custom-2":"bar"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/groups/{group_id}/artifacts/{artifact_id}/meta'.format(group_id='group_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_artifact_owner(client):
    """Test case for update_artifact_owner

    Update artifact owner
    """
    body = {"owner":"bwayne"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/groups/{group_id}/artifacts/{artifact_id}/owner'.format(group_id='group_id_example', artifact_id='artifact_id_example'),
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
        path='/groups/{group_id}/artifacts/{artifact_id}/versions/{version}/meta'.format(group_id='group_id_example', artifact_id='artifact_id_example', version='version_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

