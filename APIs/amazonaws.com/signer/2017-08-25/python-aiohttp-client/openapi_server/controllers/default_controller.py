from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_profile_permission_request import AddProfilePermissionRequest
from openapi_server.models.add_profile_permission_response import AddProfilePermissionResponse
from openapi_server.models.describe_signing_job_response import DescribeSigningJobResponse
from openapi_server.models.get_revocation_status_response import GetRevocationStatusResponse
from openapi_server.models.get_signing_platform_response import GetSigningPlatformResponse
from openapi_server.models.get_signing_profile_response import GetSigningProfileResponse
from openapi_server.models.list_profile_permissions_response import ListProfilePermissionsResponse
from openapi_server.models.list_signing_jobs_response import ListSigningJobsResponse
from openapi_server.models.list_signing_platforms_response import ListSigningPlatformsResponse
from openapi_server.models.list_signing_profiles_response import ListSigningProfilesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_signing_profile_request import PutSigningProfileRequest
from openapi_server.models.put_signing_profile_response import PutSigningProfileResponse
from openapi_server.models.remove_profile_permission_response import RemoveProfilePermissionResponse
from openapi_server.models.revoke_signature_request import RevokeSignatureRequest
from openapi_server.models.revoke_signing_profile_request import RevokeSigningProfileRequest
from openapi_server.models.sign_payload_request import SignPayloadRequest
from openapi_server.models.sign_payload_response import SignPayloadResponse
from openapi_server.models.signing_profile_status import SigningProfileStatus
from openapi_server.models.start_signing_job_request import StartSigningJobRequest
from openapi_server.models.start_signing_job_response import StartSigningJobResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server import util


