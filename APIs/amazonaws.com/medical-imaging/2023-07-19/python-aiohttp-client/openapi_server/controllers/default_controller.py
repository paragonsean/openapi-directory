from typing import List, Dict
from aiohttp import web

from openapi_server.models.copy_image_set_request import CopyImageSetRequest
from openapi_server.models.copy_image_set_response import CopyImageSetResponse
from openapi_server.models.create_datastore_request import CreateDatastoreRequest
from openapi_server.models.create_datastore_response import CreateDatastoreResponse
from openapi_server.models.delete_datastore_response import DeleteDatastoreResponse
from openapi_server.models.delete_image_set_response import DeleteImageSetResponse
from openapi_server.models.get_dicom_import_job_response import GetDICOMImportJobResponse
from openapi_server.models.get_datastore_response import GetDatastoreResponse
from openapi_server.models.get_image_frame_request import GetImageFrameRequest
from openapi_server.models.get_image_frame_response import GetImageFrameResponse
from openapi_server.models.get_image_set_metadata_response import GetImageSetMetadataResponse
from openapi_server.models.get_image_set_response import GetImageSetResponse
from openapi_server.models.list_dicom_import_jobs_response import ListDICOMImportJobsResponse
from openapi_server.models.list_datastores_response import ListDatastoresResponse
from openapi_server.models.list_image_set_versions_response import ListImageSetVersionsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.search_image_sets_request import SearchImageSetsRequest
from openapi_server.models.search_image_sets_response import SearchImageSetsResponse
from openapi_server.models.start_dicom_import_job_request import StartDICOMImportJobRequest
from openapi_server.models.start_dicom_import_job_response import StartDICOMImportJobResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_image_set_metadata_request import UpdateImageSetMetadataRequest
from openapi_server.models.update_image_set_metadata_response import UpdateImageSetMetadataResponse
from openapi_server import util


async def copy_image_set(request: web.Request, datastore_id, source_image_set_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """copy_image_set

    Copy an image set.

    :param datastore_id: The data store identifier.
    :type datastore_id: str
    :param source_image_set_id: The source image set identifier.
    :type source_image_set_id: str
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
    body = CopyImageSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_datastore(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_datastore

    Create a data store.

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
    body = CreateDatastoreRequest.from_dict(body)
    return web.Response(status=200)


async def delete_datastore(request: web.Request, datastore_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_datastore

    &lt;p&gt;Delete a data store.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before a data store can be deleted, you must first delete all image sets within it.&lt;/p&gt; &lt;/note&gt;

    :param datastore_id: The data store identifier.
    :type datastore_id: str
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


async def delete_image_set(request: web.Request, datastore_id, image_set_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_image_set

    Delete an image set.

    :param datastore_id: The data store identifier.
    :type datastore_id: str
    :param image_set_id: The image set identifier.
    :type image_set_id: str
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


async def get_datastore(request: web.Request, datastore_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_datastore

    Get data store properties.

    :param datastore_id: The data store identifier.
    :type datastore_id: str
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


async def get_dicom_import_job(request: web.Request, datastore_id, job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_dicom_import_job

    Get the import job properties to learn more about the job or job progress.

    :param datastore_id: The data store identifier.
    :type datastore_id: str
    :param job_id: The import job identifier.
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


async def get_image_frame(request: web.Request, datastore_id, image_set_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_image_frame

    Get an image frame (pixel data) for an image set.

    :param datastore_id: The data store identifier.
    :type datastore_id: str
    :param image_set_id: The image set identifier.
    :type image_set_id: str
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
    body = GetImageFrameRequest.from_dict(body)
    return web.Response(status=200)


async def get_image_set(request: web.Request, datastore_id, image_set_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """get_image_set

    Get image set properties.

    :param datastore_id: The data store identifier.
    :type datastore_id: str
    :param image_set_id: The image set identifier.
    :type image_set_id: str
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
    :param version: The image set version identifier.
    :type version: str

    """
    return web.Response(status=200)


async def get_image_set_metadata(request: web.Request, datastore_id, image_set_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """get_image_set_metadata

    Get metadata attributes for an image set.

    :param datastore_id: The data store identifier.
    :type datastore_id: str
    :param image_set_id: The image set identifier.
    :type image_set_id: str
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
    :param version: The image set version identifier.
    :type version: str

    """
    return web.Response(status=200)


async def list_datastores(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, datastore_status=None, next_token=None, max_results=None) -> web.Response:
    """list_datastores

    List data stores created by this AWS account.

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
    :param datastore_status: The data store status.
    :type datastore_status: str
    :param next_token: The pagination token used to request the list of data stores on the next page.
    :type next_token: str
    :param max_results: Valid Range: Minimum value of 1. Maximum value of 50.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_dicom_import_jobs(request: web.Request, datastore_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, job_status=None, next_token=None, max_results=None) -> web.Response:
    """list_dicom_import_jobs

    List import jobs created by this AWS account for a specific data store.

    :param datastore_id: The data store identifier.
    :type datastore_id: str
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
    :param job_status: The filters for listing import jobs based on status.
    :type job_status: str
    :param next_token: The pagination token used to request the list of import jobs on the next page.
    :type next_token: str
    :param max_results: The max results count. The upper bound is determined by load testing.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_image_set_versions(request: web.Request, datastore_id, image_set_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_image_set_versions

    List image set versions.

    :param datastore_id: The data store identifier.
    :type datastore_id: str
    :param image_set_id: The image set identifier.
    :type image_set_id: str
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
    :param next_token: The pagination token used to request the list of image set versions on the next page.
    :type next_token: str
    :param max_results: The max results count.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists all tags associated with a medical imaging resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the medical imaging resource to list tags for.
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


async def search_image_sets(request: web.Request, datastore_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_image_sets

    Search image sets based on defined input attributes.

    :param datastore_id: The identifier of the data store where the image sets reside.
    :type datastore_id: str
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
    :param max_results: The maximum number of results that can be returned in a search.
    :type max_results: int
    :param next_token: The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended.
    :type next_token: str

    """
    body = SearchImageSetsRequest.from_dict(body)
    return web.Response(status=200)


async def start_dicom_import_job(request: web.Request, datastore_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_dicom_import_job

    Start importing bulk data into an &lt;code&gt;ACTIVE&lt;/code&gt; data store. The import job imports DICOM P10 files found in the S3 prefix specified by the &lt;code&gt;inputS3Uri&lt;/code&gt; parameter. The import job stores processing results in the file specified by the &lt;code&gt;outputS3Uri&lt;/code&gt; parameter.

    :param datastore_id: The data store identifier.
    :type datastore_id: str
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
    body = StartDICOMImportJobRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds a user-specifed key and value tag to a medical imaging resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to.
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

    Removes tags from a medical imaging resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from.
    :type resource_arn: str
    :param tag_keys: The keys for the tags to be removed from the medical imaging resource.
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


async def update_image_set_metadata(request: web.Request, datastore_id, image_set_id, latest_version, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_image_set_metadata

    Update image set metadata attributes.

    :param datastore_id: The data store identifier.
    :type datastore_id: str
    :param image_set_id: The image set identifier.
    :type image_set_id: str
    :param latest_version: The latest image set version identifier.
    :type latest_version: str
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
    body = UpdateImageSetMetadataRequest.from_dict(body)
    return web.Response(status=200)
