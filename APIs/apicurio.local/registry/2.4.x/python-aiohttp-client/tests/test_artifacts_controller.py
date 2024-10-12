# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_content import ArtifactContent
from openapi_server.models.artifact_meta_data import ArtifactMetaData
from openapi_server.models.artifact_reference import ArtifactReference
from openapi_server.models.artifact_search_results import ArtifactSearchResults
from openapi_server.models.error import Error
from openapi_server.models.if_exists import IfExists
from openapi_server.models.rule_violation_error import RuleViolationError
from openapi_server.models.sort_by import SortBy
from openapi_server.models.sort_order import SortOrder
from openapi_server.models.update_state import UpdateState


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_artifact(client):
    """Test case for create_artifact

    Create artifact
    """
    body = {"components":{"schemas":{"Widget":{"description":"A sample data type.","example":{"property-1":"value1","property-2":true},"properties":{"property-1":{"type":"string"},"property-2":{"type":"boolean"}},"title":"Root Type for Widget","type":"object"}}},"info":{"description":"An example API design using OpenAPI.","title":"Empty API","version":"1.0.7"},"openapi":"3.0.2","paths":{"/widgets":{"get":{"responses":{"200":{"content":{"application/json":{"schema":{"items":{"type":"string"},"type":"array"}}},"description":"All widgets"}},"summary":"Get widgets"}}}}
    params = [('ifExists', openapi_server.IfExists()),
                    ('canonical', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/create.extended+json',
        'x_registry_artifact_type': 'x_registry_artifact_type_example',
        'x_registry_artifact_id': 'x_registry_artifact_id_example',
        'x_registry_version': 'x_registry_version_example',
        'x_registry_description': 'x_registry_description_example',
        'x_registry_description_encoded': 'x_registry_description_encoded_example',
        'x_registry_name': 'x_registry_name_example',
        'x_registry_name_encoded': 'x_registry_name_encoded_example',
        'x_registry_content_hash': 'x_registry_content_hash_example',
        'x_registry_hash_algorithm': 'x_registry_hash_algorithm_example',
    }
    response = await client.request(
        method='POST',
        path='/groups/{group_id}/artifacts'.format(group_id='group_id_example'),
        headers=headers,
        json=body,
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
        path='/groups/{group_id}/artifacts/{artifact_id}'.format(group_id='group_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_artifacts_in_group(client):
    """Test case for delete_artifacts_in_group

    Delete artifacts in group
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/{group_id}/artifacts'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_content_by_global_id(client):
    """Test case for get_content_by_global_id

    Get artifact by global ID
    """
    params = [('dereference', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ids/globalIds/{global_id}'.format(global_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_content_by_hash(client):
    """Test case for get_content_by_hash

    Get artifact content by SHA-256 hash
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ids/contentHashes/{content_hash}'.format(content_hash='content_hash_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_content_by_id(client):
    """Test case for get_content_by_id

    Get artifact content by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ids/contentIds/{content_id}'.format(content_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_artifact(client):
    """Test case for get_latest_artifact

    Get latest artifact
    """
    params = [('dereference', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}/artifacts/{artifact_id}'.format(group_id='group_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_artifacts_in_group(client):
    """Test case for list_artifacts_in_group

    List artifacts in group
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('order', openapi_server.SortOrder()),
                    ('orderby', openapi_server.SortBy())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}/artifacts'.format(group_id='group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_by_content_hash(client):
    """Test case for references_by_content_hash

    List artifact references by hash
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ids/contentHashes/{content_hash}/references'.format(content_hash='content_hash_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_by_content_id(client):
    """Test case for references_by_content_id

    List artifact references by content ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ids/contentIds/{content_id}/references'.format(content_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_by_global_id(client):
    """Test case for references_by_global_id

    List artifact references by global ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ids/globalIds/{global_id}/references'.format(global_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_artifacts_0(client):
    """Test case for search_artifacts_0

    Search for artifacts
    """
    params = [('name', 'name_example'),
                    ('offset', 0),
                    ('limit', 20),
                    ('order', openapi_server.SortOrder()),
                    ('orderby', openapi_server.SortBy()),
                    ('labels', ['labels_example']),
                    ('properties', ['properties_example']),
                    ('description', 'description_example'),
                    ('group', 'group_example'),
                    ('globalId', 56),
                    ('contentId', 56)]
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

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_search_artifacts_by_content_0(client):
    """Test case for search_artifacts_by_content_0

    Search for artifacts by content
    """
    body = '/path/to/file'
    params = [('canonical', True),
                    ('artifactType', 'artifact_type_example'),
                    ('offset', 0),
                    ('limit', 20),
                    ('order', 'order_example'),
                    ('orderby', 'orderby_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/search/artifacts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_artifact(client):
    """Test case for update_artifact

    Update artifact
    """
    body = {"components":{"schemas":{"Widget":{"description":"A sample data type.","example":{"property-1":"value1","property-2":true},"properties":{"property-1":{"type":"string"},"property-2":{"type":"boolean"}},"title":"Root Type for Widget","type":"object"}}},"info":{"description":"An example API design using OpenAPI.","title":"Empty API","version":"1.0.7"},"openapi":"3.0.2","paths":{"/widgets":{"get":{"responses":{"200":{"content":{"application/json":{"schema":{"items":{"type":"string"},"type":"array"}}},"description":"All widgets"}},"summary":"Get widgets"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/create.extended+json',
        'x_registry_version': 'x_registry_version_example',
        'x_registry_name': 'x_registry_name_example',
        'x_registry_name_encoded': 'x_registry_name_encoded_example',
        'x_registry_description': 'x_registry_description_example',
        'x_registry_description_encoded': 'x_registry_description_encoded_example',
    }
    response = await client.request(
        method='PUT',
        path='/groups/{group_id}/artifacts/{artifact_id}'.format(group_id='group_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        json=body,
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
        path='/groups/{group_id}/artifacts/{artifact_id}/state'.format(group_id='group_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