async def add_profile_permission(request: web.Request, profile_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_profile_permission

    Adds cross-account permissions to a signing profile.

    :param profile_name: The human-readable name of the signing profile.
    :type profile_name: str
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
    body = AddProfilePermissionRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_signing_profile(request: web.Request, profile_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_signing_profile

    Changes the state of an &lt;code&gt;ACTIVE&lt;/code&gt; signing profile to &lt;code&gt;CANCELED&lt;/code&gt;. A canceled profile is still viewable with the &lt;code&gt;ListSigningProfiles&lt;/code&gt; operation, but it cannot perform new signing jobs, and is deleted two years after cancelation.

    :param profile_name: The name of the signing profile to be canceled.
    :type profile_name: str
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
    return web.Response(status=200)


async def describe_signing_job(request: web.Request, job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_signing_job

    Returns information about a specific code signing job. You specify the job by using the &lt;code&gt;jobId&lt;/code&gt; value that is returned by the &lt;a&gt;StartSigningJob&lt;/a&gt; operation. 

    :param job_id: The ID of the signing job on input.
    :type job_id: str
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
    return web.Response(status=200)


async def get_revocation_status(request: web.Request, signature_timestamp, platform_id, profile_version_arn, job_arn, certificate_hashes, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_revocation_status

    Retrieves the revocation status of one or more of the signing profile, signing job, and signing certificate.

    :param signature_timestamp: The timestamp of the signature that validates the profile or job.
    :type signature_timestamp: str
    :param platform_id: The ID of a signing platform. 
    :type platform_id: str
    :param profile_version_arn: The version of a signing profile.
    :type profile_version_arn: str
    :param job_arn: The ARN of a signing job.
    :type job_arn: str
    :param certificate_hashes: &lt;p&gt;A list of composite signed hashes that identify certificates.&lt;/p&gt; &lt;p&gt;A certificate identifier consists of a subject certificate TBS hash (signed by the parent CA) combined with a parent CA TBS hash (signed by the parent CA’s CA). Root certificates are defined as their own CA.&lt;/p&gt;
    :type certificate_hashes: List[str]
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
    signature_timestamp = util.deserialize_datetime(signature_timestamp)
    return web.Response(status=200)


async def get_signing_platform(request: web.Request, platform_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_signing_platform

    Returns information on a specific signing platform.

    :param platform_id: The ID of the target signing platform.
    :type platform_id: str
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
    return web.Response(status=200)


async def get_signing_profile(request: web.Request, profile_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, profile_owner=None) -> web.Response:
    """get_signing_profile

    Returns information on a specific signing profile.

    :param profile_name: The name of the target signing profile.
    :type profile_name: str
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
    :param profile_owner: The AWS account ID of the profile owner.
    :type profile_owner: str

    """
    return web.Response(status=200)


async def list_profile_permissions(request: web.Request, profile_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_profile_permissions

    Lists the cross-account permissions associated with a signing profile.

    :param profile_name: Name of the signing profile containing the cross-account permissions.
    :type profile_name: str
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
    :param next_token: String for specifying the next set of paginated results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_signing_jobs(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, status=None, platform_id=None, requested_by=None, max_results=None, next_token=None, is_revoked=None, signature_expires_before=None, signature_expires_after=None, job_invoker=None) -> web.Response:
    """list_signing_jobs

    Lists all your signing jobs. You can use the &lt;code&gt;maxResults&lt;/code&gt; parameter to limit the number of signing jobs that are returned in the response. If additional jobs remain to be listed, code signing returns a &lt;code&gt;nextToken&lt;/code&gt; value. Use this value in subsequent calls to &lt;code&gt;ListSigningJobs&lt;/code&gt; to fetch the remaining values. You can continue calling &lt;code&gt;ListSigningJobs&lt;/code&gt; with your &lt;code&gt;maxResults&lt;/code&gt; parameter and with new values that code signing returns in the &lt;code&gt;nextToken&lt;/code&gt; parameter until all of your signing jobs have been returned. 

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
    :param status: A status value with which to filter your results.
    :type status: str
    :param platform_id: The ID of microcontroller platform that you specified for the distribution of your code image.
    :type platform_id: str
    :param requested_by: The IAM principal that requested the signing job.
    :type requested_by: str
    :param max_results: Specifies the maximum number of items to return in the response. Use this parameter when paginating results. If additional items exist beyond the number you specify, the &lt;code&gt;nextToken&lt;/code&gt; element is set in the response. Use the &lt;code&gt;nextToken&lt;/code&gt; value in a subsequent request to retrieve additional items. 
    :type max_results: int
    :param next_token: String for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of &lt;code&gt;nextToken&lt;/code&gt; from the response that you just received.
    :type next_token: str
    :param is_revoked: Filters results to return only signing jobs with revoked signatures.
    :type is_revoked: bool
    :param signature_expires_before: Filters results to return only signing jobs with signatures expiring before a specified timestamp.
    :type signature_expires_before: str
    :param signature_expires_after: Filters results to return only signing jobs with signatures expiring after a specified timestamp.
    :type signature_expires_after: str
    :param job_invoker: Filters results to return only signing jobs initiated by a specified IAM entity.
    :type job_invoker: str

    """
    signature_expires_before = util.deserialize_datetime(signature_expires_before)
    signature_expires_after = util.deserialize_datetime(signature_expires_after)
    return web.Response(status=200)


async def list_signing_platforms(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, category=None, partner=None, target=None, max_results=None, next_token=None) -> web.Response:
    """list_signing_platforms

    Lists all signing platforms available in code signing that match the request parameters. If additional jobs remain to be listed, code signing returns a &lt;code&gt;nextToken&lt;/code&gt; value. Use this value in subsequent calls to &lt;code&gt;ListSigningJobs&lt;/code&gt; to fetch the remaining values. You can continue calling &lt;code&gt;ListSigningJobs&lt;/code&gt; with your &lt;code&gt;maxResults&lt;/code&gt; parameter and with new values that code signing returns in the &lt;code&gt;nextToken&lt;/code&gt; parameter until all of your signing jobs have been returned.

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
    :param category: The category type of a signing platform.
    :type category: str
    :param partner: Any partner entities connected to a signing platform.
    :type partner: str
    :param target: The validation template that is used by the target signing platform.
    :type target: str
    :param max_results: The maximum number of results to be returned by this operation.
    :type max_results: int
    :param next_token: Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of &lt;code&gt;nextToken&lt;/code&gt; from the response that you just received.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_signing_profiles(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, include_canceled=None, max_results=None, next_token=None, platform_id=None, statuses=None) -> web.Response:
    """list_signing_profiles

    Lists all available signing profiles in your AWS account. Returns only profiles with an &lt;code&gt;ACTIVE&lt;/code&gt; status unless the &lt;code&gt;includeCanceled&lt;/code&gt; request field is set to &lt;code&gt;true&lt;/code&gt;. If additional jobs remain to be listed, code signing returns a &lt;code&gt;nextToken&lt;/code&gt; value. Use this value in subsequent calls to &lt;code&gt;ListSigningJobs&lt;/code&gt; to fetch the remaining values. You can continue calling &lt;code&gt;ListSigningJobs&lt;/code&gt; with your &lt;code&gt;maxResults&lt;/code&gt; parameter and with new values that code signing returns in the &lt;code&gt;nextToken&lt;/code&gt; parameter until all of your signing jobs have been returned.

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
    :param include_canceled: Designates whether to include profiles with the status of &lt;code&gt;CANCELED&lt;/code&gt;.
    :type include_canceled: bool
    :param max_results: The maximum number of profiles to be returned.
    :type max_results: int
    :param next_token: Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of &lt;code&gt;nextToken&lt;/code&gt; from the response that you just received.
    :type next_token: str
    :param platform_id: Filters results to return only signing jobs initiated for a specified signing platform.
    :type platform_id: str
    :param statuses: Filters results to return only signing jobs with statuses in the specified list.
    :type statuses: list | bytes

    """
    statuses = [SigningProfileStatus.from_dict(d) for d in statuses]
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Returns a list of the tags associated with a signing profile resource.

    :param resource_arn: The Amazon Resource Name (ARN) for the signing profile.
    :type resource_arn: str
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
    return web.Response(status=200)


async def put_signing_profile(request: web.Request, profile_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_signing_profile

    Creates a signing profile. A signing profile is a code signing template that can be used to carry out a pre-defined signing job. 

    :param profile_name: The name of the signing profile to be created.
    :type profile_name: str
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
    body = PutSigningProfileRequest.from_dict(body)
    return web.Response(status=200)


async def remove_profile_permission(request: web.Request, profile_name, revision_id, statement_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_profile_permission

    Removes cross-account permissions from a signing profile.

    :param profile_name: A human-readable name for the signing profile with permissions to be removed.
    :type profile_name: str
    :param revision_id: An identifier for the current revision of the signing profile permissions.
    :type revision_id: str
    :param statement_id: A unique identifier for the cross-account permissions statement.
    :type statement_id: str
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
    return web.Response(status=200)


async def revoke_signature(request: web.Request, job_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """revoke_signature

    Changes the state of a signing job to REVOKED. This indicates that the signature is no longer valid.

    :param job_id: ID of the signing job to be revoked.
    :type job_id: str
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
    body = RevokeSignatureRequest.from_dict(body)
    return web.Response(status=200)


async def revoke_signing_profile(request: web.Request, profile_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """revoke_signing_profile

    Changes the state of a signing profile to REVOKED. This indicates that signatures generated using the signing profile after an effective start date are no longer valid.

    :param profile_name: The name of the signing profile to be revoked.
    :type profile_name: str
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
    body = RevokeSigningProfileRequest.from_dict(body)
    return web.Response(status=200)


async def sign_payload(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """sign_payload

    Signs a binary payload and returns a signature envelope.

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
    body = SignPayloadRequest.from_dict(body)
    return web.Response(status=200)


async def start_signing_job(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_signing_job

    &lt;p&gt;Initiates a signing job to be performed on the code provided. Signing jobs are viewable by the &lt;code&gt;ListSigningJobs&lt;/code&gt; operation for two years after they are performed. Note the following requirements: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; You must create an Amazon S3 source bucket. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html\&quot;&gt;Creating a Bucket&lt;/a&gt; in the &lt;i&gt;Amazon S3 Getting Started Guide&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Your S3 source bucket must be version enabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You must create an S3 destination bucket. Code signing uses your S3 destination bucket to write your signed code.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You specify the name of the source and destination buckets when calling the &lt;code&gt;StartSigningJob&lt;/code&gt; operation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You must also specify a request token that identifies your request to code signing.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can call the &lt;a&gt;DescribeSigningJob&lt;/a&gt; and the &lt;a&gt;ListSigningJobs&lt;/a&gt; actions after you call &lt;code&gt;StartSigningJob&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For a Java example that shows how to use this action, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/signer/latest/developerguide/api-startsigningjob.html\&quot;&gt;StartSigningJob&lt;/a&gt;.&lt;/p&gt;

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
    body = StartSigningJobRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds one or more tags to a signing profile. Tags are labels that you can use to identify and organize your AWS resources. Each tag consists of a key and an optional value. To specify the signing profile, use its Amazon Resource Name (ARN). To specify the tag, use a key-value pair.

    :param resource_arn: The Amazon Resource Name (ARN) for the signing profile.
    :type resource_arn: str
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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes one or more tags from a signing profile. To remove the tags, specify a list of tag keys.

    :param resource_arn: The Amazon Resource Name (ARN) for the signing profile.
    :type resource_arn: str
    :param tag_keys: A list of tag keys to be removed from the signing profile.
    :type tag_keys: List[str]
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
    return web.Response(status=200)
