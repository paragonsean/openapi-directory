# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_access_point_for_object_lambda_request import CreateAccessPointForObjectLambdaRequest
from openapi_server.models.create_access_point_for_object_lambda_result import CreateAccessPointForObjectLambdaResult
from openapi_server.models.create_access_point_request import CreateAccessPointRequest
from openapi_server.models.create_access_point_result import CreateAccessPointResult
from openapi_server.models.create_bucket_request import CreateBucketRequest
from openapi_server.models.create_bucket_result import CreateBucketResult
from openapi_server.models.create_job_request import CreateJobRequest
from openapi_server.models.create_job_result import CreateJobResult
from openapi_server.models.create_multi_region_access_point_request import CreateMultiRegionAccessPointRequest
from openapi_server.models.create_multi_region_access_point_result import CreateMultiRegionAccessPointResult
from openapi_server.models.delete_multi_region_access_point_request import DeleteMultiRegionAccessPointRequest
from openapi_server.models.delete_multi_region_access_point_result import DeleteMultiRegionAccessPointResult
from openapi_server.models.describe_job_result import DescribeJobResult
from openapi_server.models.describe_multi_region_access_point_operation_result import DescribeMultiRegionAccessPointOperationResult
from openapi_server.models.get_access_point_configuration_for_object_lambda_result import GetAccessPointConfigurationForObjectLambdaResult
from openapi_server.models.get_access_point_for_object_lambda_result import GetAccessPointForObjectLambdaResult
from openapi_server.models.get_access_point_policy_for_object_lambda_result import GetAccessPointPolicyForObjectLambdaResult
from openapi_server.models.get_access_point_policy_result import GetAccessPointPolicyResult
from openapi_server.models.get_access_point_policy_status_for_object_lambda_result import GetAccessPointPolicyStatusForObjectLambdaResult
from openapi_server.models.get_access_point_policy_status_result import GetAccessPointPolicyStatusResult
from openapi_server.models.get_access_point_result import GetAccessPointResult
from openapi_server.models.get_bucket_lifecycle_configuration_result import GetBucketLifecycleConfigurationResult
from openapi_server.models.get_bucket_policy_result import GetBucketPolicyResult
from openapi_server.models.get_bucket_replication_result import GetBucketReplicationResult
from openapi_server.models.get_bucket_result import GetBucketResult
from openapi_server.models.get_bucket_tagging_result import GetBucketTaggingResult
from openapi_server.models.get_bucket_versioning_result import GetBucketVersioningResult
from openapi_server.models.get_job_tagging_result import GetJobTaggingResult
from openapi_server.models.get_multi_region_access_point_policy_result import GetMultiRegionAccessPointPolicyResult
from openapi_server.models.get_multi_region_access_point_policy_status_result import GetMultiRegionAccessPointPolicyStatusResult
from openapi_server.models.get_multi_region_access_point_result import GetMultiRegionAccessPointResult
from openapi_server.models.get_multi_region_access_point_routes_result import GetMultiRegionAccessPointRoutesResult
from openapi_server.models.get_public_access_block_output import GetPublicAccessBlockOutput
from openapi_server.models.get_storage_lens_configuration_result import GetStorageLensConfigurationResult
from openapi_server.models.get_storage_lens_configuration_tagging_result import GetStorageLensConfigurationTaggingResult
from openapi_server.models.job_status import JobStatus
from openapi_server.models.list_access_points_for_object_lambda_result import ListAccessPointsForObjectLambdaResult
from openapi_server.models.list_access_points_result import ListAccessPointsResult
from openapi_server.models.list_jobs_result import ListJobsResult
from openapi_server.models.list_multi_region_access_points_result import ListMultiRegionAccessPointsResult
from openapi_server.models.list_regional_buckets_result import ListRegionalBucketsResult
from openapi_server.models.list_storage_lens_configurations_result import ListStorageLensConfigurationsResult
from openapi_server.models.put_access_point_policy_for_object_lambda_request import PutAccessPointPolicyForObjectLambdaRequest
from openapi_server.models.put_access_point_policy_request import PutAccessPointPolicyRequest
from openapi_server.models.put_bucket_lifecycle_configuration_request import PutBucketLifecycleConfigurationRequest
from openapi_server.models.put_bucket_policy_request import PutBucketPolicyRequest
from openapi_server.models.put_bucket_replication_request import PutBucketReplicationRequest
from openapi_server.models.put_bucket_tagging_request import PutBucketTaggingRequest
from openapi_server.models.put_bucket_versioning_request import PutBucketVersioningRequest
from openapi_server.models.put_job_tagging_request import PutJobTaggingRequest
from openapi_server.models.put_multi_region_access_point_policy_request import PutMultiRegionAccessPointPolicyRequest
from openapi_server.models.put_multi_region_access_point_policy_result import PutMultiRegionAccessPointPolicyResult
from openapi_server.models.put_public_access_block_request import PutPublicAccessBlockRequest
from openapi_server.models.put_storage_lens_configuration_request import PutStorageLensConfigurationRequest
from openapi_server.models.put_storage_lens_configuration_tagging_request import PutStorageLensConfigurationTaggingRequest
from openapi_server.models.submit_multi_region_access_point_routes_request import SubmitMultiRegionAccessPointRoutesRequest
from openapi_server.models.update_job_priority_result import UpdateJobPriorityResult
from openapi_server.models.update_job_status_result import UpdateJobStatusResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_access_point(client):
    """Test case for create_access_point

    
    """
    body = openapi_server.CreateAccessPointRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/accesspoint/{namex_amz_account_i}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_access_point_for_object_lambda(client):
    """Test case for create_access_point_for_object_lambda

    
    """
    body = openapi_server.CreateAccessPointForObjectLambdaRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/accesspointforobjectlambda/{namex_amz_account_i}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_bucket(client):
    """Test case for create_bucket

    
    """
    body = openapi_server.CreateBucketRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_acl': 'x_amz_acl_example',
        'x_amz_grant_full_control': 'x_amz_grant_full_control_example',
        'x_amz_grant_read': 'x_amz_grant_read_example',
        'x_amz_grant_read_acp': 'x_amz_grant_read_acp_example',
        'x_amz_grant_write': 'x_amz_grant_write_example',
        'x_amz_grant_write_acp': 'x_amz_grant_write_acp_example',
        'x_amz_bucket_object_lock_enabled': True,
        'x_amz_outpost_id': 'x_amz_outpost_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/bucket/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_job(client):
    """Test case for create_job

    
    """
    body = openapi_server.CreateJobRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v20180820/jobs#x-amz-account-id',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_multi_region_access_point(client):
    """Test case for create_multi_region_access_point

    
    """
    body = openapi_server.CreateMultiRegionAccessPointRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v20180820/async-requests/mrap/create#x-amz-account-id',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_access_point(client):
    """Test case for delete_access_point

    
    """
    headers = { 
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/accesspoint/{namex_amz_account_i}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_access_point_for_object_lambda(client):
    """Test case for delete_access_point_for_object_lambda

    
    """
    headers = { 
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/accesspointforobjectlambda/{namex_amz_account_i}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_access_point_policy(client):
    """Test case for delete_access_point_policy

    
    """
    headers = { 
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/accesspoint/{name}/policy#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_access_point_policy_for_object_lambda(client):
    """Test case for delete_access_point_policy_for_object_lambda

    
    """
    headers = { 
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/accesspointforobjectlambda/{name}/policy#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bucket(client):
    """Test case for delete_bucket

    
    """
    headers = { 
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/bucket/{namex_amz_account_i}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bucket_lifecycle_configuration(client):
    """Test case for delete_bucket_lifecycle_configuration

    
    """
    headers = { 
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/bucket/{name}/lifecycleconfiguration#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bucket_policy(client):
    """Test case for delete_bucket_policy

    
    """
    headers = { 
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/bucket/{name}/policy#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bucket_replication(client):
    """Test case for delete_bucket_replication

    
    """
    headers = { 
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/bucket/{name}/replication#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bucket_tagging(client):
    """Test case for delete_bucket_tagging

    
    """
    headers = { 
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/bucket/{name}/tagging#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_job_tagging(client):
    """Test case for delete_job_tagging

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/jobs/{id}/tagging#x-amz-account-id'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_delete_multi_region_access_point(client):
    """Test case for delete_multi_region_access_point

    
    """
    body = openapi_server.DeleteMultiRegionAccessPointRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v20180820/async-requests/mrap/delete#x-amz-account-id',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_public_access_block(client):
    """Test case for delete_public_access_block

    
    """
    headers = { 
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/configuration/publicAccessBlock#x-amz-account-id',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_storage_lens_configuration(client):
    """Test case for delete_storage_lens_configuration

    
    """
    headers = { 
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/storagelens/{storagelensidx_amz_account_i}'.format(storagelensid='storagelensid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_storage_lens_configuration_tagging(client):
    """Test case for delete_storage_lens_configuration_tagging

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v20180820/storagelens/{storagelensid}/tagging#x-amz-account-id'.format(storagelensid='storagelensid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_job(client):
    """Test case for describe_job

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/jobs/{idx_amz_account_i}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_multi_region_access_point_operation(client):
    """Test case for describe_multi_region_access_point_operation

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/async-requests/mrap/{request_tokenx_amz_account_i}'.format(request_token='request_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_access_point(client):
    """Test case for get_access_point

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/accesspoint/{namex_amz_account_i}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_access_point_configuration_for_object_lambda(client):
    """Test case for get_access_point_configuration_for_object_lambda

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/accesspointforobjectlambda/{name}/configuration#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_access_point_for_object_lambda(client):
    """Test case for get_access_point_for_object_lambda

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/accesspointforobjectlambda/{namex_amz_account_i}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_access_point_policy(client):
    """Test case for get_access_point_policy

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/accesspoint/{name}/policy#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_access_point_policy_for_object_lambda(client):
    """Test case for get_access_point_policy_for_object_lambda

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/accesspointforobjectlambda/{name}/policy#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_access_point_policy_status(client):
    """Test case for get_access_point_policy_status

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/accesspoint/{name}/policyStatus#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_access_point_policy_status_for_object_lambda(client):
    """Test case for get_access_point_policy_status_for_object_lambda

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/accesspointforobjectlambda/{name}/policyStatus#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bucket(client):
    """Test case for get_bucket

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/bucket/{namex_amz_account_i}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bucket_lifecycle_configuration(client):
    """Test case for get_bucket_lifecycle_configuration

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/bucket/{name}/lifecycleconfiguration#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bucket_policy(client):
    """Test case for get_bucket_policy

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/bucket/{name}/policy#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bucket_replication(client):
    """Test case for get_bucket_replication

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/bucket/{name}/replication#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bucket_tagging(client):
    """Test case for get_bucket_tagging

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/bucket/{name}/tagging#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bucket_versioning(client):
    """Test case for get_bucket_versioning

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/bucket/{name}/versioning#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job_tagging(client):
    """Test case for get_job_tagging

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/jobs/{id}/tagging#x-amz-account-id'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multi_region_access_point(client):
    """Test case for get_multi_region_access_point

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/mrap/instances/{namex_amz_account_i}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multi_region_access_point_policy(client):
    """Test case for get_multi_region_access_point_policy

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/mrap/instances/{name}/policy#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multi_region_access_point_policy_status(client):
    """Test case for get_multi_region_access_point_policy_status

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/mrap/instances/{name}/policystatus#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multi_region_access_point_routes(client):
    """Test case for get_multi_region_access_point_routes

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/mrap/instances/{mrap}/routes#x-amz-account-id'.format(mrap='mrap_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_access_block(client):
    """Test case for get_public_access_block

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/configuration/publicAccessBlock#x-amz-account-id',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_storage_lens_configuration(client):
    """Test case for get_storage_lens_configuration

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/storagelens/{storagelensidx_amz_account_i}'.format(storagelensid='storagelensid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_storage_lens_configuration_tagging(client):
    """Test case for get_storage_lens_configuration_tagging

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/storagelens/{storagelensid}/tagging#x-amz-account-id'.format(storagelensid='storagelensid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_access_points(client):
    """Test case for list_access_points

    
    """
    params = [('bucket', 'bucket_example'),
                    ('nextToken', 'next_token_example'),
                    ('maxResults', 56),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/accesspoint#x-amz-account-id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_access_points_for_object_lambda(client):
    """Test case for list_access_points_for_object_lambda

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 56),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/accesspointforobjectlambda#x-amz-account-id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_jobs(client):
    """Test case for list_jobs

    
    """
    params = [('jobStatuses', [openapi_server.JobStatus()]),
                    ('nextToken', 'next_token_example'),
                    ('maxResults', 56),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/jobs#x-amz-account-id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_multi_region_access_points(client):
    """Test case for list_multi_region_access_points

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 56),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/mrap/instances#x-amz-account-id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_regional_buckets(client):
    """Test case for list_regional_buckets

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('maxResults', 56),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'x_amz_outpost_id': 'x_amz_outpost_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/bucket#x-amz-account-id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_storage_lens_configurations(client):
    """Test case for list_storage_lens_configurations

    
    """
    params = [('nextToken', 'next_token_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v20180820/storagelens#x-amz-account-id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_access_point_configuration_for_object_lambda(client):
    """Test case for put_access_point_configuration_for_object_lambda

    
    """
    body = openapi_server.CreateAccessPointForObjectLambdaRequest()
    headers = { 
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/accesspointforobjectlambda/{name}/configuration#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_access_point_policy(client):
    """Test case for put_access_point_policy

    
    """
    body = openapi_server.PutAccessPointPolicyRequest()
    headers = { 
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/accesspoint/{name}/policy#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_access_point_policy_for_object_lambda(client):
    """Test case for put_access_point_policy_for_object_lambda

    
    """
    body = openapi_server.PutAccessPointPolicyForObjectLambdaRequest()
    headers = { 
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/accesspointforobjectlambda/{name}/policy#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_bucket_lifecycle_configuration(client):
    """Test case for put_bucket_lifecycle_configuration

    
    """
    body = openapi_server.PutBucketLifecycleConfigurationRequest()
    headers = { 
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/bucket/{name}/lifecycleconfiguration#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_bucket_policy(client):
    """Test case for put_bucket_policy

    
    """
    body = openapi_server.PutBucketPolicyRequest()
    headers = { 
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'x_amz_confirm_remove_self_bucket_access': True,
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/bucket/{name}/policy#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_bucket_replication(client):
    """Test case for put_bucket_replication

    
    """
    body = openapi_server.PutBucketReplicationRequest()
    headers = { 
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/bucket/{name}/replication#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_bucket_tagging(client):
    """Test case for put_bucket_tagging

    
    """
    body = openapi_server.PutBucketTaggingRequest()
    headers = { 
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/bucket/{name}/tagging#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_bucket_versioning(client):
    """Test case for put_bucket_versioning

    
    """
    body = openapi_server.PutBucketVersioningRequest()
    headers = { 
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'x_amz_mfa': 'x_amz_mfa_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/bucket/{name}/versioning#x-amz-account-id'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_job_tagging(client):
    """Test case for put_job_tagging

    
    """
    body = openapi_server.PutJobTaggingRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/jobs/{id}/tagging#x-amz-account-id'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_multi_region_access_point_policy(client):
    """Test case for put_multi_region_access_point_policy

    
    """
    body = openapi_server.PutMultiRegionAccessPointPolicyRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v20180820/async-requests/mrap/put-policy#x-amz-account-id',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_public_access_block(client):
    """Test case for put_public_access_block

    
    """
    body = openapi_server.PutPublicAccessBlockRequest()
    headers = { 
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/configuration/publicAccessBlock#x-amz-account-id',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_storage_lens_configuration(client):
    """Test case for put_storage_lens_configuration

    
    """
    body = openapi_server.PutStorageLensConfigurationRequest()
    headers = { 
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/storagelens/{storagelensidx_amz_account_i}'.format(storagelensid='storagelensid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_put_storage_lens_configuration_tagging(client):
    """Test case for put_storage_lens_configuration_tagging

    
    """
    body = openapi_server.PutStorageLensConfigurationTaggingRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v20180820/storagelens/{storagelensid}/tagging#x-amz-account-id'.format(storagelensid='storagelensid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_submit_multi_region_access_point_routes(client):
    """Test case for submit_multi_region_access_point_routes

    
    """
    body = openapi_server.SubmitMultiRegionAccessPointRoutesRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v20180820/mrap/instances/{mrap}/routes#x-amz-account-id'.format(mrap='mrap_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_job_priority(client):
    """Test case for update_job_priority

    
    """
    params = [('priority', 56)]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v20180820/jobs/{id}/priority#x-amz-account-id&priority'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_job_status(client):
    """Test case for update_job_status

    
    """
    params = [('requestedJobStatus', 'requested_job_status_example'),
                    ('statusUpdateReason', 'status_update_reason_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_account_id': 'x_amz_account_id_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v20180820/jobs/{id}/status#x-amz-account-id&requestedJobStatus'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

