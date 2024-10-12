# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_chunk_output import GetChunkOutput
from openapi_server.models.get_object_metadata_output import GetObjectMetadataOutput
from openapi_server.models.list_chunks_output import ListChunksOutput
from openapi_server.models.list_objects_output import ListObjectsOutput
from openapi_server.models.notify_object_complete_output import NotifyObjectCompleteOutput
from openapi_server.models.notify_object_complete_request import NotifyObjectCompleteRequest
from openapi_server.models.put_chunk_output import PutChunkOutput
from openapi_server.models.put_chunk_request import PutChunkRequest
from openapi_server.models.put_object_output import PutObjectOutput
from openapi_server.models.put_object_request import PutObjectRequest
from openapi_server.models.start_object_output import StartObjectOutput
from openapi_server.models.start_object_request import StartObjectRequest


pytestmark = pytest.mark.asyncio

async def test_delete_object(client):
    """Test case for delete_object

    
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
        path='/backup-jobs/{job_id}/object/{object_name}'.format(job_id='job_id_example', object_name='object_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_chunk(client):
    """Test case for get_chunk

    
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
        path='/restore-jobs/{job_id}/chunk/{chunk_token}'.format(job_id='job_id_example', chunk_token='chunk_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_object_metadata(client):
    """Test case for get_object_metadata

    
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
        path='/restore-jobs/{job_id}/object/{object_token}/metadata'.format(job_id='job_id_example', object_token='object_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_chunks(client):
    """Test case for list_chunks

    
    """
    params = [('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        path='/restore-jobs/{job_id}/chunks/{object_token}/list'.format(job_id='job_id_example', object_token='object_token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_objects(client):
    """Test case for list_objects

    
    """
    params = [('starting-object-name', 'starting_object_name_example'),
                    ('starting-object-prefix', 'starting_object_prefix_example'),
                    ('max-results', 56),
                    ('next-token', 'next_token_example'),
                    ('created-before', '2013-10-20T19:20:30+01:00'),
                    ('created-after', '2013-10-20T19:20:30+01:00'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        path='/restore-jobs/{job_id}/objects/list'.format(job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notify_object_complete(client):
    """Test case for notify_object_complete

    
    """
    body = openapi_server.NotifyObjectCompleteRequest()
    params = [('checksum', 'checksum_example'),
                    ('checksum-algorithm', 'checksum_algorithm_example'),
                    ('metadata-string', 'metadata_string_example'),
                    ('metadata-blob-length', 56),
                    ('metadata-checksum', 'metadata_checksum_example'),
                    ('metadata-checksum-algorithm', 'metadata_checksum_algorithm_example')]
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
        path='/backup-jobs/{job_id}/object/{upload_id}/complete#checksum&checksum-algorithm'.format(job_id='job_id_example', upload_id='upload_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_chunk(client):
    """Test case for put_chunk

    
    """
    body = openapi_server.PutChunkRequest()
    params = [('length', 56),
                    ('checksum', 'checksum_example'),
                    ('checksum-algorithm', 'checksum_algorithm_example')]
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
        path='/backup-jobs/{job_id}/chunk/{upload_id}/{chunk_indexlengthchecksumchecksum_algorith}'.format(job_id='job_id_example', upload_id='upload_id_example', chunk_index=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_object(client):
    """Test case for put_object

    
    """
    body = openapi_server.PutObjectRequest()
    params = [('metadata-string', 'metadata_string_example'),
                    ('length', 56),
                    ('checksum', 'checksum_example'),
                    ('checksum-algorithm', 'checksum_algorithm_example'),
                    ('object-checksum', 'object_checksum_example'),
                    ('object-checksum-algorithm', 'object_checksum_algorithm_example'),
                    ('throwOnDuplicate', True)]
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
        path='/backup-jobs/{job_id}/object/{object_name}/put-object'.format(job_id='job_id_example', object_name='object_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_object(client):
    """Test case for start_object

    
    """
    body = openapi_server.StartObjectRequest()
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
        path='/backup-jobs/{job_id}/object/{object_name}'.format(job_id='job_id_example', object_name='object_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

