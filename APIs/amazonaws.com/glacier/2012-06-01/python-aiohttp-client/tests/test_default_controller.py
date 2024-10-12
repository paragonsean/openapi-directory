# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_tags_to_vault_request import AddTagsToVaultRequest
from openapi_server.models.describe_vault_output import DescribeVaultOutput
from openapi_server.models.get_data_retrieval_policy_output import GetDataRetrievalPolicyOutput
from openapi_server.models.get_job_output_output import GetJobOutputOutput
from openapi_server.models.get_vault_access_policy_output import GetVaultAccessPolicyOutput
from openapi_server.models.get_vault_lock_output import GetVaultLockOutput
from openapi_server.models.get_vault_notifications_output import GetVaultNotificationsOutput
from openapi_server.models.glacier_job_description import GlacierJobDescription
from openapi_server.models.initiate_job_request import InitiateJobRequest
from openapi_server.models.initiate_vault_lock_request import InitiateVaultLockRequest
from openapi_server.models.list_jobs_output import ListJobsOutput
from openapi_server.models.list_multipart_uploads_output import ListMultipartUploadsOutput
from openapi_server.models.list_parts_output import ListPartsOutput
from openapi_server.models.list_provisioned_capacity_output import ListProvisionedCapacityOutput
from openapi_server.models.list_tags_for_vault_output import ListTagsForVaultOutput
from openapi_server.models.list_vaults_output import ListVaultsOutput
from openapi_server.models.remove_tags_from_vault_request import RemoveTagsFromVaultRequest
from openapi_server.models.set_data_retrieval_policy_request import SetDataRetrievalPolicyRequest
from openapi_server.models.set_vault_access_policy_request import SetVaultAccessPolicyRequest
from openapi_server.models.set_vault_notifications_request import SetVaultNotificationsRequest
from openapi_server.models.upload_multipart_part_request import UploadMultipartPartRequest


pytestmark = pytest.mark.asyncio

