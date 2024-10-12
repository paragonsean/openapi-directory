from typing import List, Dict
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
from openapi_server import util


async def g_et_cancel_job(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, job_id, operation, action, version, api_version=None) -> web.Response:
    """g_et_cancel_job

    This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param job_id: 
    :type job_id: str
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param api_version: 
    :type api_version: str

    """
    return web.Response(status=200)


async def g_et_create_job(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, job_type, manifest, validate_only, operation, action, version, manifest_addendum=None, api_version=None) -> web.Response:
    """g_et_create_job

    This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param job_type: 
    :type job_type: str
    :param manifest: 
    :type manifest: str
    :param validate_only: 
    :type validate_only: bool
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param manifest_addendum: 
    :type manifest_addendum: str
    :param api_version: 
    :type api_version: str

    """
    return web.Response(status=200)


async def g_et_get_shipping_label(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, job_ids, operation, action, version, name=None, company=None, phone_number=None, country=None, state_or_province=None, city=None, postal_code=None, street1=None, street2=None, street3=None, api_version=None) -> web.Response:
    """g_et_get_shipping_label

    This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param job_ids: 
    :type job_ids: List[str]
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param name: 
    :type name: str
    :param company: 
    :type company: str
    :param phone_number: 
    :type phone_number: str
    :param country: 
    :type country: str
    :param state_or_province: 
    :type state_or_province: str
    :param city: 
    :type city: str
    :param postal_code: 
    :type postal_code: str
    :param street1: 
    :type street1: str
    :param street2: 
    :type street2: str
    :param street3: 
    :type street3: str
    :param api_version: 
    :type api_version: str

    """
    return web.Response(status=200)


async def g_et_get_status(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, job_id, operation, action, version, api_version=None) -> web.Response:
    """g_et_get_status

    This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param job_id: 
    :type job_id: str
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param api_version: 
    :type api_version: str

    """
    return web.Response(status=200)


async def g_et_list_jobs(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, operation, action, version, max_jobs=None, marker=None, api_version=None) -> web.Response:
    """g_et_list_jobs

    This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param max_jobs: 
    :type max_jobs: int
    :param marker: 
    :type marker: str
    :param api_version: 
    :type api_version: str

    """
    return web.Response(status=200)


async def g_et_update_job(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, job_id, manifest, job_type, validate_only, operation, action, version, api_version=None) -> web.Response:
    """g_et_update_job

    You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param job_id: 
    :type job_id: str
    :param manifest: 
    :type manifest: str
    :param job_type: 
    :type job_type: str
    :param validate_only: 
    :type validate_only: bool
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param api_version: 
    :type api_version: str

    """
    return web.Response(status=200)


async def p_ost_cancel_job(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, operation, action, version, body=None) -> web.Response:
    """p_ost_cancel_job

    This operation cancels a specified job. Only the job owner can cancel it. The operation fails if the job has already started or is complete.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = CancelJobInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_job(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, operation, action, version, body=None) -> web.Response:
    """p_ost_create_job

    This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateJobInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_shipping_label(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, operation, action, version, body=None) -> web.Response:
    """p_ost_get_shipping_label

    This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetShippingLabelInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_status(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, operation, action, version, body=None) -> web.Response:
    """p_ost_get_status

    This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetStatusInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_jobs(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, operation, action, version, max_jobs=None, marker=None, body=None) -> web.Response:
    """p_ost_list_jobs

    This operation returns the jobs associated with the requester. AWS Import/Export lists the jobs in reverse chronological order based on the date of creation. For example if Job Test1 was created 2009Dec30 and Test2 was created 2010Feb05, the ListJobs operation would return Test2 followed by Test1.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param max_jobs: Pagination limit
    :type max_jobs: str
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListJobsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_job(request: web.Request, aws_access_key_id, signature_method, signature_version, timestamp, signature, operation, action, version, body=None) -> web.Response:
    """p_ost_update_job

    You use this operation to change the parameters specified in the original manifest file by supplying a new manifest file. The manifest file attached to this request replaces the original manifest file. You can only use the operation after a CreateJob request but before the data transfer starts and you can only use it on jobs you own.

    :param aws_access_key_id: 
    :type aws_access_key_id: str
    :param signature_method: 
    :type signature_method: str
    :param signature_version: 
    :type signature_version: str
    :param timestamp: 
    :type timestamp: str
    :param signature: 
    :type signature: str
    :param operation: 
    :type operation: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateJobInput.from_dict(body)
    return web.Response(status=200)
