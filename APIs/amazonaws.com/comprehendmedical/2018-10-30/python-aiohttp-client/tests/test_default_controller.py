# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.describe_entities_detection_v2_job_request import DescribeEntitiesDetectionV2JobRequest
from openapi_server.models.describe_entities_detection_v2_job_response import DescribeEntitiesDetectionV2JobResponse
from openapi_server.models.describe_icd10_cm_inference_job_request import DescribeICD10CMInferenceJobRequest
from openapi_server.models.describe_icd10_cm_inference_job_response import DescribeICD10CMInferenceJobResponse
from openapi_server.models.describe_phi_detection_job_request import DescribePHIDetectionJobRequest
from openapi_server.models.describe_phi_detection_job_response import DescribePHIDetectionJobResponse
from openapi_server.models.describe_rx_norm_inference_job_request import DescribeRxNormInferenceJobRequest
from openapi_server.models.describe_rx_norm_inference_job_response import DescribeRxNormInferenceJobResponse
from openapi_server.models.describe_snomedct_inference_job_request import DescribeSNOMEDCTInferenceJobRequest
from openapi_server.models.describe_snomedct_inference_job_response import DescribeSNOMEDCTInferenceJobResponse
from openapi_server.models.detect_entities_request import DetectEntitiesRequest
from openapi_server.models.detect_entities_response import DetectEntitiesResponse
from openapi_server.models.detect_entities_v2_request import DetectEntitiesV2Request
from openapi_server.models.detect_entities_v2_response import DetectEntitiesV2Response
from openapi_server.models.detect_phi_request import DetectPHIRequest
from openapi_server.models.detect_phi_response import DetectPHIResponse
from openapi_server.models.infer_icd10_cm_request import InferICD10CMRequest
from openapi_server.models.infer_icd10_cm_response import InferICD10CMResponse
from openapi_server.models.infer_rx_norm_request import InferRxNormRequest
from openapi_server.models.infer_rx_norm_response import InferRxNormResponse
from openapi_server.models.infer_snomedct_request import InferSNOMEDCTRequest
from openapi_server.models.infer_snomedct_response import InferSNOMEDCTResponse
from openapi_server.models.list_entities_detection_v2_jobs_request import ListEntitiesDetectionV2JobsRequest
from openapi_server.models.list_entities_detection_v2_jobs_response import ListEntitiesDetectionV2JobsResponse
from openapi_server.models.list_icd10_cm_inference_jobs_request import ListICD10CMInferenceJobsRequest
from openapi_server.models.list_icd10_cm_inference_jobs_response import ListICD10CMInferenceJobsResponse
from openapi_server.models.list_phi_detection_jobs_request import ListPHIDetectionJobsRequest
from openapi_server.models.list_phi_detection_jobs_response import ListPHIDetectionJobsResponse
from openapi_server.models.list_rx_norm_inference_jobs_request import ListRxNormInferenceJobsRequest
from openapi_server.models.list_rx_norm_inference_jobs_response import ListRxNormInferenceJobsResponse
from openapi_server.models.list_snomedct_inference_jobs_request import ListSNOMEDCTInferenceJobsRequest
from openapi_server.models.list_snomedct_inference_jobs_response import ListSNOMEDCTInferenceJobsResponse
from openapi_server.models.start_entities_detection_v2_job_request import StartEntitiesDetectionV2JobRequest
from openapi_server.models.start_entities_detection_v2_job_response import StartEntitiesDetectionV2JobResponse
from openapi_server.models.start_icd10_cm_inference_job_request import StartICD10CMInferenceJobRequest
from openapi_server.models.start_icd10_cm_inference_job_response import StartICD10CMInferenceJobResponse
from openapi_server.models.start_phi_detection_job_request import StartPHIDetectionJobRequest
from openapi_server.models.start_phi_detection_job_response import StartPHIDetectionJobResponse
from openapi_server.models.start_rx_norm_inference_job_request import StartRxNormInferenceJobRequest
from openapi_server.models.start_rx_norm_inference_job_response import StartRxNormInferenceJobResponse
from openapi_server.models.start_snomedct_inference_job_request import StartSNOMEDCTInferenceJobRequest
from openapi_server.models.start_snomedct_inference_job_response import StartSNOMEDCTInferenceJobResponse
from openapi_server.models.stop_entities_detection_v2_job_request import StopEntitiesDetectionV2JobRequest
from openapi_server.models.stop_entities_detection_v2_job_response import StopEntitiesDetectionV2JobResponse
from openapi_server.models.stop_icd10_cm_inference_job_request import StopICD10CMInferenceJobRequest
from openapi_server.models.stop_icd10_cm_inference_job_response import StopICD10CMInferenceJobResponse
from openapi_server.models.stop_phi_detection_job_request import StopPHIDetectionJobRequest
from openapi_server.models.stop_phi_detection_job_response import StopPHIDetectionJobResponse
from openapi_server.models.stop_rx_norm_inference_job_request import StopRxNormInferenceJobRequest
from openapi_server.models.stop_rx_norm_inference_job_response import StopRxNormInferenceJobResponse
from openapi_server.models.stop_snomedct_inference_job_request import StopSNOMEDCTInferenceJobRequest
from openapi_server.models.stop_snomedct_inference_job_response import StopSNOMEDCTInferenceJobResponse


pytestmark = pytest.mark.asyncio

