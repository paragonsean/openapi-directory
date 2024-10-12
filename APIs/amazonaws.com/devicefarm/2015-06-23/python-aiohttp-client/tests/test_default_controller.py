# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_device_pool_request import CreateDevicePoolRequest
from openapi_server.models.create_device_pool_result import CreateDevicePoolResult
from openapi_server.models.create_instance_profile_request import CreateInstanceProfileRequest
from openapi_server.models.create_instance_profile_result import CreateInstanceProfileResult
from openapi_server.models.create_network_profile_request import CreateNetworkProfileRequest
from openapi_server.models.create_network_profile_result import CreateNetworkProfileResult
from openapi_server.models.create_project_request import CreateProjectRequest
from openapi_server.models.create_project_result import CreateProjectResult
from openapi_server.models.create_remote_access_session_request import CreateRemoteAccessSessionRequest
from openapi_server.models.create_remote_access_session_result import CreateRemoteAccessSessionResult
from openapi_server.models.create_test_grid_project_request import CreateTestGridProjectRequest
from openapi_server.models.create_test_grid_project_result import CreateTestGridProjectResult
from openapi_server.models.create_test_grid_url_request import CreateTestGridUrlRequest
from openapi_server.models.create_test_grid_url_result import CreateTestGridUrlResult
from openapi_server.models.create_upload_request import CreateUploadRequest
from openapi_server.models.create_upload_result import CreateUploadResult
from openapi_server.models.create_vpce_configuration_request import CreateVPCEConfigurationRequest
from openapi_server.models.create_vpce_configuration_result import CreateVPCEConfigurationResult
from openapi_server.models.delete_device_pool_request import DeleteDevicePoolRequest
from openapi_server.models.delete_instance_profile_request import DeleteInstanceProfileRequest
from openapi_server.models.delete_network_profile_request import DeleteNetworkProfileRequest
from openapi_server.models.delete_project_request import DeleteProjectRequest
from openapi_server.models.delete_remote_access_session_request import DeleteRemoteAccessSessionRequest
from openapi_server.models.delete_run_request import DeleteRunRequest
from openapi_server.models.delete_test_grid_project_request import DeleteTestGridProjectRequest
from openapi_server.models.delete_upload_request import DeleteUploadRequest
from openapi_server.models.delete_vpce_configuration_request import DeleteVPCEConfigurationRequest
from openapi_server.models.get_account_settings_result import GetAccountSettingsResult
from openapi_server.models.get_device_instance_request import GetDeviceInstanceRequest
from openapi_server.models.get_device_instance_result import GetDeviceInstanceResult
from openapi_server.models.get_device_pool_compatibility_request import GetDevicePoolCompatibilityRequest
from openapi_server.models.get_device_pool_compatibility_result import GetDevicePoolCompatibilityResult
from openapi_server.models.get_device_pool_request import GetDevicePoolRequest
from openapi_server.models.get_device_pool_result import GetDevicePoolResult
from openapi_server.models.get_device_request import GetDeviceRequest
from openapi_server.models.get_device_result import GetDeviceResult
from openapi_server.models.get_instance_profile_request import GetInstanceProfileRequest
from openapi_server.models.get_instance_profile_result import GetInstanceProfileResult
from openapi_server.models.get_job_request import GetJobRequest
from openapi_server.models.get_job_result import GetJobResult
from openapi_server.models.get_network_profile_request import GetNetworkProfileRequest
from openapi_server.models.get_network_profile_result import GetNetworkProfileResult
from openapi_server.models.get_offering_status_request import GetOfferingStatusRequest
from openapi_server.models.get_offering_status_result import GetOfferingStatusResult
from openapi_server.models.get_project_request import GetProjectRequest
from openapi_server.models.get_project_result import GetProjectResult
from openapi_server.models.get_remote_access_session_request import GetRemoteAccessSessionRequest
from openapi_server.models.get_remote_access_session_result import GetRemoteAccessSessionResult
from openapi_server.models.get_run_request import GetRunRequest
from openapi_server.models.get_run_result import GetRunResult
from openapi_server.models.get_suite_request import GetSuiteRequest
from openapi_server.models.get_suite_result import GetSuiteResult
from openapi_server.models.get_test_grid_project_request import GetTestGridProjectRequest
from openapi_server.models.get_test_grid_project_result import GetTestGridProjectResult
from openapi_server.models.get_test_grid_session_request import GetTestGridSessionRequest
from openapi_server.models.get_test_grid_session_result import GetTestGridSessionResult
from openapi_server.models.get_test_request import GetTestRequest
from openapi_server.models.get_test_result import GetTestResult
from openapi_server.models.get_upload_request import GetUploadRequest
from openapi_server.models.get_upload_result import GetUploadResult
from openapi_server.models.get_vpce_configuration_request import GetVPCEConfigurationRequest
from openapi_server.models.get_vpce_configuration_result import GetVPCEConfigurationResult
from openapi_server.models.install_to_remote_access_session_request import InstallToRemoteAccessSessionRequest
from openapi_server.models.install_to_remote_access_session_result import InstallToRemoteAccessSessionResult
from openapi_server.models.list_artifacts_request import ListArtifactsRequest
from openapi_server.models.list_artifacts_result import ListArtifactsResult
from openapi_server.models.list_device_instances_request import ListDeviceInstancesRequest
from openapi_server.models.list_device_instances_result import ListDeviceInstancesResult
from openapi_server.models.list_device_pools_request import ListDevicePoolsRequest
from openapi_server.models.list_device_pools_result import ListDevicePoolsResult
from openapi_server.models.list_devices_request import ListDevicesRequest
from openapi_server.models.list_devices_result import ListDevicesResult
from openapi_server.models.list_instance_profiles_request import ListInstanceProfilesRequest
from openapi_server.models.list_instance_profiles_result import ListInstanceProfilesResult
from openapi_server.models.list_jobs_request import ListJobsRequest
from openapi_server.models.list_jobs_result import ListJobsResult
from openapi_server.models.list_network_profiles_request import ListNetworkProfilesRequest
from openapi_server.models.list_network_profiles_result import ListNetworkProfilesResult
from openapi_server.models.list_offering_promotions_request import ListOfferingPromotionsRequest
from openapi_server.models.list_offering_promotions_result import ListOfferingPromotionsResult
from openapi_server.models.list_offering_transactions_request import ListOfferingTransactionsRequest
from openapi_server.models.list_offering_transactions_result import ListOfferingTransactionsResult
from openapi_server.models.list_offerings_request import ListOfferingsRequest
from openapi_server.models.list_offerings_result import ListOfferingsResult
from openapi_server.models.list_projects_request import ListProjectsRequest
from openapi_server.models.list_projects_result import ListProjectsResult
from openapi_server.models.list_remote_access_sessions_request import ListRemoteAccessSessionsRequest
from openapi_server.models.list_remote_access_sessions_result import ListRemoteAccessSessionsResult
from openapi_server.models.list_runs_request import ListRunsRequest
from openapi_server.models.list_runs_result import ListRunsResult
from openapi_server.models.list_samples_request import ListSamplesRequest
from openapi_server.models.list_samples_result import ListSamplesResult
from openapi_server.models.list_suites_request import ListSuitesRequest
from openapi_server.models.list_suites_result import ListSuitesResult
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_test_grid_projects_request import ListTestGridProjectsRequest
from openapi_server.models.list_test_grid_projects_result import ListTestGridProjectsResult
from openapi_server.models.list_test_grid_session_actions_request import ListTestGridSessionActionsRequest
from openapi_server.models.list_test_grid_session_actions_result import ListTestGridSessionActionsResult
from openapi_server.models.list_test_grid_session_artifacts_request import ListTestGridSessionArtifactsRequest
from openapi_server.models.list_test_grid_session_artifacts_result import ListTestGridSessionArtifactsResult
from openapi_server.models.list_test_grid_sessions_request import ListTestGridSessionsRequest
from openapi_server.models.list_test_grid_sessions_result import ListTestGridSessionsResult
from openapi_server.models.list_tests_request import ListTestsRequest
from openapi_server.models.list_tests_result import ListTestsResult
from openapi_server.models.list_unique_problems_request import ListUniqueProblemsRequest
from openapi_server.models.list_unique_problems_result import ListUniqueProblemsResult
from openapi_server.models.list_uploads_request import ListUploadsRequest
from openapi_server.models.list_uploads_result import ListUploadsResult
from openapi_server.models.list_vpce_configurations_request import ListVPCEConfigurationsRequest
from openapi_server.models.list_vpce_configurations_result import ListVPCEConfigurationsResult
from openapi_server.models.purchase_offering_request import PurchaseOfferingRequest
from openapi_server.models.purchase_offering_result import PurchaseOfferingResult
from openapi_server.models.renew_offering_request import RenewOfferingRequest
from openapi_server.models.renew_offering_result import RenewOfferingResult
from openapi_server.models.schedule_run_request import ScheduleRunRequest
from openapi_server.models.schedule_run_result import ScheduleRunResult
from openapi_server.models.stop_job_request import StopJobRequest
from openapi_server.models.stop_job_result import StopJobResult
from openapi_server.models.stop_remote_access_session_request import StopRemoteAccessSessionRequest
from openapi_server.models.stop_remote_access_session_result import StopRemoteAccessSessionResult
from openapi_server.models.stop_run_request import StopRunRequest
from openapi_server.models.stop_run_result import StopRunResult
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_device_instance_request import UpdateDeviceInstanceRequest
from openapi_server.models.update_device_instance_result import UpdateDeviceInstanceResult
from openapi_server.models.update_device_pool_request import UpdateDevicePoolRequest
from openapi_server.models.update_device_pool_result import UpdateDevicePoolResult
from openapi_server.models.update_instance_profile_request import UpdateInstanceProfileRequest
from openapi_server.models.update_instance_profile_result import UpdateInstanceProfileResult
from openapi_server.models.update_network_profile_request import UpdateNetworkProfileRequest
from openapi_server.models.update_network_profile_result import UpdateNetworkProfileResult
from openapi_server.models.update_project_request import UpdateProjectRequest
from openapi_server.models.update_project_result import UpdateProjectResult
from openapi_server.models.update_test_grid_project_request import UpdateTestGridProjectRequest
from openapi_server.models.update_test_grid_project_result import UpdateTestGridProjectResult
from openapi_server.models.update_upload_request import UpdateUploadRequest
from openapi_server.models.update_upload_result import UpdateUploadResult
from openapi_server.models.update_vpce_configuration_request import UpdateVPCEConfigurationRequest
from openapi_server.models.update_vpce_configuration_result import UpdateVPCEConfigurationResult


