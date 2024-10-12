# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_meta_data import ArtifactMetaData
from openapi_server.models.artifact_search_results import ArtifactSearchResults
from openapi_server.models.error import Error
from openapi_server.models.update_state import UpdateState


pytestmark = pytest.mark.asyncio

async def test_create_artifact(client):
    """Test case for create_artifact

    Create artifact
    """
    params = [('ifExists', 'if_exists_example')]
    headers = { 
        'Accept': 'application/json',
        'x_registry_artifact_type': 'x_registry_artifact_type_example',
        'x_registry_artifact_id': 'x_registry_artifact_id_example',
    }
    response = await client.request(
        method='POST',
        path='/artifacts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_artifact(client):
    """Test case for delete_artifact

    Delete artifact
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/artifacts/{artifact_id}'.format(artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artifact_by_global_id(client):
    """Test case for get_artifact_by_global_id

    Get artifact by global ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ids/{global_id}'.format(global_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_artifact(client):
    """Test case for get_latest_artifact

    Get latest artifact
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/artifacts/{artifact_id}'.format(artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_artifacts(client):
    """Test case for list_artifacts

    List all artifact IDs
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/artifacts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_artifacts_0(client):
    """Test case for search_artifacts_0

    Search for artifacts
    """
    params = [('search', 'search_example'),
                    ('offset', 0),
                    ('limit', 20),
                    ('over', 'over_example'),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/search/artifacts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_artifact(client):
    """Test case for update_artifact

    Update artifact
    """
    headers = { 
        'Accept': 'application/json',
        'x_registry_artifact_type': 'x_registry_artifact_type_example',
    }
    response = await client.request(
        method='PUT',
        path='/artifacts/{artifact_id}'.format(artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_artifact_state(client):
    """Test case for update_artifact_state

    Update artifact state
    """
    body = {"state":"DISABLED"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/artifacts/{artifact_id}/state'.format(artifact_id='artifact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

