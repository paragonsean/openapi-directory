# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.branch_configurations_delete200_response import BranchConfigurationsDelete200Response
from openapi_server.models.code_push_acquisition_get_acquisition_status200_response import CodePushAcquisitionGetAcquisitionStatus200Response
from openapi_server.models.code_push_acquisition_update_check200_response import CodePushAcquisitionUpdateCheck200Response
from openapi_server.models.code_push_acquisition_update_deploy_status_request import CodePushAcquisitionUpdateDeployStatusRequest
from openapi_server.models.code_push_deployment_metrics_get200_response_inner import CodePushDeploymentMetricsGet200ResponseInner
from openapi_server.models.code_push_deployment_release_rollback_request import CodePushDeploymentReleaseRollbackRequest
from openapi_server.models.code_push_deployment_releases_create_request import CodePushDeploymentReleasesCreateRequest
from openapi_server.models.code_push_deployment_upload_create200_response import CodePushDeploymentUploadCreate200Response
from openapi_server.models.code_push_deployments_list200_response_inner import CodePushDeploymentsList200ResponseInner
from openapi_server.models.code_push_deployments_list200_response_inner_latest_release import CodePushDeploymentsList200ResponseInnerLatestRelease
from openapi_server.models.code_push_deployments_promote_request import CodePushDeploymentsPromoteRequest
from openapi_server.models.code_push_deployments_update_request import CodePushDeploymentsUpdateRequest
from openapi_server.models.deployment_releases_update_request import DeploymentReleasesUpdateRequest
from openapi_server.models.legacy_code_push_acquisition_update_check200_response import LegacyCodePushAcquisitionUpdateCheck200Response
from openapi_server.models.legacy_code_push_acquisition_update_installs_status_request import LegacyCodePushAcquisitionUpdateInstallsStatusRequest


pytestmark = pytest.mark.asyncio

async def test_code_push_acquisition_get_acquisition_status(client):
    """Test case for code_push_acquisition_get_acquisition_status

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/public/codepush/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_acquisition_update_check(client):
    """Test case for code_push_acquisition_update_check

    
    """
    params = [('deployment_key', 'deployment_key_example'),
                    ('app_version', 'app_version_example'),
                    ('package_hash', 'package_hash_example'),
                    ('label', 'label_example'),
                    ('client_unique_id', 'client_unique_id_example'),
                    ('is_companion', True),
                    ('previous_label_or_app_version', 'previous_label_or_app_version_example'),
                    ('previous_deployment_key', 'previous_deployment_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/public/codepush/update_check',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_acquisition_update_deploy_status(client):
    """Test case for code_push_acquisition_update_deploy_status

    
    """
    body = openapi_server.CodePushAcquisitionUpdateDeployStatusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/public/codepush/report_status/deploy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_acquisition_update_download_status(client):
    """Test case for code_push_acquisition_update_download_status

    
    """
    body = openapi_server.CodePushAcquisitionUpdateDeployStatusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/public/codepush/report_status/download',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployment_metrics_get(client):
    """Test case for code_push_deployment_metrics_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/metrics'.format(deployment_name='deployment_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployment_release_rollback(client):
    """Test case for code_push_deployment_release_rollback

    
    """
    body = openapi_server.CodePushDeploymentReleaseRollbackRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/rollback_release'.format(deployment_name='deployment_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployment_releases_create(client):
    """Test case for code_push_deployment_releases_create

    
    """
    body = openapi_server.CodePushDeploymentReleasesCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases'.format(deployment_name='deployment_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployment_releases_delete(client):
    """Test case for code_push_deployment_releases_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases'.format(deployment_name='deployment_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployment_releases_get(client):
    """Test case for code_push_deployment_releases_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases'.format(deployment_name='deployment_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployment_upload_create(client):
    """Test case for code_push_deployment_upload_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/uploads'.format(deployment_name='deployment_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployments_create(client):
    """Test case for code_push_deployments_create

    
    """
    body = openapi_server.CodePushDeploymentsList200ResponseInner()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployments_delete(client):
    """Test case for code_push_deployments_delete

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}'.format(deployment_name='deployment_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployments_get(client):
    """Test case for code_push_deployments_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}'.format(deployment_name='deployment_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployments_list(client):
    """Test case for code_push_deployments_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployments_promote(client):
    """Test case for code_push_deployments_promote

    
    """
    body = openapi_server.CodePushDeploymentsPromoteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/promote_release/{promote_deployment_name}'.format(deployment_name='deployment_name_example', promote_deployment_name='promote_deployment_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_code_push_deployments_update(client):
    """Test case for code_push_deployments_update

    
    """
    body = openapi_server.CodePushDeploymentsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}'.format(deployment_name='deployment_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_releases_update(client):
    """Test case for deployment_releases_update

    
    """
    body = openapi_server.DeploymentReleasesUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases/{release_label}'.format(deployment_name='deployment_name_example', release_label='release_label_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_legacy_code_push_acquisition_update_check(client):
    """Test case for legacy_code_push_acquisition_update_check

    
    """
    params = [('deploymentKey', 'deployment_key_example'),
                    ('appVersion', 'app_version_example'),
                    ('packageHash', 'package_hash_example'),
                    ('label', 'label_example'),
                    ('clientUniqueId', 'client_unique_id_example'),
                    ('isCompanion', 'is_companion_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/legacy/updateCheck',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_legacy_code_push_acquisition_update_download_status(client):
    """Test case for legacy_code_push_acquisition_update_download_status

    
    """
    body = openapi_server.LegacyCodePushAcquisitionUpdateInstallsStatusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/legacy/reportStatus/download',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_legacy_code_push_acquisition_update_installs_status(client):
    """Test case for legacy_code_push_acquisition_update_installs_status

    
    """
    body = openapi_server.LegacyCodePushAcquisitionUpdateInstallsStatusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/legacy/reportStatus/deploy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

