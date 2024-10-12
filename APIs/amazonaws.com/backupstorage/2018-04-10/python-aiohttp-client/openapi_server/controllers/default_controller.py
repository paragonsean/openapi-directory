from typing import List, Dict
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
from openapi_server import util


async def delete_object(request: web.Request, job_id, object_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_object

    Delete Object from the incremental base Backup.

    :param job_id: Backup job Id for the in-progress backup.
    :type job_id: str
    :param object_name: The name of the Object.
    :type object_name: str
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


async def get_chunk(request: web.Request, job_id, chunk_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_chunk

    Gets the specified object&#39;s chunk.

    :param job_id: Storage job id
    :type job_id: str
    :param chunk_token: Chunk token
    :type chunk_token: str
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


async def get_object_metadata(request: web.Request, job_id, object_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_object_metadata

    Get metadata associated with an Object.

    :param job_id: Backup job id for the in-progress backup.
    :type job_id: str
    :param object_token: Object token.
    :type object_token: str
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


async def list_chunks(request: web.Request, job_id, object_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_chunks

    List chunks in a given Object

    :param job_id: Storage job id
    :type job_id: str
    :param object_token: Object token
    :type object_token: str
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
    :param max_results: Maximum number of chunks
    :type max_results: int
    :param next_token: Pagination token
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_objects(request: web.Request, job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, starting_object_name=None, starting_object_prefix=None, max_results=None, next_token=None, created_before=None, created_after=None, max_results2=None, next_token2=None) -> web.Response:
    """list_objects

    List all Objects in a given Backup.

    :param job_id: Storage job id
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
    :param starting_object_name: Optional, specifies the starting Object name to list from. Ignored if NextToken is not NULL
    :type starting_object_name: str
    :param starting_object_prefix: Optional, specifies the starting Object prefix to list from. Ignored if NextToken is not NULL
    :type starting_object_prefix: str
    :param max_results: Maximum objects count
    :type max_results: int
    :param next_token: Pagination token
    :type next_token: str
    :param created_before: (Optional) Created before filter
    :type created_before: str
    :param created_after: (Optional) Created after filter
    :type created_after: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    created_before = util.deserialize_datetime(created_before)
    created_after = util.deserialize_datetime(created_after)
    return web.Response(status=200)


async def notify_object_complete(request: web.Request, job_id, upload_id, checksum, checksum_algorithm, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, metadata_string=None, metadata_blob_length=None, metadata_checksum=None, metadata_checksum_algorithm=None) -> web.Response:
    """notify_object_complete

    Complete upload

    :param job_id: Backup job Id for the in-progress backup
    :type job_id: str
    :param upload_id: Upload Id for the in-progress upload
    :type upload_id: str
    :param checksum: Object checksum
    :type checksum: str
    :param checksum_algorithm: Checksum algorithm
    :type checksum_algorithm: str
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
    :param metadata_string: Optional metadata associated with an Object. Maximum string length is 256 bytes.
    :type metadata_string: str
    :param metadata_blob_length: The size of MetadataBlob.
    :type metadata_blob_length: int
    :param metadata_checksum: Checksum of MetadataBlob.
    :type metadata_checksum: str
    :param metadata_checksum_algorithm: Checksum algorithm.
    :type metadata_checksum_algorithm: str

    """
    body = NotifyObjectCompleteRequest.from_dict(body)
    return web.Response(status=200)


async def put_chunk(request: web.Request, job_id, upload_id, chunk_index, length, checksum, checksum_algorithm, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_chunk

    Upload chunk.

    :param job_id: Backup job Id for the in-progress backup.
    :type job_id: str
    :param upload_id: Upload Id for the in-progress upload.
    :type upload_id: str
    :param chunk_index: Describes this chunk&#39;s position relative to the other chunks
    :type chunk_index: int
    :param length: Data length
    :type length: int
    :param checksum: Data checksum
    :type checksum: str
    :param checksum_algorithm: Checksum algorithm
    :type checksum_algorithm: str
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
    body = PutChunkRequest.from_dict(body)
    return web.Response(status=200)


async def put_object(request: web.Request, job_id, object_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, metadata_string=None, length=None, checksum=None, checksum_algorithm=None, object_checksum=None, object_checksum_algorithm=None, throw_on_duplicate=None) -> web.Response:
    """put_object

    Upload object that can store object metadata String and data blob in single API call using inline chunk field.

    :param job_id: Backup job Id for the in-progress backup.
    :type job_id: str
    :param object_name: The name of the Object to be uploaded.
    :type object_name: str
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
    :param metadata_string: Store user defined metadata like backup checksum, disk ids, restore metadata etc.
    :type metadata_string: str
    :param length: Length of the inline chunk data.
    :type length: int
    :param checksum: Inline chunk checksum
    :type checksum: str
    :param checksum_algorithm: Inline chunk checksum algorithm
    :type checksum_algorithm: str
    :param object_checksum: object checksum
    :type object_checksum: str
    :param object_checksum_algorithm: object checksum algorithm
    :type object_checksum_algorithm: str
    :param throw_on_duplicate: Throw an exception if Object name is already exist.
    :type throw_on_duplicate: bool

    """
    body = PutObjectRequest.from_dict(body)
    return web.Response(status=200)


async def start_object(request: web.Request, job_id, object_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_object

    Start upload containing one or many chunks.

    :param job_id: Backup job Id for the in-progress backup
    :type job_id: str
    :param object_name: Name for the object.
    :type object_name: str
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
    body = StartObjectRequest.from_dict(body)
    return web.Response(status=200)