pytestmark = pytest.mark.asyncio

async def test_create_device_pool(client):
    """Test case for create_device_pool

    
    """
    body = {"projectArn":"","name":"","maxDevices":"","description":"","rules":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.CreateDevicePool',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_instance_profile(client):
    """Test case for create_instance_profile

    
    """
    body = {"excludeAppPackagesFromCleanup":"","name":"","description":"","rebootAfterUse":"","packageCleanup":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.CreateInstanceProfile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_profile(client):
    """Test case for create_network_profile

    
    """
    body = {"projectArn":"","uplinkLossPercent":"","downlinkBandwidthBits":"","downlinkDelayMs":"","uplinkJitterMs":"","name":"","description":"","uplinkBandwidthBits":"","downlinkJitterMs":"","type":"","downlinkLossPercent":"","uplinkDelayMs":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.CreateNetworkProfile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_project(client):
    """Test case for create_project

    
    """
    body = {"defaultJobTimeoutMinutes":"","vpcConfig":{"securityGroupIds":"","vpcId":"","subnetIds":""},"name":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.CreateProject',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_remote_access_session(client):
    """Test case for create_remote_access_session

    
    """
    body = {"projectArn":"","sshPublicKey":"","remoteRecordEnabled":"","clientId":"","interactionMode":"","configuration":{"billingMethod":"","vpceConfigurationArns":""},"deviceArn":"","name":"","skipAppResign":"","instanceArn":"","remoteDebugEnabled":"","remoteRecordAppArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.CreateRemoteAccessSession',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_test_grid_project(client):
    """Test case for create_test_grid_project

    
    """
    body = {"vpcConfig":{"securityGroupIds":"","vpcId":"","subnetIds":""},"name":"","description":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.CreateTestGridProject',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_test_grid_url(client):
    """Test case for create_test_grid_url

    
    """
    body = {"projectArn":"","expiresInSeconds":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.CreateTestGridUrl',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_upload(client):
    """Test case for create_upload

    
    """
    body = {"projectArn":"","name":"","type":"","contentType":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.CreateUpload',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_vpce_configuration(client):
    """Test case for create_vpce_configuration

    
    """
    body = {"serviceDnsName":"","vpceServiceName":"","vpceConfigurationDescription":"","vpceConfigurationName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.CreateVPCEConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_device_pool(client):
    """Test case for delete_device_pool

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.DeleteDevicePool',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_instance_profile(client):
    """Test case for delete_instance_profile

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.DeleteInstanceProfile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_profile(client):
    """Test case for delete_network_profile

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.DeleteNetworkProfile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project(client):
    """Test case for delete_project

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.DeleteProject',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_remote_access_session(client):
    """Test case for delete_remote_access_session

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.DeleteRemoteAccessSession',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_run(client):
    """Test case for delete_run

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.DeleteRun',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_test_grid_project(client):
    """Test case for delete_test_grid_project

    
    """
    body = {"projectArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.DeleteTestGridProject',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_upload(client):
    """Test case for delete_upload

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.DeleteUpload',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vpce_configuration(client):
    """Test case for delete_vpce_configuration

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.DeleteVPCEConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_settings(client):
    """Test case for get_account_settings

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetAccountSettings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device(client):
    """Test case for get_device

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetDevice',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_instance(client):
    """Test case for get_device_instance

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetDeviceInstance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_pool(client):
    """Test case for get_device_pool

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetDevicePool',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_pool_compatibility(client):
    """Test case for get_device_pool_compatibility

    
    """
    body = {"test":{"filter":"","testSpecArn":"","testPackageArn":"","type":"","parameters":""},"configuration":{"extraDataPackageArn":"","radios":{"wifi":"","bluetooth":"","nfc":"","gps":""},"billingMethod":"","vpceConfigurationArns":"","auxiliaryApps":"","location":{"latitude":"","longitude":""},"networkProfileArn":"","locale":"","customerArtifactPaths":{"iosPaths":"","androidPaths":"","deviceHostPaths":""}},"appArn":"","testType":"","devicePoolArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetDevicePoolCompatibility',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instance_profile(client):
    """Test case for get_instance_profile

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetInstanceProfile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job(client):
    """Test case for get_job

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_profile(client):
    """Test case for get_network_profile

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetNetworkProfile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_offering_status(client):
    """Test case for get_offering_status

    
    """
    body = {"nextToken":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetOfferingStatus',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project(client):
    """Test case for get_project

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetProject',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_access_session(client):
    """Test case for get_remote_access_session

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetRemoteAccessSession',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_run(client):
    """Test case for get_run

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetRun',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_suite(client):
    """Test case for get_suite

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetSuite',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_test(client):
    """Test case for get_test

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetTest',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_test_grid_project(client):
    """Test case for get_test_grid_project

    
    """
    body = {"projectArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetTestGridProject',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_test_grid_session(client):
    """Test case for get_test_grid_session

    
    """
    body = {"projectArn":"","sessionArn":"","sessionId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetTestGridSession',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_upload(client):
    """Test case for get_upload

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetUpload',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vpce_configuration(client):
    """Test case for get_vpce_configuration

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.GetVPCEConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_install_to_remote_access_session(client):
    """Test case for install_to_remote_access_session

    
    """
    body = {"remoteAccessSessionArn":"","appArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.InstallToRemoteAccessSession',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_artifacts(client):
    """Test case for list_artifacts

    
    """
    body = {"nextToken":"","arn":"","type":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListArtifacts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_device_instances(client):
    """Test case for list_device_instances

    
    """
    body = {"maxResults":"","nextToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListDeviceInstances',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_device_pools(client):
    """Test case for list_device_pools

    
    """
    body = {"nextToken":"","arn":"","type":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListDevicePools',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_devices(client):
    """Test case for list_devices

    
    """
    body = {"nextToken":"","filters":"","arn":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListDevices',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_instance_profiles(client):
    """Test case for list_instance_profiles

    
    """
    body = {"maxResults":"","nextToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListInstanceProfiles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_jobs(client):
    """Test case for list_jobs

    
    """
    body = {"nextToken":"","arn":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListJobs',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_network_profiles(client):
    """Test case for list_network_profiles

    
    """
    body = {"nextToken":"","arn":"","type":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListNetworkProfiles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_offering_promotions(client):
    """Test case for list_offering_promotions

    
    """
    body = {"nextToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListOfferingPromotions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_offering_transactions(client):
    """Test case for list_offering_transactions

    
    """
    body = {"nextToken":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListOfferingTransactions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_offerings(client):
    """Test case for list_offerings

    
    """
    body = {"nextToken":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListOfferings',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_projects(client):
    """Test case for list_projects

    
    """
    body = {"nextToken":"","arn":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListProjects',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_remote_access_sessions(client):
    """Test case for list_remote_access_sessions

    
    """
    body = {"nextToken":"","arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListRemoteAccessSessions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_runs(client):
    """Test case for list_runs

    
    """
    body = {"nextToken":"","arn":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListRuns',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_samples(client):
    """Test case for list_samples

    
    """
    body = {"nextToken":"","arn":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListSamples',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_suites(client):
    """Test case for list_suites

    
    """
    body = {"nextToken":"","arn":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListSuites',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    body = {"ResourceARN":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListTagsForResource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_test_grid_projects(client):
    """Test case for list_test_grid_projects

    
    """
    body = {"maxResult":"","nextToken":""}
    params = [('maxResult', 'max_result_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListTestGridProjects',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_test_grid_session_actions(client):
    """Test case for list_test_grid_session_actions

    
    """
    body = {"maxResult":"","nextToken":"","sessionArn":""}
    params = [('maxResult', 'max_result_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListTestGridSessionActions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_test_grid_session_artifacts(client):
    """Test case for list_test_grid_session_artifacts

    
    """
    body = {"maxResult":"","nextToken":"","sessionArn":"","type":""}
    params = [('maxResult', 'max_result_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListTestGridSessionArtifacts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_test_grid_sessions(client):
    """Test case for list_test_grid_sessions

    
    """
    body = {"projectArn":"","maxResult":"","nextToken":"","creationTimeAfter":"","endTimeAfter":"","endTimeBefore":"","creationTimeBefore":"","status":""}
    params = [('maxResult', 'max_result_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListTestGridSessions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tests(client):
    """Test case for list_tests

    
    """
    body = {"nextToken":"","arn":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListTests',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_unique_problems(client):
    """Test case for list_unique_problems

    
    """
    body = {"nextToken":"","arn":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListUniqueProblems',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_uploads(client):
    """Test case for list_uploads

    
    """
    body = {"nextToken":"","arn":"","type":""}
    params = [('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListUploads',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_vpce_configurations(client):
    """Test case for list_vpce_configurations

    
    """
    body = {"maxResults":"","nextToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ListVPCEConfigurations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purchase_offering(client):
    """Test case for purchase_offering

    
    """
    body = {"offeringPromotionId":"","quantity":"","offeringId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.PurchaseOffering',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_renew_offering(client):
    """Test case for renew_offering

    
    """
    body = {"quantity":"","offeringId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.RenewOffering',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedule_run(client):
    """Test case for schedule_run

    
    """
    body = {"projectArn":"","executionConfiguration":{"videoCapture":"","appPackagesCleanup":"","jobTimeoutMinutes":"","skipAppResign":"","accountsCleanup":""},"test":{"filter":"","testSpecArn":"","testPackageArn":"","type":"","parameters":""},"configuration":{"extraDataPackageArn":"","radios":{"wifi":"","bluetooth":"","nfc":"","gps":""},"billingMethod":"","vpceConfigurationArns":"","auxiliaryApps":"","location":{"latitude":"","longitude":""},"networkProfileArn":"","locale":"","customerArtifactPaths":{"iosPaths":"","androidPaths":"","deviceHostPaths":""}},"deviceSelectionConfiguration":{"maxDevices":"","filters":""},"appArn":"","name":"","devicePoolArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.ScheduleRun',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_job(client):
    """Test case for stop_job

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.StopJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_remote_access_session(client):
    """Test case for stop_remote_access_session

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.StopRemoteAccessSession',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_run(client):
    """Test case for stop_run

    
    """
    body = {"arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.StopRun',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"ResourceARN":"","Tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.TagResource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    body = {"ResourceARN":"","TagKeys":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.UntagResource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_instance(client):
    """Test case for update_device_instance

    
    """
    body = {"profileArn":"","arn":"","labels":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.UpdateDeviceInstance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_pool(client):
    """Test case for update_device_pool

    
    """
    body = {"clearMaxDevices":"","name":"","maxDevices":"","description":"","rules":"","arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.UpdateDevicePool',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_instance_profile(client):
    """Test case for update_instance_profile

    
    """
    body = {"excludeAppPackagesFromCleanup":"","name":"","description":"","rebootAfterUse":"","packageCleanup":"","arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.UpdateInstanceProfile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_profile(client):
    """Test case for update_network_profile

    
    """
    body = {"uplinkLossPercent":"","downlinkBandwidthBits":"","downlinkDelayMs":"","uplinkJitterMs":"","name":"","description":"","uplinkBandwidthBits":"","downlinkJitterMs":"","arn":"","type":"","downlinkLossPercent":"","uplinkDelayMs":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.UpdateNetworkProfile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project(client):
    """Test case for update_project

    
    """
    body = {"defaultJobTimeoutMinutes":"","vpcConfig":{"securityGroupIds":"","vpcId":"","subnetIds":""},"name":"","arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.UpdateProject',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_test_grid_project(client):
    """Test case for update_test_grid_project

    
    """
    body = {"projectArn":"","vpcConfig":{"securityGroupIds":"","vpcId":"","subnetIds":""},"name":"","description":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.UpdateTestGridProject',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_upload(client):
    """Test case for update_upload

    
    """
    body = {"name":"","editContent":"","arn":"","contentType":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.UpdateUpload',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_vpce_configuration(client):
    """Test case for update_vpce_configuration

    
    """
    body = {"serviceDnsName":"","vpceServiceName":"","vpceConfigurationDescription":"","vpceConfigurationName":"","arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DeviceFarm_20150623.UpdateVPCEConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

