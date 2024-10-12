# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact import Artifact
from openapi_server.models.artifact_container_sas import ArtifactContainerSas
from openapi_server.models.artifact_content_information import ArtifactContentInformation
from openapi_server.models.artifact_id_list import ArtifactIdList
from openapi_server.models.artifact_path_list import ArtifactPathList
from openapi_server.models.batch_artifact_content_information_result import BatchArtifactContentInformationResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.paginated_artifact_content_information_list import PaginatedArtifactContentInformationList
from openapi_server.models.paginated_artifact_list import PaginatedArtifactList


pytestmark = pytest.mark.asyncio

async def test_artifacts_batch_create_empty_artifacts(client):
    """Test case for artifacts_batch_create_empty_artifacts

    Create a batch of empty Artifacts.
    """
    artifact_paths = {"paths":[{"path":"path"},{"path":"path"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/batch/metadata'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        json=artifact_paths,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_batch_get_by_id(client):
    """Test case for artifacts_batch_get_by_id

    Get Batch Artifacts by Ids.
    """
    artifact_ids = {"artifactIds":["artifactIds","artifactIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/batch/metadata'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        json=artifact_ids,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_batch_get_storage_by_id(client):
    """Test case for artifacts_batch_get_storage_by_id

    Get Batch Artifacts storage by Ids.
    """
    artifact_ids = {"artifactIds":["artifactIds","artifactIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/storageuri/batch/metadata'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        json=artifact_ids,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_batch_ingest_from_sas(client):
    """Test case for artifacts_batch_ingest_from_sas

    Batch ingest using shared access signature.
    """
    artifact_container_sas = {"containerSas":"containerSas","artifactPrefix":"artifactPrefix","prefix":"prefix","containerUri":"containerUri"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/batch/ingest/containersas'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        json=artifact_container_sas,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_create(client):
    """Test case for artifacts_create

    Create Artifact.
    """
    artifact = {"container":"container","path":"path","origin":"origin","createdTime":"2000-01-23T04:56:07.000+00:00","artifactId":"artifactId","etag":"etag","dataPath":{"relativePath":"relativePath","dataStoreName":"dataStoreName","sqlDataPath":{"sqlStoredProcedureParams":[{"name":"name","type":"String","value":"value"},{"name":"name","type":"String","value":"value"}],"sqlStoredProcedureName":"sqlStoredProcedureName","sqlQuery":"sqlQuery","sqlTableName":"sqlTableName"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/metadata'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        json=artifact,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_delete_batch_meta_data(client):
    """Test case for artifacts_delete_batch_meta_data

    Delete Batch of Artifact Metadata.
    """
    artifact_paths = {"paths":[{"path":"path"},{"path":"path"}]}
    params = [('hardDelete', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/batch/metadata:delete'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        json=artifact_paths,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_delete_meta_data(client):
    """Test case for artifacts_delete_meta_data

    Delete Artifact Metadata.
    """
    params = [('path', 'path_example'),
                    ('hardDelete', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/metadata'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_delete_meta_data_in_container(client):
    """Test case for artifacts_delete_meta_data_in_container

    Delete Artifact Metadata.
    """
    params = [('hardDelete', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/batch'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_download(client):
    """Test case for artifacts_download

    Get Artifact content by Id.
    """
    params = [('path', 'path_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/content'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_get(client):
    """Test case for artifacts_get

    Get Artifact metadata by Id.
    """
    params = [('path', 'path_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/metadata'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_get_content_information(client):
    """Test case for artifacts_get_content_information

    Get Artifact content information.
    """
    params = [('path', 'path_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/contentinfo'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_get_sas(client):
    """Test case for artifacts_get_sas

    Get writable shared access signature for Artifact.
    """
    params = [('path', 'path_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/write'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_get_storage_content_information(client):
    """Test case for artifacts_get_storage_content_information

    Get Artifact storage content information.
    """
    params = [('path', 'path_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/contentinfo/storageuri'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_list_in_container(client):
    """Test case for artifacts_list_in_container

    Get Artifacts metadata in a container or path.
    """
    params = [('path', 'path_example'),
                    ('continuationToken', 'continuation_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_list_sas_by_prefix(client):
    """Test case for artifacts_list_sas_by_prefix

    Get shared access signature for an Artifact
    """
    params = [('path', 'path_example'),
                    ('continuationToken', 'continuation_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/prefix/contentinfo'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_list_storage_uri_by_prefix(client):
    """Test case for artifacts_list_storage_uri_by_prefix

    Get storage Uri for Artifacts in a path.
    """
    params = [('path', 'path_example'),
                    ('continuationToken', 'continuation_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/prefix/contentinfo/storageuri'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_register(client):
    """Test case for artifacts_register

    Create an Artifact for an existing data location.
    """
    artifact = {"container":"container","path":"path","origin":"origin","createdTime":"2000-01-23T04:56:07.000+00:00","artifactId":"artifactId","etag":"etag","dataPath":{"relativePath":"relativePath","dataStoreName":"dataStoreName","sqlDataPath":{"sqlStoredProcedureParams":[{"name":"name","type":"String","value":"value"},{"name":"name","type":"String","value":"value"}],"sqlStoredProcedureName":"sqlStoredProcedureName","sqlQuery":"sqlQuery","sqlTableName":"sqlTableName"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/register'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        json=artifact,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_artifacts_upload(client):
    """Test case for artifacts_upload

    Upload Artifact content.
    """
    content = '/path/to/file'
    params = [('path', 'path_example'),
                    ('index', 56),
                    ('append', False),
                    ('allowOverwrite', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/artifact/v2.0/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/artifacts/{origin}/{container}/content'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', origin='origin_example', container='container_example'),
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