async def test_describe_entities_detection_v2_job(client):
    """Test case for describe_entities_detection_v2_job

    
    """
    body = {"JobId":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.DescribeEntitiesDetectionV2Job',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_icd10_cm_inference_job(client):
    """Test case for describe_icd10_cm_inference_job

    
    """
    body = {"JobId":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.DescribeICD10CMInferenceJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_phi_detection_job(client):
    """Test case for describe_phi_detection_job

    
    """
    body = {"JobId":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.DescribePHIDetectionJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_rx_norm_inference_job(client):
    """Test case for describe_rx_norm_inference_job

    
    """
    body = {"JobId":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.DescribeRxNormInferenceJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_snomedct_inference_job(client):
    """Test case for describe_snomedct_inference_job

    
    """
    body = {"JobId":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.DescribeSNOMEDCTInferenceJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detect_entities(client):
    """Test case for detect_entities

    
    """
    body = {"Text":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.DetectEntities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detect_entities_v2(client):
    """Test case for detect_entities_v2

    
    """
    body = {"Text":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.DetectEntitiesV2',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detect_phi(client):
    """Test case for detect_phi

    
    """
    body = {"Text":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.DetectPHI',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_infer_icd10_cm(client):
    """Test case for infer_icd10_cm

    
    """
    body = {"Text":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.InferICD10CM',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_infer_rx_norm(client):
    """Test case for infer_rx_norm

    
    """
    body = {"Text":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.InferRxNorm',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_infer_snomedct(client):
    """Test case for infer_snomedct

    
    """
    body = {"Text":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.InferSNOMEDCT',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_entities_detection_v2_jobs(client):
    """Test case for list_entities_detection_v2_jobs

    
    """
    body = {"NextToken":"","Filter":{"JobStatus":"","SubmitTimeAfter":"","SubmitTimeBefore":"","JobName":""},"MaxResults":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.ListEntitiesDetectionV2Jobs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_icd10_cm_inference_jobs(client):
    """Test case for list_icd10_cm_inference_jobs

    
    """
    body = {"NextToken":"","Filter":{"JobStatus":"","SubmitTimeAfter":"","SubmitTimeBefore":"","JobName":""},"MaxResults":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.ListICD10CMInferenceJobs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_phi_detection_jobs(client):
    """Test case for list_phi_detection_jobs

    
    """
    body = {"NextToken":"","Filter":{"JobStatus":"","SubmitTimeAfter":"","SubmitTimeBefore":"","JobName":""},"MaxResults":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.ListPHIDetectionJobs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_rx_norm_inference_jobs(client):
    """Test case for list_rx_norm_inference_jobs

    
    """
    body = {"NextToken":"","Filter":{"JobStatus":"","SubmitTimeAfter":"","SubmitTimeBefore":"","JobName":""},"MaxResults":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.ListRxNormInferenceJobs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_snomedct_inference_jobs(client):
    """Test case for list_snomedct_inference_jobs

    
    """
    body = {"NextToken":"","Filter":{"JobStatus":"","SubmitTimeAfter":"","SubmitTimeBefore":"","JobName":""},"MaxResults":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.ListSNOMEDCTInferenceJobs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_entities_detection_v2_job(client):
    """Test case for start_entities_detection_v2_job

    
    """
    body = {"ClientRequestToken":"","KMSKey":"","LanguageCode":"","DataAccessRoleArn":"","OutputDataConfig":{"S3Bucket":"","S3Key":""},"JobName":"","InputDataConfig":{"S3Bucket":"","S3Key":""}}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.StartEntitiesDetectionV2Job',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_icd10_cm_inference_job(client):
    """Test case for start_icd10_cm_inference_job

    
    """
    body = {"ClientRequestToken":"","KMSKey":"","LanguageCode":"","DataAccessRoleArn":"","OutputDataConfig":{"S3Bucket":"","S3Key":""},"JobName":"","InputDataConfig":{"S3Bucket":"","S3Key":""}}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.StartICD10CMInferenceJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_phi_detection_job(client):
    """Test case for start_phi_detection_job

    
    """
    body = {"ClientRequestToken":"","KMSKey":"","LanguageCode":"","DataAccessRoleArn":"","OutputDataConfig":{"S3Bucket":"","S3Key":""},"JobName":"","InputDataConfig":{"S3Bucket":"","S3Key":""}}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.StartPHIDetectionJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_rx_norm_inference_job(client):
    """Test case for start_rx_norm_inference_job

    
    """
    body = {"ClientRequestToken":"","KMSKey":"","LanguageCode":"","DataAccessRoleArn":"","OutputDataConfig":{"S3Bucket":"","S3Key":""},"JobName":"","InputDataConfig":{"S3Bucket":"","S3Key":""}}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.StartRxNormInferenceJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_snomedct_inference_job(client):
    """Test case for start_snomedct_inference_job

    
    """
    body = {"ClientRequestToken":"","KMSKey":"","LanguageCode":"","DataAccessRoleArn":"","OutputDataConfig":{"S3Bucket":"","S3Key":""},"JobName":"","InputDataConfig":{"S3Bucket":"","S3Key":""}}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.StartSNOMEDCTInferenceJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_entities_detection_v2_job(client):
    """Test case for stop_entities_detection_v2_job

    
    """
    body = {"JobId":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.StopEntitiesDetectionV2Job',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_icd10_cm_inference_job(client):
    """Test case for stop_icd10_cm_inference_job

    
    """
    body = {"JobId":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.StopICD10CMInferenceJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_phi_detection_job(client):
    """Test case for stop_phi_detection_job

    
    """
    body = {"JobId":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.StopPHIDetectionJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_rx_norm_inference_job(client):
    """Test case for stop_rx_norm_inference_job

    
    """
    body = {"JobId":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.StopRxNormInferenceJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_snomedct_inference_job(client):
    """Test case for stop_snomedct_inference_job

    
    """
    body = {"JobId":""}
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
        path='/#X-Amz-Target=ComprehendMedical_20181030.StopSNOMEDCTInferenceJob',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

