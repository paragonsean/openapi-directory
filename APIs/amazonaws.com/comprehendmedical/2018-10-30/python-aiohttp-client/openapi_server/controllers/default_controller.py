from typing import List, Dict
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
from openapi_server import util


async def describe_entities_detection_v2_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_entities_detection_v2_job

    Gets the properties associated with a medical entities detection job. Use this operation to get the status of a detection job.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeEntitiesDetectionV2JobRequest.from_dict(body)
    return web.Response(status=200)


async def describe_icd10_cm_inference_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_icd10_cm_inference_job

    Gets the properties associated with an InferICD10CM job. Use this operation to get the status of an inference job.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeICD10CMInferenceJobRequest.from_dict(body)
    return web.Response(status=200)


async def describe_phi_detection_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_phi_detection_job

    Gets the properties associated with a protected health information (PHI) detection job. Use this operation to get the status of a detection job.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribePHIDetectionJobRequest.from_dict(body)
    return web.Response(status=200)


async def describe_rx_norm_inference_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_rx_norm_inference_job

    Gets the properties associated with an InferRxNorm job. Use this operation to get the status of an inference job.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeRxNormInferenceJobRequest.from_dict(body)
    return web.Response(status=200)


async def describe_snomedct_inference_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_snomedct_inference_job

     Gets the properties associated with an InferSNOMEDCT job. Use this operation to get the status of an inference job. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeSNOMEDCTInferenceJobRequest.from_dict(body)
    return web.Response(status=200)


async def detect_entities(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """detect_entities

    &lt;p&gt;The &lt;code&gt;DetectEntities&lt;/code&gt; operation is deprecated. You should use the &lt;a&gt;DetectEntitiesV2&lt;/a&gt; operation instead.&lt;/p&gt; &lt;p&gt;Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DetectEntitiesRequest.from_dict(body)
    return web.Response(status=200)


async def detect_entities_v2(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """detect_entities_v2

    &lt;p&gt;Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information. Amazon Comprehend Medical only detects medical entities in English language texts.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;DetectEntitiesV2&lt;/code&gt; operation replaces the &lt;a&gt;DetectEntities&lt;/a&gt; operation. This new action uses a different model for determining the entities in your medical text and changes the way that some entities are returned in the output. You should use the &lt;code&gt;DetectEntitiesV2&lt;/code&gt; operation in all new applications.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;DetectEntitiesV2&lt;/code&gt; operation returns the &lt;code&gt;Acuity&lt;/code&gt; and &lt;code&gt;Direction&lt;/code&gt; entities as attributes instead of types. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DetectEntitiesV2Request.from_dict(body)
    return web.Response(status=200)


async def detect_phi(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """detect_phi

    Inspects the clinical text for protected health information (PHI) entities and returns the entity category, location, and confidence score for each entity. Amazon Comprehend Medical only detects entities in English language texts.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DetectPHIRequest.from_dict(body)
    return web.Response(status=200)


async def infer_icd10_cm(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """infer_icd10_cm

    InferICD10CM detects medical conditions as entities listed in a patient record and links those entities to normalized concept identifiers in the ICD-10-CM knowledge base from the Centers for Disease Control. Amazon Comprehend Medical only detects medical entities in English language texts. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = InferICD10CMRequest.from_dict(body)
    return web.Response(status=200)


async def infer_rx_norm(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """infer_rx_norm

    InferRxNorm detects medications as entities listed in a patient record and links to the normalized concept identifiers in the RxNorm database from the National Library of Medicine. Amazon Comprehend Medical only detects medical entities in English language texts. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = InferRxNormRequest.from_dict(body)
    return web.Response(status=200)


async def infer_snomedct(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """infer_snomedct

     InferSNOMEDCT detects possible medical concepts as entities and links them to codes from the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED-CT) ontology

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = InferSNOMEDCTRequest.from_dict(body)
    return web.Response(status=200)


async def list_entities_detection_v2_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_entities_detection_v2_jobs

    Gets a list of medical entity detection jobs that you have submitted.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListEntitiesDetectionV2JobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_icd10_cm_inference_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_icd10_cm_inference_jobs

    Gets a list of InferICD10CM jobs that you have submitted.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListICD10CMInferenceJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_phi_detection_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_phi_detection_jobs

    Gets a list of protected health information (PHI) detection jobs you have submitted.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListPHIDetectionJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_rx_norm_inference_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_rx_norm_inference_jobs

    Gets a list of InferRxNorm jobs that you have submitted.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListRxNormInferenceJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_snomedct_inference_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_snomedct_inference_jobs

     Gets a list of InferSNOMEDCT jobs a user has submitted. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListSNOMEDCTInferenceJobsRequest.from_dict(body)
    return web.Response(status=200)


async def start_entities_detection_v2_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_entities_detection_v2_job

    Starts an asynchronous medical entity detection job for a collection of documents. Use the &lt;code&gt;DescribeEntitiesDetectionV2Job&lt;/code&gt; operation to track the status of a job.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartEntitiesDetectionV2JobRequest.from_dict(body)
    return web.Response(status=200)


async def start_icd10_cm_inference_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_icd10_cm_inference_job

    Starts an asynchronous job to detect medical conditions and link them to the ICD-10-CM ontology. Use the &lt;code&gt;DescribeICD10CMInferenceJob&lt;/code&gt; operation to track the status of a job.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartICD10CMInferenceJobRequest.from_dict(body)
    return web.Response(status=200)


async def start_phi_detection_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_phi_detection_job

    Starts an asynchronous job to detect protected health information (PHI). Use the &lt;code&gt;DescribePHIDetectionJob&lt;/code&gt; operation to track the status of a job.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartPHIDetectionJobRequest.from_dict(body)
    return web.Response(status=200)


async def start_rx_norm_inference_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_rx_norm_inference_job

    Starts an asynchronous job to detect medication entities and link them to the RxNorm ontology. Use the &lt;code&gt;DescribeRxNormInferenceJob&lt;/code&gt; operation to track the status of a job.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartRxNormInferenceJobRequest.from_dict(body)
    return web.Response(status=200)


async def start_snomedct_inference_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_snomedct_inference_job

     Starts an asynchronous job to detect medical concepts and link them to the SNOMED-CT ontology. Use the DescribeSNOMEDCTInferenceJob operation to track the status of a job. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartSNOMEDCTInferenceJobRequest.from_dict(body)
    return web.Response(status=200)


async def stop_entities_detection_v2_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_entities_detection_v2_job

    Stops a medical entities detection job in progress.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StopEntitiesDetectionV2JobRequest.from_dict(body)
    return web.Response(status=200)


async def stop_icd10_cm_inference_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_icd10_cm_inference_job

    Stops an InferICD10CM inference job in progress.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StopICD10CMInferenceJobRequest.from_dict(body)
    return web.Response(status=200)


async def stop_phi_detection_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_phi_detection_job

    Stops a protected health information (PHI) detection job in progress.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StopPHIDetectionJobRequest.from_dict(body)
    return web.Response(status=200)


async def stop_rx_norm_inference_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_rx_norm_inference_job

    Stops an InferRxNorm inference job in progress.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StopRxNormInferenceJobRequest.from_dict(body)
    return web.Response(status=200)


async def stop_snomedct_inference_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_snomedct_inference_job

     Stops an InferSNOMEDCT inference job in progress. 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StopSNOMEDCTInferenceJobRequest.from_dict(body)
    return web.Response(status=200)