async def test_abort_multipart_upload(client):
    """Test case for abort_multipart_upload

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{account_id}/vaults/{vault_name}/multipart-uploads/{upload_id}'.format(account_id='account_id_example', vault_name='vault_name_example', upload_id='upload_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_abort_vault_lock(client):
    """Test case for abort_vault_lock

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{account_id}/vaults/{vault_name}/lock-policy'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_tags_to_vault(client):
    """Test case for add_tags_to_vault

    
    """
    body = openapi_server.AddTagsToVaultRequest()
    params = [('operation', 'operation_example')]
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
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/{account_id}/vaults/{vault_name}/tags#operation=add'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_multipart_upload(client):
    """Test case for complete_multipart_upload

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_archive_size': 'x_amz_archive_size_example',
        'x_amz_sha256_tree_hash': 'x_amz_sha256_tree_hash_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/{account_id}/vaults/{vault_name}/multipart-uploads/{upload_id}'.format(account_id='account_id_example', vault_name='vault_name_example', upload_id='upload_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_vault_lock(client):
    """Test case for complete_vault_lock

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/{account_id}/vaults/{vault_name}/lock-policy/{lock_id}'.format(account_id='account_id_example', vault_name='vault_name_example', lock_id='lock_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_vault(client):
    """Test case for create_vault

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{account_id}/vaults/{vault_name}'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_archive(client):
    """Test case for delete_archive

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{account_id}/vaults/{vault_name}/archives/{archive_id}'.format(account_id='account_id_example', vault_name='vault_name_example', archive_id='archive_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vault(client):
    """Test case for delete_vault

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{account_id}/vaults/{vault_name}'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vault_access_policy(client):
    """Test case for delete_vault_access_policy

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{account_id}/vaults/{vault_name}/access-policy'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vault_notifications(client):
    """Test case for delete_vault_notifications

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{account_id}/vaults/{vault_name}/notification-configuration'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_job(client):
    """Test case for describe_job

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/vaults/{vault_name}/jobs/{job_id}'.format(account_id='account_id_example', vault_name='vault_name_example', job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_vault(client):
    """Test case for describe_vault

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/vaults/{vault_name}'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_data_retrieval_policy(client):
    """Test case for get_data_retrieval_policy

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/policies/data-retrieval'.format(account_id='account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job_output(client):
    """Test case for get_job_output

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'range': 'range_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/vaults/{vault_name}/jobs/{job_id}/output'.format(account_id='account_id_example', vault_name='vault_name_example', job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vault_access_policy(client):
    """Test case for get_vault_access_policy

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/vaults/{vault_name}/access-policy'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vault_lock(client):
    """Test case for get_vault_lock

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/vaults/{vault_name}/lock-policy'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vault_notifications(client):
    """Test case for get_vault_notifications

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/vaults/{vault_name}/notification-configuration'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_initiate_job(client):
    """Test case for initiate_job

    
    """
    body = openapi_server.InitiateJobRequest()
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
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/{account_id}/vaults/{vault_name}/jobs'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_initiate_multipart_upload(client):
    """Test case for initiate_multipart_upload

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_archive_description': 'x_amz_archive_description_example',
        'x_amz_part_size': 'x_amz_part_size_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/{account_id}/vaults/{vault_name}/multipart-uploads'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_initiate_vault_lock(client):
    """Test case for initiate_vault_lock

    
    """
    body = openapi_server.InitiateVaultLockRequest()
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
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/{account_id}/vaults/{vault_name}/lock-policy'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_jobs(client):
    """Test case for list_jobs

    
    """
    params = [('limit', 'limit_example'),
                    ('marker', 'marker_example'),
                    ('statuscode', 'statuscode_example'),
                    ('completed', 'completed_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/vaults/{vault_name}/jobs'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_multipart_uploads(client):
    """Test case for list_multipart_uploads

    
    """
    params = [('marker', 'marker_example'),
                    ('limit', 'limit_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/vaults/{vault_name}/multipart-uploads'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_parts(client):
    """Test case for list_parts

    
    """
    params = [('marker', 'marker_example'),
                    ('limit', 'limit_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/vaults/{vault_name}/multipart-uploads/{upload_id}'.format(account_id='account_id_example', vault_name='vault_name_example', upload_id='upload_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_provisioned_capacity(client):
    """Test case for list_provisioned_capacity

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/provisioned-capacity'.format(account_id='account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_vault(client):
    """Test case for list_tags_for_vault

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/vaults/{vault_name}/tags'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_vaults(client):
    """Test case for list_vaults

    
    """
    params = [('marker', 'marker_example'),
                    ('limit', 'limit_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{account_id}/vaults'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purchase_provisioned_capacity(client):
    """Test case for purchase_provisioned_capacity

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/{account_id}/provisioned-capacity'.format(account_id='account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_tags_from_vault(client):
    """Test case for remove_tags_from_vault

    
    """
    body = openapi_server.RemoveTagsFromVaultRequest()
    params = [('operation', 'operation_example')]
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
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/{account_id}/vaults/{vault_name}/tags#operation=remove'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_data_retrieval_policy(client):
    """Test case for set_data_retrieval_policy

    
    """
    body = openapi_server.SetDataRetrievalPolicyRequest()
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
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{account_id}/policies/data-retrieval'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_vault_access_policy(client):
    """Test case for set_vault_access_policy

    
    """
    body = openapi_server.SetVaultAccessPolicyRequest()
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
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{account_id}/vaults/{vault_name}/access-policy'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_vault_notifications(client):
    """Test case for set_vault_notifications

    
    """
    body = openapi_server.SetVaultNotificationsRequest()
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
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{account_id}/vaults/{vault_name}/notification-configuration'.format(account_id='account_id_example', vault_name='vault_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upload_archive(client):
    """Test case for upload_archive

    
    """
    body = openapi_server.UploadMultipartPartRequest()
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
        'x_amz_archive_description': 'x_amz_archive_description_example',
        'x_amz_sha256_tree_hash': 'x_amz_sha256_tree_hash_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/{account_id}/vaults/{vault_name}/archives'.format(vault_name='vault_name_example', account_id='account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upload_multipart_part(client):
    """Test case for upload_multipart_part

    
    """
    body = openapi_server.UploadMultipartPartRequest()
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
        'x_amz_sha256_tree_hash': 'x_amz_sha256_tree_hash_example',
        'content_range': 'content_range_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{account_id}/vaults/{vault_name}/multipart-uploads/{upload_id}'.format(account_id='account_id_example', vault_name='vault_name_example', upload_id='upload_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

