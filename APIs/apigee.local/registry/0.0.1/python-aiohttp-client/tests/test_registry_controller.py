# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api import Api
from openapi_server.models.api_deployment import ApiDeployment
from openapi_server.models.api_spec import ApiSpec
from openapi_server.models.api_version import ApiVersion
from openapi_server.models.artifact import Artifact
from openapi_server.models.list_api_deployment_revisions_response import ListApiDeploymentRevisionsResponse
from openapi_server.models.list_api_deployments_response import ListApiDeploymentsResponse
from openapi_server.models.list_api_spec_revisions_response import ListApiSpecRevisionsResponse
from openapi_server.models.list_api_specs_response import ListApiSpecsResponse
from openapi_server.models.list_api_versions_response import ListApiVersionsResponse
from openapi_server.models.list_apis_response import ListApisResponse
from openapi_server.models.list_artifacts_response import ListArtifactsResponse
from openapi_server.models.rollback_api_deployment_request import RollbackApiDeploymentRequest
from openapi_server.models.rollback_api_spec_request import RollbackApiSpecRequest
from openapi_server.models.status import Status
from openapi_server.models.tag_api_deployment_revision_request import TagApiDeploymentRevisionRequest
from openapi_server.models.tag_api_spec_revision_request import TagApiSpecRevisionRequest


pytestmark = pytest.mark.asyncio

