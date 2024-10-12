# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_add_facet_to_object(client):
    """Test case for add_facet_to_object

    
    """
    body = {"SchemaFacet":{"FacetName":"","SchemaArn":""},"ObjectReference":{"Selector":""},"ObjectAttributeList":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/object/facets#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apply_schema(client):
    """Test case for apply_schema

    
    """
    body = {"PublishedSchemaArn":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/schema/apply#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attach_object(client):
    """Test case for attach_object

    
    """
    body = {"LinkName":"","ParentReference":{"Selector":""},"ChildReference":{"Selector":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/object/attach#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attach_policy(client):
    """Test case for attach_policy

    
    """
    body = {"ObjectReference":{"Selector":""},"PolicyReference":{"Selector":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/policy/attach#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attach_to_index(client):
    """Test case for attach_to_index

    
    """
    body = {"TargetReference":{"Selector":""},"IndexReference":{"Selector":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/index/attach#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attach_typed_link(client):
    """Test case for attach_typed_link

    
    """
    body = {"TargetObjectReference":{"Selector":""},"Attributes":"","TypedLinkFacet":{"TypedLinkName":"","SchemaArn":""},"SourceObjectReference":{"Selector":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/typedlink/attach#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_read(client):
    """Test case for batch_read

    
    """
    body = {"Operations":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'x_amz_consistency_level': 'x_amz_consistency_level_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/batchread#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_write(client):
    """Test case for batch_write

    
    """
    body = {"Operations":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/batchwrite#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_directory(client):
    """Test case for create_directory

    
    """
    body = {"Name":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/directory/create#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_facet(client):
    """Test case for create_facet

    
    """
    body = {"ObjectType":"","Attributes":"","Name":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/facet/create#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_index(client):
    """Test case for create_index

    
    """
    body = {"LinkName":"","ParentReference":{"Selector":""},"IsUnique":"","OrderedIndexedAttributeList":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/index#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_object(client):
    """Test case for create_object

    
    """
    body = {"LinkName":"","ParentReference":{"Selector":""},"SchemaFacets":"","ObjectAttributeList":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/object#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_schema(client):
    """Test case for create_schema

    
    """
    body = {"Name":""}
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
        path='/amazonclouddirectory/2017-01-11/schema/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_typed_link_facet(client):
    """Test case for create_typed_link_facet

    
    """
    body = {"Facet":{"IdentityAttributeOrder":"","Attributes":"","Name":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/typedlink/facet/create#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_directory(client):
    """Test case for delete_directory

    
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/directory#x-amz-data-partition',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_facet(client):
    """Test case for delete_facet

    
    """
    body = {"Name":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/facet/delete#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_object(client):
    """Test case for delete_object

    
    """
    body = {"ObjectReference":{"Selector":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/object/delete#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_schema(client):
    """Test case for delete_schema

    
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/schema#x-amz-data-partition',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_typed_link_facet(client):
    """Test case for delete_typed_link_facet

    
    """
    body = {"Name":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/typedlink/facet/delete#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detach_from_index(client):
    """Test case for detach_from_index

    
    """
    body = {"TargetReference":{"Selector":""},"IndexReference":{"Selector":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/index/detach#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detach_object(client):
    """Test case for detach_object

    
    """
    body = {"LinkName":"","ParentReference":{"Selector":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/object/detach#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detach_policy(client):
    """Test case for detach_policy

    
    """
    body = {"ObjectReference":{"Selector":""},"PolicyReference":{"Selector":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/policy/detach#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detach_typed_link(client):
    """Test case for detach_typed_link

    
    """
    body = {"TypedLinkSpecifier":{"TargetObjectReference":{"Selector":""},"IdentityAttributeValues":"","TypedLinkFacet":{"TypedLinkName":"","SchemaArn":""},"SourceObjectReference":{"Selector":""}}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/typedlink/detach#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_directory(client):
    """Test case for disable_directory

    
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/directory/disable#x-amz-data-partition',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_directory(client):
    """Test case for enable_directory

    
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/directory/enable#x-amz-data-partition',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_applied_schema_version(client):
    """Test case for get_applied_schema_version

    
    """
    body = {"SchemaArn":""}
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
        method='POST',
        path='/amazonclouddirectory/2017-01-11/schema/getappliedschema',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_directory(client):
    """Test case for get_directory

    
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/directory/get#x-amz-data-partition',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_facet(client):
    """Test case for get_facet

    
    """
    body = {"Name":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/facet#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_link_attributes(client):
    """Test case for get_link_attributes

    
    """
    body = {"ConsistencyLevel":"","AttributeNames":"","TypedLinkSpecifier":{"TargetObjectReference":{"Selector":""},"IdentityAttributeValues":"","TypedLinkFacet":{"TypedLinkName":"","SchemaArn":""},"SourceObjectReference":{"Selector":""}}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/typedlink/attributes/get#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_object_attributes(client):
    """Test case for get_object_attributes

    
    """
    body = {"SchemaFacet":{"FacetName":"","SchemaArn":""},"ObjectReference":{"Selector":""},"AttributeNames":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'x_amz_consistency_level': 'x_amz_consistency_level_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/object/attributes/get#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_object_information(client):
    """Test case for get_object_information

    
    """
    body = {"ObjectReference":{"Selector":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'x_amz_consistency_level': 'x_amz_consistency_level_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/object/information#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_schema_as_json(client):
    """Test case for get_schema_as_json

    
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/schema/json#x-amz-data-partition',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_typed_link_facet_information(client):
    """Test case for get_typed_link_facet_information

    
    """
    body = {"Name":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/typedlink/facet/get#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_applied_schema_arns(client):
    """Test case for list_applied_schema_arns

    
    """
    body = {"DirectoryArn":"","NextToken":"","MaxResults":"","SchemaArn":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        method='POST',
        path='/amazonclouddirectory/2017-01-11/schema/applied',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_attached_indices(client):
    """Test case for list_attached_indices

    
    """
    body = {"TargetReference":{"Selector":""},"NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'x_amz_consistency_level': 'x_amz_consistency_level_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/object/indices#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_development_schema_arns(client):
    """Test case for list_development_schema_arns

    
    """
    body = {"NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        method='POST',
        path='/amazonclouddirectory/2017-01-11/schema/development',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_directories(client):
    """Test case for list_directories

    
    """
    body = {"NextToken":"","MaxResults":"","state":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        method='POST',
        path='/amazonclouddirectory/2017-01-11/directory/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_facet_attributes(client):
    """Test case for list_facet_attributes

    
    """
    body = {"NextToken":"","MaxResults":"","Name":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/facet/attributes#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_facet_names(client):
    """Test case for list_facet_names

    
    """
    body = {"NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/facet/list#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_incoming_typed_links(client):
    """Test case for list_incoming_typed_links

    
    """
    body = {"ConsistencyLevel":"","NextToken":"","ObjectReference":{"Selector":""},"FilterAttributeRanges":"","MaxResults":"","FilterTypedLink":{"TypedLinkName":"","SchemaArn":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/typedlink/incoming#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_index(client):
    """Test case for list_index

    
    """
    body = {"RangesOnIndexedValues":"","NextToken":"","MaxResults":"","IndexReference":{"Selector":""}}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'x_amz_consistency_level': 'x_amz_consistency_level_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/index/targets#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_object_attributes(client):
    """Test case for list_object_attributes

    
    """
    body = {"NextToken":"","ObjectReference":{"Selector":""},"FacetFilter":{"FacetName":"","SchemaArn":""},"MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'x_amz_consistency_level': 'x_amz_consistency_level_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/object/attributes#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_object_children(client):
    """Test case for list_object_children

    
    """
    body = {"NextToken":"","ObjectReference":{"Selector":""},"MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'x_amz_consistency_level': 'x_amz_consistency_level_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/object/children#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_object_parent_paths(client):
    """Test case for list_object_parent_paths

    
    """
    body = {"NextToken":"","ObjectReference":{"Selector":""},"MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/object/parentpaths#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_object_parents(client):
    """Test case for list_object_parents

    
    """
    body = {"NextToken":"","ObjectReference":{"Selector":""},"MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'x_amz_consistency_level': 'x_amz_consistency_level_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/object/parent#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_object_policies(client):
    """Test case for list_object_policies

    
    """
    body = {"NextToken":"","ObjectReference":{"Selector":""},"MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'x_amz_consistency_level': 'x_amz_consistency_level_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/object/policy#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_outgoing_typed_links(client):
    """Test case for list_outgoing_typed_links

    
    """
    body = {"ConsistencyLevel":"","NextToken":"","ObjectReference":{"Selector":""},"FilterAttributeRanges":"","MaxResults":"","FilterTypedLink":{"TypedLinkName":"","SchemaArn":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/typedlink/outgoing#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_policy_attachments(client):
    """Test case for list_policy_attachments

    
    """
    body = {"NextToken":"","MaxResults":"","PolicyReference":{"Selector":""}}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'x_amz_consistency_level': 'x_amz_consistency_level_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/policy/attachment#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_published_schema_arns(client):
    """Test case for list_published_schema_arns

    
    """
    body = {"NextToken":"","MaxResults":"","SchemaArn":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        method='POST',
        path='/amazonclouddirectory/2017-01-11/schema/published',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    body = {"ResourceArn":"","NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        method='POST',
        path='/amazonclouddirectory/2017-01-11/tags',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_typed_link_facet_attributes(client):
    """Test case for list_typed_link_facet_attributes

    
    """
    body = {"NextToken":"","MaxResults":"","Name":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/typedlink/facet/attributes#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_typed_link_facet_names(client):
    """Test case for list_typed_link_facet_names

    
    """
    body = {"NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/typedlink/facet/list#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lookup_policy(client):
    """Test case for lookup_policy

    
    """
    body = {"NextToken":"","ObjectReference":{"Selector":""},"MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/policy/lookup#x-amz-data-partition',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_schema(client):
    """Test case for publish_schema

    
    """
    body = {"Version":"","MinorVersion":"","Name":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/schema/publish#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_schema_from_json(client):
    """Test case for put_schema_from_json

    
    """
    body = {"Document":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/schema/json#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_facet_from_object(client):
    """Test case for remove_facet_from_object

    
    """
    body = {"SchemaFacet":{"FacetName":"","SchemaArn":""},"ObjectReference":{"Selector":""}}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/object/facets/delete#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"ResourceArn":"","Tags":""}
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
        path='/amazonclouddirectory/2017-01-11/tags/add',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    body = {"ResourceArn":"","TagKeys":""}
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
        path='/amazonclouddirectory/2017-01-11/tags/remove',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_facet(client):
    """Test case for update_facet

    
    """
    body = {"ObjectType":"","AttributeUpdates":"","Name":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/facet#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_link_attributes(client):
    """Test case for update_link_attributes

    
    """
    body = {"TypedLinkSpecifier":{"TargetObjectReference":{"Selector":""},"IdentityAttributeValues":"","TypedLinkFacet":{"TypedLinkName":"","SchemaArn":""},"SourceObjectReference":{"Selector":""}},"AttributeUpdates":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/amazonclouddirectory/2017-01-11/typedlink/attributes/update#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_object_attributes(client):
    """Test case for update_object_attributes

    
    """
    body = {"ObjectReference":{"Selector":""},"AttributeUpdates":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/object/update#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_schema(client):
    """Test case for update_schema

    
    """
    body = {"Name":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/schema/update#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_typed_link_facet(client):
    """Test case for update_typed_link_facet

    
    """
    body = {"IdentityAttributeOrder":"","AttributeUpdates":"","Name":""}
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
        'x_amz_data_partition': 'x_amz_data_partition_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/amazonclouddirectory/2017-01-11/typedlink/facet#x-amz-data-partition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upgrade_applied_schema(client):
    """Test case for upgrade_applied_schema

    
    """
    body = {"DirectoryArn":"","PublishedSchemaArn":"","DryRun":""}
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
        path='/amazonclouddirectory/2017-01-11/schema/upgradeapplied',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upgrade_published_schema(client):
    """Test case for upgrade_published_schema

    
    """
    body = {"PublishedSchemaArn":"","DryRun":"","MinorVersion":"","DevelopmentSchemaArn":""}
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
        path='/amazonclouddirectory/2017-01-11/schema/upgradepublished',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

