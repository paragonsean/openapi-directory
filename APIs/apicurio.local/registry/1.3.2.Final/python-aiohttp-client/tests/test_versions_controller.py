# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.update_state import UpdateState
from openapi_server.models.version_meta_data import VersionMetaData
from openapi_server.models.version_search_results import VersionSearchResults


pytestmark = pytest.mark.asyncio

async def test_create_artifact_version(client):
    """Test case for create_artifact_version

    Create artifact version
    """
    headers = { 
        'Accept': 'application/json',
        'x_registry_artifact_type': 'x_registry_artifact_type_example',
    }
    response = await client.request(
        method='POST',
        path='/artifacts/{artifact_id}/versions'.format(artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artifact_version(client):
    """Test case for get_artifact_version

    Get artifact version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/artifacts/{artifact_id}/versions/{version}'.format(version=56, artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_artifact_versions(client):
    """Test case for list_artifact_versions

    List artifact versions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/artifacts/{artifact_id}/versions'.format(artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_versions_0(client):
    """Test case for search_versions_0

    Search artifact versions
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/search/artifacts/{artifact_id}/versions'.format(artifact_id='artifact_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_artifact_version_state(client):
    """Test case for update_artifact_version_state

    Update artifact version state
    """
    body = {"state":"DISABLED"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/artifacts/{artifact_id}/versions/{version}/state'.format(version=56, artifact_id='artifact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