async def test_registry_create_api(client):
    """Test case for registry_create_api

    
    """
    body = {"recommendedVersion":"recommendedVersion","createTime":"2000-01-23T04:56:07.000+00:00","displayName":"displayName","name":"name","annotations":{"key":"annotations"},"description":"description","updateTime":"2000-01-23T04:56:07.000+00:00","availability":"availability","labels":{"key":"labels"},"recommendedDeployment":"recommendedDeployment"}
    params = [('apiId', 'api_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project}/locations/{location}/apis'.format(project='project_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_create_api_deployment(client):
    """Test case for registry_create_api_deployment

    
    """
    body = {"intendedAudience":"intendedAudience","displayName":"displayName","annotations":{"key":"annotations"},"description":"description","revisionCreateTime":"2000-01-23T04:56:07.000+00:00","labels":{"key":"labels"},"revisionId":"revisionId","createTime":"2000-01-23T04:56:07.000+00:00","name":"name","accessGuidance":"accessGuidance","endpointUri":"endpointUri","externalChannelUri":"externalChannelUri","revisionUpdateTime":"2000-01-23T04:56:07.000+00:00","apiSpecRevision":"apiSpecRevision"}
    params = [('apiDeploymentId', 'api_deployment_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/deployments'.format(project='project_example', location='location_example', api='api_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_create_api_spec(client):
    """Test case for registry_create_api_spec

    
    """
    body = {"annotations":{"key":"annotations"},"description":"description","mimeType":"mimeType","revisionCreateTime":"2000-01-23T04:56:07.000+00:00","labels":{"key":"labels"},"sizeBytes":0,"revisionId":"revisionId","filename":"filename","contents":"contents","createTime":"2000-01-23T04:56:07.000+00:00","sourceUri":"sourceUri","name":"name","hash":"hash","revisionUpdateTime":"2000-01-23T04:56:07.000+00:00"}
    params = [('apiSpecId', 'api_spec_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs'.format(project='project_example', location='location_example', api='api_example', version='version_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_create_api_version(client):
    """Test case for registry_create_api_version

    
    """
    body = {"createTime":"2000-01-23T04:56:07.000+00:00","displayName":"displayName","name":"name","annotations":{"key":"annotations"},"description":"description","updateTime":"2000-01-23T04:56:07.000+00:00","state":"state","labels":{"key":"labels"}}
    params = [('apiVersionId', 'api_version_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions'.format(project='project_example', location='location_example', api='api_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_create_artifact(client):
    """Test case for registry_create_artifact

    
    """
    body = {"contents":"contents","createTime":"2000-01-23T04:56:07.000+00:00","name":"name","updateTime":"2000-01-23T04:56:07.000+00:00","mimeType":"mimeType","hash":"hash","sizeBytes":0}
    params = [('artifactId', 'artifact_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project}/locations/{location}/artifacts'.format(project='project_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_delete_api(client):
    """Test case for registry_delete_api

    
    """
    params = [('force', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/projects/{project}/locations/{location}/apis/{api}'.format(project='project_example', location='location_example', api='api_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_delete_api_deployment(client):
    """Test case for registry_delete_api_deployment

    
    """
    params = [('force', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}'.format(project='project_example', location='location_example', api='api_example', deployment='deployment_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_delete_api_deployment_revision(client):
    """Test case for registry_delete_api_deployment_revision

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deploymentdelete_revisio}'.format(project='project_example', location='location_example', api='api_example', deployment='deployment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_delete_api_spec(client):
    """Test case for registry_delete_api_spec

    
    """
    params = [('force', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}'.format(project='project_example', location='location_example', api='api_example', version='version_example', spec='spec_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_delete_api_spec_revision(client):
    """Test case for registry_delete_api_spec_revision

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{specdelete_revisio}'.format(project='project_example', location='location_example', api='api_example', version='version_example', spec='spec_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_delete_api_version(client):
    """Test case for registry_delete_api_version

    
    """
    params = [('force', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}'.format(project='project_example', location='location_example', api='api_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_delete_artifact(client):
    """Test case for registry_delete_artifact

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/projects/{project}/locations/{location}/artifacts/{artifact}'.format(project='project_example', location='location_example', artifact='artifact_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_get_api(client):
    """Test case for registry_get_api

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/apis/{api}'.format(project='project_example', location='location_example', api='api_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_get_api_deployment(client):
    """Test case for registry_get_api_deployment

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}'.format(project='project_example', location='location_example', api='api_example', deployment='deployment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_get_api_spec(client):
    """Test case for registry_get_api_spec

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}'.format(project='project_example', location='location_example', api='api_example', version='version_example', spec='spec_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_get_api_spec_contents(client):
    """Test case for registry_get_api_spec_contents

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{specget_content}'.format(project='project_example', location='location_example', api='api_example', version='version_example', spec='spec_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_get_api_version(client):
    """Test case for registry_get_api_version

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}'.format(project='project_example', location='location_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_get_artifact(client):
    """Test case for registry_get_artifact

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/artifacts/{artifact}'.format(project='project_example', location='location_example', artifact='artifact_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_get_artifact_contents(client):
    """Test case for registry_get_artifact_contents

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/artifacts/{artifactget_content}'.format(project='project_example', location='location_example', artifact='artifact_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_list_api_deployment_revisions(client):
    """Test case for registry_list_api_deployment_revisions

    
    """
    params = [('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deploymentlist_revision}'.format(project='project_example', location='location_example', api='api_example', deployment='deployment_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_list_api_deployments(client):
    """Test case for registry_list_api_deployments

    
    """
    params = [('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/deployments'.format(project='project_example', location='location_example', api='api_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_list_api_spec_revisions(client):
    """Test case for registry_list_api_spec_revisions

    
    """
    params = [('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{speclist_revision}'.format(project='project_example', location='location_example', api='api_example', version='version_example', spec='spec_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_list_api_specs(client):
    """Test case for registry_list_api_specs

    
    """
    params = [('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs'.format(project='project_example', location='location_example', api='api_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_list_api_versions(client):
    """Test case for registry_list_api_versions

    
    """
    params = [('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions'.format(project='project_example', location='location_example', api='api_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_list_apis(client):
    """Test case for registry_list_apis

    
    """
    params = [('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/apis'.format(project='project_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_list_artifacts(client):
    """Test case for registry_list_artifacts

    
    """
    params = [('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{project}/locations/{location}/artifacts'.format(project='project_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_replace_artifact(client):
    """Test case for registry_replace_artifact

    
    """
    body = {"contents":"contents","createTime":"2000-01-23T04:56:07.000+00:00","name":"name","updateTime":"2000-01-23T04:56:07.000+00:00","mimeType":"mimeType","hash":"hash","sizeBytes":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/projects/{project}/locations/{location}/artifacts/{artifact}'.format(project='project_example', location='location_example', artifact='artifact_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_rollback_api_deployment(client):
    """Test case for registry_rollback_api_deployment

    
    """
    body = {"revisionId":"revisionId","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deploymentrollbac}'.format(project='project_example', location='location_example', api='api_example', deployment='deployment_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_rollback_api_spec(client):
    """Test case for registry_rollback_api_spec

    
    """
    body = {"revisionId":"revisionId","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{specrollbac}'.format(project='project_example', location='location_example', api='api_example', version='version_example', spec='spec_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_tag_api_deployment_revision(client):
    """Test case for registry_tag_api_deployment_revision

    
    """
    body = {"name":"name","tag":"tag"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deploymenttag_revisio}'.format(project='project_example', location='location_example', api='api_example', deployment='deployment_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_tag_api_spec_revision(client):
    """Test case for registry_tag_api_spec_revision

    
    """
    body = {"name":"name","tag":"tag"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spectag_revisio}'.format(project='project_example', location='location_example', api='api_example', version='version_example', spec='spec_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_update_api(client):
    """Test case for registry_update_api

    
    """
    body = {"recommendedVersion":"recommendedVersion","createTime":"2000-01-23T04:56:07.000+00:00","displayName":"displayName","name":"name","annotations":{"key":"annotations"},"description":"description","updateTime":"2000-01-23T04:56:07.000+00:00","availability":"availability","labels":{"key":"labels"},"recommendedDeployment":"recommendedDeployment"}
    params = [('updateMask', 'update_mask_example'),
                    ('allowMissing', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/projects/{project}/locations/{location}/apis/{api}'.format(project='project_example', location='location_example', api='api_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_update_api_deployment(client):
    """Test case for registry_update_api_deployment

    
    """
    body = {"intendedAudience":"intendedAudience","displayName":"displayName","annotations":{"key":"annotations"},"description":"description","revisionCreateTime":"2000-01-23T04:56:07.000+00:00","labels":{"key":"labels"},"revisionId":"revisionId","createTime":"2000-01-23T04:56:07.000+00:00","name":"name","accessGuidance":"accessGuidance","endpointUri":"endpointUri","externalChannelUri":"externalChannelUri","revisionUpdateTime":"2000-01-23T04:56:07.000+00:00","apiSpecRevision":"apiSpecRevision"}
    params = [('updateMask', 'update_mask_example'),
                    ('allowMissing', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}'.format(project='project_example', location='location_example', api='api_example', deployment='deployment_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_update_api_spec(client):
    """Test case for registry_update_api_spec

    
    """
    body = {"annotations":{"key":"annotations"},"description":"description","mimeType":"mimeType","revisionCreateTime":"2000-01-23T04:56:07.000+00:00","labels":{"key":"labels"},"sizeBytes":0,"revisionId":"revisionId","filename":"filename","contents":"contents","createTime":"2000-01-23T04:56:07.000+00:00","sourceUri":"sourceUri","name":"name","hash":"hash","revisionUpdateTime":"2000-01-23T04:56:07.000+00:00"}
    params = [('updateMask', 'update_mask_example'),
                    ('allowMissing', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}'.format(project='project_example', location='location_example', api='api_example', version='version_example', spec='spec_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_update_api_version(client):
    """Test case for registry_update_api_version

    
    """
    body = {"createTime":"2000-01-23T04:56:07.000+00:00","displayName":"displayName","name":"name","annotations":{"key":"annotations"},"description":"description","updateTime":"2000-01-23T04:56:07.000+00:00","state":"state","labels":{"key":"labels"}}
    params = [('updateMask', 'update_mask_example'),
                    ('allowMissing', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}'.format(project='project_example', location='location_example', api='api_example', version='version_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

