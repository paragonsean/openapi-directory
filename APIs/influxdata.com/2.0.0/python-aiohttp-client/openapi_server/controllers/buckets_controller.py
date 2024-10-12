from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_resource_member_request_body import AddResourceMemberRequestBody
from openapi_server.models.bucket import Bucket
from openapi_server.models.buckets import Buckets
from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.patch_bucket_request import PatchBucketRequest
from openapi_server.models.post_bucket_request import PostBucketRequest
from openapi_server.models.resource_member import ResourceMember
from openapi_server.models.resource_members import ResourceMembers
from openapi_server.models.resource_owner import ResourceOwner
from openapi_server.models.resource_owners import ResourceOwners
from openapi_server import util


async def delete_buckets_id(request: web.Request, bucket_id, zap_trace_span=None) -> web.Response:
    """Delete a bucket

    

    :param bucket_id: The ID of the bucket to delete.
    :type bucket_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_buckets_id_labels_id(request: web.Request, bucket_id, label_id, zap_trace_span=None) -> web.Response:
    """Delete a label from a bucket

    

    :param bucket_id: The bucket ID.
    :type bucket_id: str
    :param label_id: The ID of the label to delete.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_buckets_id_members_id(request: web.Request, user_id, bucket_id, zap_trace_span=None) -> web.Response:
    """Remove a member from a bucket

    

    :param user_id: The ID of the member to remove.
    :type user_id: str
    :param bucket_id: The bucket ID.
    :type bucket_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_buckets_id_owners_id(request: web.Request, user_id, bucket_id, zap_trace_span=None) -> web.Response:
    """Remove an owner from a bucket

    

    :param user_id: The ID of the owner to remove.
    :type user_id: str
    :param bucket_id: The bucket ID.
    :type bucket_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_buckets(request: web.Request, zap_trace_span=None, offset=None, limit=None, after=None, org=None, org_id=None, name=None, id=None) -> web.Response:
    """List all buckets

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int
    :param after: The last resource ID from which to seek from (but not including). This is to be used instead of &#x60;offset&#x60;. 
    :type after: str
    :param org: The name of the organization.
    :type org: str
    :param org_id: The organization ID.
    :type org_id: str
    :param name: Only returns buckets with a specific name.
    :type name: str
    :param id: Only returns buckets with a specific ID.
    :type id: str

    """
    return web.Response(status=200)


async def get_buckets_id(request: web.Request, bucket_id, zap_trace_span=None) -> web.Response:
    """Retrieve a bucket

    

    :param bucket_id: The bucket ID.
    :type bucket_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_buckets_id_labels(request: web.Request, bucket_id, zap_trace_span=None) -> web.Response:
    """List all labels for a bucket

    

    :param bucket_id: The bucket ID.
    :type bucket_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_buckets_id_members(request: web.Request, bucket_id, zap_trace_span=None) -> web.Response:
    """List all users with member privileges for a bucket

    

    :param bucket_id: The bucket ID.
    :type bucket_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_buckets_id_owners(request: web.Request, bucket_id, zap_trace_span=None) -> web.Response:
    """List all owners of a bucket

    

    :param bucket_id: The bucket ID.
    :type bucket_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_sources_id_buckets_0(request: web.Request, source_id, zap_trace_span=None, org=None) -> web.Response:
    """Get buckets in a source

    

    :param source_id: The source ID.
    :type source_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param org: The name of the organization.
    :type org: str

    """
    return web.Response(status=200)


async def patch_buckets_id(request: web.Request, bucket_id, body, zap_trace_span=None) -> web.Response:
    """Update a bucket

    

    :param bucket_id: The bucket ID.
    :type bucket_id: str
    :param body: Bucket update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = PatchBucketRequest.from_dict(body)
    return web.Response(status=200)


async def post_buckets(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Create a bucket

    

    :param body: Bucket to create
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = PostBucketRequest.from_dict(body)
    return web.Response(status=200)


async def post_buckets_id_labels(request: web.Request, bucket_id, body, zap_trace_span=None) -> web.Response:
    """Add a label to a bucket

    

    :param bucket_id: The bucket ID.
    :type bucket_id: str
    :param body: Label to add
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = LabelMapping.from_dict(body)
    return web.Response(status=200)


async def post_buckets_id_members(request: web.Request, bucket_id, body, zap_trace_span=None) -> web.Response:
    """Add a member to a bucket

    

    :param bucket_id: The bucket ID.
    :type bucket_id: str
    :param body: User to add as member
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)


async def post_buckets_id_owners(request: web.Request, bucket_id, body, zap_trace_span=None) -> web.Response:
    """Add an owner to a bucket

    

    :param bucket_id: The bucket ID.
    :type bucket_id: str
    :param body: User to add as owner
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)
