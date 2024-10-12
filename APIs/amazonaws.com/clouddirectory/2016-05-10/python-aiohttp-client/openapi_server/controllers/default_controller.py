from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_denied_exception import AccessDeniedException
from openapi_server.models.add_facet_to_object_request import AddFacetToObjectRequest
from openapi_server.models.apply_schema_request import ApplySchemaRequest
from openapi_server.models.apply_schema_response import ApplySchemaResponse
from openapi_server.models.attach_object_request import AttachObjectRequest
from openapi_server.models.attach_object_response import AttachObjectResponse
from openapi_server.models.attach_policy_request import AttachPolicyRequest
from openapi_server.models.attach_to_index_request import AttachToIndexRequest
from openapi_server.models.attach_to_index_response import AttachToIndexResponse
from openapi_server.models.attach_typed_link_request import AttachTypedLinkRequest
from openapi_server.models.attach_typed_link_response import AttachTypedLinkResponse
from openapi_server.models.batch_read_request import BatchReadRequest
from openapi_server.models.batch_read_response import BatchReadResponse
from openapi_server.models.batch_write_exception import BatchWriteException
from openapi_server.models.batch_write_request import BatchWriteRequest
from openapi_server.models.batch_write_response import BatchWriteResponse
from openapi_server.models.cannot_list_parent_of_root_exception import CannotListParentOfRootException
from openapi_server.models.create_directory_request import CreateDirectoryRequest
from openapi_server.models.create_directory_response import CreateDirectoryResponse
from openapi_server.models.create_facet_request import CreateFacetRequest
from openapi_server.models.create_index_request import CreateIndexRequest
from openapi_server.models.create_index_response import CreateIndexResponse
from openapi_server.models.create_object_request import CreateObjectRequest
from openapi_server.models.create_object_response import CreateObjectResponse
from openapi_server.models.create_schema_request import CreateSchemaRequest
from openapi_server.models.create_schema_response import CreateSchemaResponse
from openapi_server.models.create_typed_link_facet_request import CreateTypedLinkFacetRequest
from openapi_server.models.delete_directory_response import DeleteDirectoryResponse
from openapi_server.models.delete_facet_request import DeleteFacetRequest
from openapi_server.models.delete_object_request import DeleteObjectRequest
from openapi_server.models.delete_schema_response import DeleteSchemaResponse
from openapi_server.models.delete_typed_link_facet_request import DeleteTypedLinkFacetRequest
from openapi_server.models.detach_from_index_response import DetachFromIndexResponse
from openapi_server.models.detach_object_request import DetachObjectRequest
from openapi_server.models.detach_object_response import DetachObjectResponse
from openapi_server.models.detach_typed_link_request import DetachTypedLinkRequest
from openapi_server.models.directory_already_exists_exception import DirectoryAlreadyExistsException
from openapi_server.models.directory_deleted_exception import DirectoryDeletedException
from openapi_server.models.directory_not_disabled_exception import DirectoryNotDisabledException
from openapi_server.models.directory_not_enabled_exception import DirectoryNotEnabledException
from openapi_server.models.disable_directory_response import DisableDirectoryResponse
from openapi_server.models.enable_directory_response import EnableDirectoryResponse
from openapi_server.models.facet_already_exists_exception import FacetAlreadyExistsException
from openapi_server.models.facet_in_use_exception import FacetInUseException
from openapi_server.models.facet_not_found_exception import FacetNotFoundException
from openapi_server.models.facet_validation_exception import FacetValidationException
from openapi_server.models.get_applied_schema_version_request import GetAppliedSchemaVersionRequest
from openapi_server.models.get_applied_schema_version_response import GetAppliedSchemaVersionResponse
from openapi_server.models.get_directory_response import GetDirectoryResponse
from openapi_server.models.get_facet_request import GetFacetRequest
from openapi_server.models.get_facet_response import GetFacetResponse
from openapi_server.models.get_link_attributes_request import GetLinkAttributesRequest
from openapi_server.models.get_link_attributes_response import GetLinkAttributesResponse
from openapi_server.models.get_object_attributes_request import GetObjectAttributesRequest
from openapi_server.models.get_object_attributes_response import GetObjectAttributesResponse
from openapi_server.models.get_object_information_response import GetObjectInformationResponse
from openapi_server.models.get_schema_as_json_response import GetSchemaAsJsonResponse
from openapi_server.models.get_typed_link_facet_information_response import GetTypedLinkFacetInformationResponse
from openapi_server.models.incompatible_schema_exception import IncompatibleSchemaException
from openapi_server.models.indexed_attribute_missing_exception import IndexedAttributeMissingException
from openapi_server.models.internal_service_exception import InternalServiceException
from openapi_server.models.invalid_arn_exception import InvalidArnException
from openapi_server.models.invalid_attachment_exception import InvalidAttachmentException
from openapi_server.models.invalid_facet_update_exception import InvalidFacetUpdateException
from openapi_server.models.invalid_next_token_exception import InvalidNextTokenException
from openapi_server.models.invalid_rule_exception import InvalidRuleException
from openapi_server.models.invalid_schema_doc_exception import InvalidSchemaDocException
from openapi_server.models.invalid_tagging_request_exception import InvalidTaggingRequestException
from openapi_server.models.limit_exceeded_exception import LimitExceededException
from openapi_server.models.link_name_already_in_use_exception import LinkNameAlreadyInUseException
from openapi_server.models.list_applied_schema_arns_request import ListAppliedSchemaArnsRequest
from openapi_server.models.list_applied_schema_arns_response import ListAppliedSchemaArnsResponse
from openapi_server.models.list_attached_indices_request import ListAttachedIndicesRequest
from openapi_server.models.list_attached_indices_response import ListAttachedIndicesResponse
from openapi_server.models.list_development_schema_arns_request import ListDevelopmentSchemaArnsRequest
from openapi_server.models.list_development_schema_arns_response import ListDevelopmentSchemaArnsResponse
from openapi_server.models.list_directories_request import ListDirectoriesRequest
from openapi_server.models.list_directories_response import ListDirectoriesResponse
from openapi_server.models.list_facet_attributes_request import ListFacetAttributesRequest
from openapi_server.models.list_facet_attributes_response import ListFacetAttributesResponse
from openapi_server.models.list_facet_names_response import ListFacetNamesResponse
from openapi_server.models.list_incoming_typed_links_request import ListIncomingTypedLinksRequest
from openapi_server.models.list_incoming_typed_links_response import ListIncomingTypedLinksResponse
from openapi_server.models.list_index_request import ListIndexRequest
from openapi_server.models.list_index_response import ListIndexResponse
from openapi_server.models.list_object_attributes_request import ListObjectAttributesRequest
from openapi_server.models.list_object_attributes_response import ListObjectAttributesResponse
from openapi_server.models.list_object_children_request import ListObjectChildrenRequest
from openapi_server.models.list_object_children_response import ListObjectChildrenResponse
from openapi_server.models.list_object_parent_paths_response import ListObjectParentPathsResponse
from openapi_server.models.list_object_parents_response import ListObjectParentsResponse
from openapi_server.models.list_object_policies_response import ListObjectPoliciesResponse
from openapi_server.models.list_outgoing_typed_links_response import ListOutgoingTypedLinksResponse
from openapi_server.models.list_policy_attachments_request import ListPolicyAttachmentsRequest
from openapi_server.models.list_policy_attachments_response import ListPolicyAttachmentsResponse
from openapi_server.models.list_published_schema_arns_request import ListPublishedSchemaArnsRequest
from openapi_server.models.list_published_schema_arns_response import ListPublishedSchemaArnsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_typed_link_facet_attributes_request import ListTypedLinkFacetAttributesRequest
from openapi_server.models.list_typed_link_facet_attributes_response import ListTypedLinkFacetAttributesResponse
from openapi_server.models.list_typed_link_facet_names_response import ListTypedLinkFacetNamesResponse
from openapi_server.models.lookup_policy_request import LookupPolicyRequest
from openapi_server.models.lookup_policy_response import LookupPolicyResponse
from openapi_server.models.not_index_exception import NotIndexException
from openapi_server.models.not_node_exception import NotNodeException
from openapi_server.models.not_policy_exception import NotPolicyException
from openapi_server.models.object_already_detached_exception import ObjectAlreadyDetachedException
from openapi_server.models.object_not_detached_exception import ObjectNotDetachedException
from openapi_server.models.publish_schema_request import PublishSchemaRequest
from openapi_server.models.publish_schema_response import PublishSchemaResponse
from openapi_server.models.put_schema_from_json_request import PutSchemaFromJsonRequest
from openapi_server.models.put_schema_from_json_response import PutSchemaFromJsonResponse
from openapi_server.models.remove_facet_from_object_request import RemoveFacetFromObjectRequest
from openapi_server.models.resource_not_found_exception import ResourceNotFoundException
from openapi_server.models.retryable_conflict_exception import RetryableConflictException
from openapi_server.models.schema_already_exists_exception import SchemaAlreadyExistsException
from openapi_server.models.schema_already_published_exception import SchemaAlreadyPublishedException
from openapi_server.models.still_contains_links_exception import StillContainsLinksException
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.unsupported_index_type_exception import UnsupportedIndexTypeException
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_facet_request import UpdateFacetRequest
from openapi_server.models.update_link_attributes_request import UpdateLinkAttributesRequest
from openapi_server.models.update_object_attributes_request import UpdateObjectAttributesRequest
from openapi_server.models.update_object_attributes_response import UpdateObjectAttributesResponse
from openapi_server.models.update_schema_request import UpdateSchemaRequest
from openapi_server.models.update_schema_response import UpdateSchemaResponse
from openapi_server.models.update_typed_link_facet_request import UpdateTypedLinkFacetRequest
from openapi_server.models.upgrade_applied_schema_request import UpgradeAppliedSchemaRequest
from openapi_server.models.upgrade_applied_schema_response import UpgradeAppliedSchemaResponse
from openapi_server.models.upgrade_published_schema_request import UpgradePublishedSchemaRequest
from openapi_server.models.upgrade_published_schema_response import UpgradePublishedSchemaResponse
from openapi_server.models.validation_exception import ValidationException
from openapi_server import util


