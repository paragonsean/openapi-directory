# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_content import ArtifactContent
from openapi_server.models.artifact_reference import ArtifactReference
from openapi_server.models.error import Error
from openapi_server.models.rule_violation_error import RuleViolationError
from openapi_server.models.update_state import UpdateState
from openapi_server.models.version_meta_data import VersionMetaData
from openapi_server.models.version_search_results import VersionSearchResults


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_artifact_version(client):
    """Test case for create_artifact_version

    Create artifact version
    """
    body = {"components":{"schemas":{"Widget":{"description":"A sample data type.","example":{"property-1":"value1","property-2":true},"properties":{"property-1":{"type":"string"},"property-2":{"type":"boolean"}},"title":"Root Type for Widget","type":"object"}}},"info":{"description":"An example API design using OpenAPI.","title":"Empty API","version":"1.0.7"},"openapi":"3.0.2","paths":{"/widgets":{"get":{"responses":{"200":{"content":{"application/json":{"schema":{"items":{"type":"string"},"type":"array"}}},"description":"All widgets"}},"summary":"Get widgets"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/create.extended+json',
        'x_registry_version': 'x_registry_version_example',
        'x_registry_name': 'x_registry_name_example',
        'x_registry_description': 'x_registry_description_example',
        'x_registry_description_encoded': 'x_registry_description_encoded_example',
        'x_registry_name_encoded': 'x_registry_name_encoded_example',
    }
    response = await client.request(
        method='POST',
        path='/groups/{group_id}/artifacts/{artifact_id}/versions'.format(group_id='group_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_artifact_version(client):
    """Test case for delete_artifact_version

    Delete artifact version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/{group_id}/artifacts/{artifact_id}/versions/{version}'.format(group_id='group_id_example', artifact_id='artifact_id_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artifact_version(client):
    """Test case for get_artifact_version

    Get artifact version
    """
    params = [('dereference', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}/artifacts/{artifact_id}/versions/{version}'.format(group_id='group_id_example', artifact_id='artifact_id_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artifact_version_references(client):
    """Test case for get_artifact_version_references

    Get artifact version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}/artifacts/{artifact_id}/versions/{version}/references'.format(group_id='group_id_example', artifact_id='artifact_id_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_artifact_versions(client):
    """Test case for list_artifact_versions

    List artifact versions
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}/artifacts/{artifact_id}/versions'.format(group_id='group_id_example', artifact_id='artifact_id_example'),
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
        path='/groups/{group_id}/artifacts/{artifact_id}/versions/{version}/state'.format(group_id='group_id_example', artifact_id='artifact_id_example', version='version_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

