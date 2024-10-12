# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bucket_permission_exception import BucketPermissionException
from openapi_server.models.cancel_job_input import CancelJobInput
from openapi_server.models.cancel_job_output import CancelJobOutput
from openapi_server.models.canceled_job_id_exception import CanceledJobIdException
from openapi_server.models.create_job_input import CreateJobInput
from openapi_server.models.create_job_output import CreateJobOutput
from openapi_server.models.create_job_quota_exceeded_exception import CreateJobQuotaExceededException
from openapi_server.models.expired_job_id_exception import ExpiredJobIdException
from openapi_server.models.get_shipping_label_input import GetShippingLabelInput
from openapi_server.models.get_shipping_label_output import GetShippingLabelOutput
from openapi_server.models.get_status_input import GetStatusInput
from openapi_server.models.get_status_output import GetStatusOutput
from openapi_server.models.invalid_access_key_id_exception import InvalidAccessKeyIdException
from openapi_server.models.invalid_address_exception import InvalidAddressException
from openapi_server.models.invalid_customs_exception import InvalidCustomsException
from openapi_server.models.invalid_file_system_exception import InvalidFileSystemException
from openapi_server.models.invalid_job_id_exception import InvalidJobIdException
from openapi_server.models.invalid_manifest_field_exception import InvalidManifestFieldException
from openapi_server.models.invalid_parameter_exception import InvalidParameterException
from openapi_server.models.invalid_version_exception import InvalidVersionException
from openapi_server.models.list_jobs_input import ListJobsInput
from openapi_server.models.list_jobs_output import ListJobsOutput
from openapi_server.models.malformed_manifest_exception import MalformedManifestException
from openapi_server.models.missing_customs_exception import MissingCustomsException
from openapi_server.models.missing_manifest_field_exception import MissingManifestFieldException
from openapi_server.models.missing_parameter_exception import MissingParameterException
from openapi_server.models.multiple_regions_exception import MultipleRegionsException
from openapi_server.models.no_such_bucket_exception import NoSuchBucketException
from openapi_server.models.unable_to_cancel_job_id_exception import UnableToCancelJobIdException
from openapi_server.models.unable_to_update_job_id_exception import UnableToUpdateJobIdException
from openapi_server.models.update_job_input import UpdateJobInput
from openapi_server.models.update_job_output import UpdateJobOutput


pytestmark = pytest.mark.asyncio

async def test_g_et_cancel_job(client):
    """Test case for g_et_cancel_job

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('JobId', 'job_id_example'),
                    ('APIVersion', 'api_version_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Operation=CancelJob&Action=CancelJob',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_create_job(client):
    """Test case for g_et_create_job

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('JobType', 'job_type_example'),
                    ('Manifest', 'manifest_example'),
                    ('ManifestAddendum', 'manifest_addendum_example'),
                    ('ValidateOnly', True),
                    ('APIVersion', 'api_version_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Operation=CreateJob&Action=CreateJob',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_get_shipping_label(client):
    """Test case for g_et_get_shipping_label

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('jobIds', ['job_ids_example']),
                    ('name', 'name_example'),
                    ('company', 'company_example'),
                    ('phoneNumber', 'phone_number_example'),
                    ('country', 'country_example'),
                    ('stateOrProvince', 'state_or_province_example'),
                    ('city', 'city_example'),
                    ('postalCode', 'postal_code_example'),
                    ('street1', 'street1_example'),
                    ('street2', 'street2_example'),
                    ('street3', 'street3_example'),
                    ('APIVersion', 'api_version_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Operation=GetShippingLabel&Action=GetShippingLabel',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_get_status(client):
    """Test case for g_et_get_status

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('JobId', 'job_id_example'),
                    ('APIVersion', 'api_version_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Operation=GetStatus&Action=GetStatus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_list_jobs(client):
    """Test case for g_et_list_jobs

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('MaxJobs', 56),
                    ('Marker', 'marker_example'),
                    ('APIVersion', 'api_version_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Operation=ListJobs&Action=ListJobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_update_job(client):
    """Test case for g_et_update_job

    
    """
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('JobId', 'job_id_example'),
                    ('Manifest', 'manifest_example'),
                    ('JobType', 'job_type_example'),
                    ('ValidateOnly', True),
                    ('APIVersion', 'api_version_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/#Operation=UpdateJob&Action=UpdateJob',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_cancel_job(client):
    """Test case for p_ost_cancel_job

    
    """
    body = openapi_server.CancelJobInput()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Operation=CancelJob&Action=CancelJob',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_create_job(client):
    """Test case for p_ost_create_job

    
    """
    body = openapi_server.CreateJobInput()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Operation=CreateJob&Action=CreateJob',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_get_shipping_label(client):
    """Test case for p_ost_get_shipping_label

    
    """
    body = openapi_server.GetShippingLabelInput()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Operation=GetShippingLabel&Action=GetShippingLabel',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_get_status(client):
    """Test case for p_ost_get_status

    
    """
    body = openapi_server.GetStatusInput()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Operation=GetStatus&Action=GetStatus',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_list_jobs(client):
    """Test case for p_ost_list_jobs

    
    """
    body = openapi_server.ListJobsInput()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('MaxJobs', 'max_jobs_example'),
                    ('Marker', 'marker_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Operation=ListJobs&Action=ListJobs',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_p_ost_update_job(client):
    """Test case for p_ost_update_job

    
    """
    body = openapi_server.UpdateJobInput()
    params = [('AWSAccessKeyId', 'aws_access_key_id_example'),
                    ('SignatureMethod', 'signature_method_example'),
                    ('SignatureVersion', 'signature_version_example'),
                    ('Timestamp', 'timestamp_example'),
                    ('Signature', 'signature_example'),
                    ('Operation', 'operation_example'),
                    ('Action', 'action_example'),
                    ('Version', 'version_example')]
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#Operation=UpdateJob&Action=UpdateJob',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