async def add_facet_to_object(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_facet_to_object

    Adds a new &lt;a&gt;Facet&lt;/a&gt; to an object. An object can have more than one facet applied on it.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = AddFacetToObjectRequest.from_dict(body)
    return web.Response(status=200)


async def apply_schema(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """apply_schema

    Copies the input published schema, at the specified version, into the &lt;a&gt;Directory&lt;/a&gt; with the same name and version as that of the published schema.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; into which the schema is copied. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = ApplySchemaRequest.from_dict(body)
    return web.Response(status=200)


async def attach_object(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """attach_object

    &lt;p&gt;Attaches an existing object to another object. An object can be accessed in two ways:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Using the path&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Using &lt;code&gt;ObjectIdentifier&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

    :param x_amz_data_partition: Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where both objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = AttachObjectRequest.from_dict(body)
    return web.Response(status=200)


async def attach_policy(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """attach_policy

    Attaches a policy object to a regular object. An object can have a limited number of attached policies.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where both objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = AttachPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def attach_to_index(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """attach_to_index

    Attaches the specified object to the specified index.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) of the directory where the object and index exist.
    :type x_amz_data_partition: str
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
    body = AttachToIndexRequest.from_dict(body)
    return web.Response(status=200)


async def attach_typed_link(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """attach_typed_link

    Attaches a typed link to a specified source and target object. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) of the directory where you want to attach the typed link.
    :type x_amz_data_partition: str
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
    body = AttachTypedLinkRequest.from_dict(body)
    return web.Response(status=200)


async def batch_read(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_consistency_level=None) -> web.Response:
    """batch_read

    Performs all the read operations in a batch. 

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    :param x_amz_consistency_level: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    :type x_amz_consistency_level: str

    """
    body = BatchReadRequest.from_dict(body)
    return web.Response(status=200)


async def batch_write(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_write

    Performs all the write operations in a batch. Either all the operations succeed or none.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = BatchWriteRequest.from_dict(body)
    return web.Response(status=200)


async def create_directory(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_directory

    Creates a &lt;a&gt;Directory&lt;/a&gt; by copying the published schema into the directory. A directory cannot be created without a schema.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) of the published schema that will be copied into the data &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = CreateDirectoryRequest.from_dict(body)
    return web.Response(status=200)


async def create_facet(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_facet

    Creates a new &lt;a&gt;Facet&lt;/a&gt; in a schema. Facet creation is allowed only in development or applied schemas.

    :param x_amz_data_partition: The schema ARN in which the new &lt;a&gt;Facet&lt;/a&gt; will be created. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = CreateFacetRequest.from_dict(body)
    return web.Response(status=200)


async def create_index(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_index

    Creates an index object. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_indexing.html\&quot;&gt;Indexing&lt;/a&gt; for more information.

    :param x_amz_data_partition: The ARN of the directory where the index should be created.
    :type x_amz_data_partition: str
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
    body = CreateIndexRequest.from_dict(body)
    return web.Response(status=200)


async def create_object(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_object

    Creates an object in a &lt;a&gt;Directory&lt;/a&gt;. Additionally attaches the object to a parent, if a parent reference and &lt;code&gt;LinkName&lt;/code&gt; is specified. An object is simply a collection of &lt;a&gt;Facet&lt;/a&gt; attributes. You can also use this API call to create a policy object, if the facet from which you create the object is a policy facet. 

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; in which the object will be created. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = CreateObjectRequest.from_dict(body)
    return web.Response(status=200)


async def create_schema(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_schema

    &lt;p&gt;Creates a new schema in a development state. A schema can exist in three phases:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Development:&lt;/i&gt; This is a mutable phase of the schema. All new schemas are in the development phase. Once the schema is finalized, it can be published.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Published:&lt;/i&gt; Published schemas are immutable and have a version associated with them.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Applied:&lt;/i&gt; Applied schemas are mutable in a way that allows you to add new schema facets. You can also add new, nonrequired attributes to existing schema facets. You can apply only published schemas to directories. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateSchemaRequest.from_dict(body)
    return web.Response(status=200)


async def create_typed_link_facet(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_typed_link_facet

    Creates a &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = CreateTypedLinkFacetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_directory(request: web.Request, x_amz_data_partition, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_directory

    Deletes a directory. Only disabled directories can be deleted. A deleted directory cannot be undone. Exercise extreme caution when deleting directories.

    :param x_amz_data_partition: The ARN of the directory to delete.
    :type x_amz_data_partition: str
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


async def delete_facet(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_facet

    Deletes a given &lt;a&gt;Facet&lt;/a&gt;. All attributes and &lt;a&gt;Rule&lt;/a&gt;s that are associated with the facet will be deleted. Only development schema facets are allowed deletion.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Facet&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = DeleteFacetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_object(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_object

    Deletes an object and its associated attributes. Only objects with no children and no parents can be deleted.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = DeleteObjectRequest.from_dict(body)
    return web.Response(status=200)


async def delete_schema(request: web.Request, x_amz_data_partition, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_schema

    Deletes a given schema. Schemas in a development and published state can only be deleted. 

    :param x_amz_data_partition: The Amazon Resource Name (ARN) of the development schema. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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


async def delete_typed_link_facet(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_typed_link_facet

    Deletes a &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = DeleteTypedLinkFacetRequest.from_dict(body)
    return web.Response(status=200)


async def detach_from_index(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """detach_from_index

    Detaches the specified object from the specified index.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) of the directory the index and object exist in.
    :type x_amz_data_partition: str
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
    body = AttachToIndexRequest.from_dict(body)
    return web.Response(status=200)


async def detach_object(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """detach_object

    Detaches a given object from the parent object. The object that is to be detached from the parent is specified by the link name.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = DetachObjectRequest.from_dict(body)
    return web.Response(status=200)


async def detach_policy(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """detach_policy

    Detaches a policy from an object.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where both objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = AttachPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def detach_typed_link(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """detach_typed_link

    Detaches a typed link from a specified source and target object. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) of the directory where you want to detach the typed link.
    :type x_amz_data_partition: str
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
    body = DetachTypedLinkRequest.from_dict(body)
    return web.Response(status=200)


async def disable_directory(request: web.Request, x_amz_data_partition, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disable_directory

    Disables the specified directory. Disabled directories cannot be read or written to. Only enabled directories can be disabled. Disabled directories may be reenabled.

    :param x_amz_data_partition: The ARN of the directory to disable.
    :type x_amz_data_partition: str
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


async def enable_directory(request: web.Request, x_amz_data_partition, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_directory

    Enables the specified directory. Only disabled directories can be enabled. Once enabled, the directory can then be read and written to.

    :param x_amz_data_partition: The ARN of the directory to enable.
    :type x_amz_data_partition: str
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


async def get_applied_schema_version(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_applied_schema_version

    Returns current applied schema version ARN, including the minor version in use.

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
    body = GetAppliedSchemaVersionRequest.from_dict(body)
    return web.Response(status=200)


async def get_directory(request: web.Request, x_amz_data_partition, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_directory

    Retrieves metadata about a directory.

    :param x_amz_data_partition: The ARN of the directory.
    :type x_amz_data_partition: str
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


async def get_facet(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_facet

    Gets details of the &lt;a&gt;Facet&lt;/a&gt;, such as facet name, attributes, &lt;a&gt;Rule&lt;/a&gt;s, or &lt;code&gt;ObjectType&lt;/code&gt;. You can call this on all kinds of schema facets -- published, development, or applied.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Facet&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = GetFacetRequest.from_dict(body)
    return web.Response(status=200)


async def get_link_attributes(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_link_attributes

    Retrieves attributes that are associated with a typed link.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the Directory where the typed link resides. For more information, see &lt;a&gt;arns&lt;/a&gt; or &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = GetLinkAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def get_object_attributes(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_consistency_level=None) -> web.Response:
    """get_object_attributes

    Retrieves attributes within a facet that are associated with an object.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides.
    :type x_amz_data_partition: str
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
    :param x_amz_consistency_level: The consistency level at which to retrieve the attributes on an object.
    :type x_amz_consistency_level: str

    """
    body = GetObjectAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def get_object_information(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_consistency_level=None) -> web.Response:
    """get_object_information

    Retrieves metadata about an object.

    :param x_amz_data_partition: The ARN of the directory being retrieved.
    :type x_amz_data_partition: str
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
    :param x_amz_consistency_level: The consistency level at which to retrieve the object information.
    :type x_amz_consistency_level: str

    """
    body = DeleteObjectRequest.from_dict(body)
    return web.Response(status=200)


async def get_schema_as_json(request: web.Request, x_amz_data_partition, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_schema_as_json

    Retrieves a JSON representation of the schema. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_schemas.html#jsonformat\&quot;&gt;JSON Schema Format&lt;/a&gt; for more information.

    :param x_amz_data_partition: The ARN of the schema to retrieve.
    :type x_amz_data_partition: str
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


async def get_typed_link_facet_information(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_typed_link_facet_information

    Returns the identity attribute order for a specific &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = DeleteTypedLinkFacetRequest.from_dict(body)
    return web.Response(status=200)


async def list_applied_schema_arns(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_applied_schema_arns

    Lists schema major versions applied to a directory. If &lt;code&gt;SchemaArn&lt;/code&gt; is provided, lists the minor version.

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAppliedSchemaArnsRequest.from_dict(body)
    return web.Response(status=200)


async def list_attached_indices(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_consistency_level=None, max_results=None, next_token=None) -> web.Response:
    """list_attached_indices

    Lists indices attached to the specified object.

    :param x_amz_data_partition: The ARN of the directory.
    :type x_amz_data_partition: str
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
    :param x_amz_consistency_level: The consistency level to use for this operation.
    :type x_amz_consistency_level: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAttachedIndicesRequest.from_dict(body)
    return web.Response(status=200)


async def list_development_schema_arns(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_development_schema_arns

    Retrieves each Amazon Resource Name (ARN) of schemas in the development state.

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListDevelopmentSchemaArnsRequest.from_dict(body)
    return web.Response(status=200)


async def list_directories(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_directories

    Lists directories created within an account.

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListDirectoriesRequest.from_dict(body)
    return web.Response(status=200)


async def list_facet_attributes(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_facet_attributes

    Retrieves attributes attached to the facet.

    :param x_amz_data_partition: The ARN of the schema where the facet resides.
    :type x_amz_data_partition: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListFacetAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def list_facet_names(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_facet_names

    Retrieves the names of facets that exist in a schema.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) to retrieve facet names from.
    :type x_amz_data_partition: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListDevelopmentSchemaArnsRequest.from_dict(body)
    return web.Response(status=200)


async def list_incoming_typed_links(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_incoming_typed_links

    Returns a paginated list of all the incoming &lt;a&gt;TypedLinkSpecifier&lt;/a&gt; information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
    :type x_amz_data_partition: str
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
    body = ListIncomingTypedLinksRequest.from_dict(body)
    return web.Response(status=200)


async def list_index(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_consistency_level=None, max_results=None, next_token=None) -> web.Response:
    """list_index

    Lists objects attached to the specified index.

    :param x_amz_data_partition: The ARN of the directory that the index exists in.
    :type x_amz_data_partition: str
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
    :param x_amz_consistency_level: The consistency level to execute the request at.
    :type x_amz_consistency_level: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListIndexRequest.from_dict(body)
    return web.Response(status=200)


async def list_object_attributes(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_consistency_level=None, max_results=None, next_token=None) -> web.Response:
    """list_object_attributes

    Lists all attributes that are associated with an object. 

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    :param x_amz_consistency_level: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    :type x_amz_consistency_level: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListObjectAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def list_object_children(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_consistency_level=None, max_results=None, next_token=None) -> web.Response:
    """list_object_children

    Returns a paginated list of child objects that are associated with a given object.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    :param x_amz_consistency_level: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    :type x_amz_consistency_level: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListObjectChildrenRequest.from_dict(body)
    return web.Response(status=200)


async def list_object_parent_paths(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_object_parent_paths

    &lt;p&gt;Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#dirstructure\&quot;&gt;Directory Structure&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Use this API to evaluate all parents for an object. The call returns all objects from the root of the directory up to the requested object. The API returns the number of paths based on user-defined &lt;code&gt;MaxResults&lt;/code&gt;, in case there are multiple paths to the parent. The order of the paths and nodes returned is consistent among multiple API calls unless the objects are deleted or moved. Paths not leading to the directory root are ignored from the target object.&lt;/p&gt;

    :param x_amz_data_partition: The ARN of the directory to which the parent path applies.
    :type x_amz_data_partition: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListObjectChildrenRequest.from_dict(body)
    return web.Response(status=200)


async def list_object_parents(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_consistency_level=None, max_results=None, next_token=None) -> web.Response:
    """list_object_parents

    Lists parent objects that are associated with a given object in pagination fashion.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    :param x_amz_consistency_level: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    :type x_amz_consistency_level: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListObjectChildrenRequest.from_dict(body)
    return web.Response(status=200)


async def list_object_policies(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_consistency_level=None, max_results=None, next_token=None) -> web.Response:
    """list_object_policies

    Returns policies attached to an object in pagination fashion.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    :param x_amz_consistency_level: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    :type x_amz_consistency_level: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListObjectChildrenRequest.from_dict(body)
    return web.Response(status=200)


async def list_outgoing_typed_links(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_outgoing_typed_links

    Returns a paginated list of all the outgoing &lt;a&gt;TypedLinkSpecifier&lt;/a&gt; information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) of the directory where you want to list the typed links.
    :type x_amz_data_partition: str
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
    body = ListIncomingTypedLinksRequest.from_dict(body)
    return web.Response(status=200)


async def list_policy_attachments(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_consistency_level=None, max_results=None, next_token=None) -> web.Response:
    """list_policy_attachments

    Returns all of the &lt;code&gt;ObjectIdentifiers&lt;/code&gt; to which a given policy is attached.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where objects reside. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    :param x_amz_consistency_level: Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.
    :type x_amz_consistency_level: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListPolicyAttachmentsRequest.from_dict(body)
    return web.Response(status=200)


async def list_published_schema_arns(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_published_schema_arns

    Lists the major version families of each published schema. If a major version ARN is provided as &lt;code&gt;SchemaArn&lt;/code&gt;, the minor version revisions in that family are listed instead.

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListPublishedSchemaArnsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tags_for_resource

    Returns tags for a resource. Tagging is currently supported only for directories with a limit of 50 tags per directory. All 50 tags are returned for a given directory with this API call.

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def list_typed_link_facet_attributes(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_typed_link_facet_attributes

    Returns a paginated list of all attribute definitions for a particular &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTypedLinkFacetAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def list_typed_link_facet_names(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_typed_link_facet_names

    Returns a paginated list of &lt;code&gt;TypedLink&lt;/code&gt; facet names for a particular schema. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListDevelopmentSchemaArnsRequest.from_dict(body)
    return web.Response(status=200)


async def lookup_policy(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """lookup_policy

    Lists all policies from the root of the &lt;a&gt;Directory&lt;/a&gt; to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don&#39;t have the policies attached, it returns the &lt;code&gt;ObjectIdentifier&lt;/code&gt; for such objects. If policies are present, it returns &lt;code&gt;ObjectIdentifier&lt;/code&gt;, &lt;code&gt;policyId&lt;/code&gt;, and &lt;code&gt;policyType&lt;/code&gt;. Paths that don&#39;t lead to the root from the target object are ignored. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#policies\&quot;&gt;Policies&lt;/a&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = LookupPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def publish_schema(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """publish_schema

    Publishes a development schema with a major version and a recommended minor version.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the development schema. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = PublishSchemaRequest.from_dict(body)
    return web.Response(status=200)


async def put_schema_from_json(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_schema_from_json

    Allows a schema to be updated using JSON upload. Only available for development schemas. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_schemas.html#jsonformat\&quot;&gt;JSON Schema Format&lt;/a&gt; for more information.

    :param x_amz_data_partition: The ARN of the schema to update.
    :type x_amz_data_partition: str
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
    body = PutSchemaFromJsonRequest.from_dict(body)
    return web.Response(status=200)


async def remove_facet_from_object(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_facet_from_object

    Removes the specified facet from the specified object.

    :param x_amz_data_partition: The ARN of the directory in which the object resides.
    :type x_amz_data_partition: str
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
    body = RemoveFacetFromObjectRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    An API operation for adding tags to a resource.

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


async def untag_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    An API operation for removing tags from a resource.

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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_facet(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_facet

    &lt;p&gt;Does the following:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Adds new &lt;code&gt;Attributes&lt;/code&gt;, &lt;code&gt;Rules&lt;/code&gt;, or &lt;code&gt;ObjectTypes&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Updates existing &lt;code&gt;Attributes&lt;/code&gt;, &lt;code&gt;Rules&lt;/code&gt;, or &lt;code&gt;ObjectTypes&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deletes existing &lt;code&gt;Attributes&lt;/code&gt;, &lt;code&gt;Rules&lt;/code&gt;, or &lt;code&gt;ObjectTypes&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Facet&lt;/a&gt;. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = UpdateFacetRequest.from_dict(body)
    return web.Response(status=200)


async def update_link_attributes(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_link_attributes

    Updates a given typed link’s attributes. Attributes to be updated must not contribute to the typed link’s identity, as defined by its &lt;code&gt;IdentityAttributeOrder&lt;/code&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the Directory where the updated typed link resides. For more information, see &lt;a&gt;arns&lt;/a&gt; or &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = UpdateLinkAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def update_object_attributes(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_object_attributes

    Updates a given object&#39;s attributes.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the &lt;a&gt;Directory&lt;/a&gt; where the object resides. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = UpdateObjectAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def update_schema(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_schema

    Updates the schema name with a new name. Only development schema names can be updated.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) of the development schema. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = UpdateSchemaRequest.from_dict(body)
    return web.Response(status=200)


async def update_typed_link_facet(request: web.Request, x_amz_data_partition, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_typed_link_facet

    Updates a &lt;a&gt;TypedLinkFacet&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;.

    :param x_amz_data_partition: The Amazon Resource Name (ARN) that is associated with the schema. For more information, see &lt;a&gt;arns&lt;/a&gt;.
    :type x_amz_data_partition: str
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
    body = UpdateTypedLinkFacetRequest.from_dict(body)
    return web.Response(status=200)


async def upgrade_applied_schema(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """upgrade_applied_schema

    Upgrades a single directory in-place using the &lt;code&gt;PublishedSchemaArn&lt;/code&gt; with schema updates found in &lt;code&gt;MinorVersion&lt;/code&gt;. Backwards-compatible minor version upgrades are instantaneously available for readers on all objects in the directory. Note: This is a synchronous API call and upgrades only one schema on a given directory per call. To upgrade multiple directories from one schema, you would need to call this API on each directory.

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
    body = UpgradeAppliedSchemaRequest.from_dict(body)
    return web.Response(status=200)


async def upgrade_published_schema(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """upgrade_published_schema

    Upgrades a published schema under a new minor version revision using the current contents of &lt;code&gt;DevelopmentSchemaArn&lt;/code&gt;.

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
    body = UpgradePublishedSchemaRequest.from_dict(body)
    return web.Response(status=200)
