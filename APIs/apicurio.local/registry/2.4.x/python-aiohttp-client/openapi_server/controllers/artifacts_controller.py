from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact_content import ArtifactContent
from openapi_server.models.artifact_meta_data import ArtifactMetaData
from openapi_server.models.artifact_reference import ArtifactReference
from openapi_server.models.artifact_search_results import ArtifactSearchResults
from openapi_server.models.error import Error
from openapi_server.models.if_exists import IfExists
from openapi_server.models.rule_violation_error import RuleViolationError
from openapi_server.models.sort_by import SortBy
from openapi_server.models.sort_order import SortOrder
from openapi_server.models.update_state import UpdateState
from openapi_server import util


async def create_artifact(request: web.Request, group_id, body, x_registry_artifact_type=None, x_registry_artifact_id=None, x_registry_version=None, if_exists=None, canonical=None, x_registry_description=None, x_registry_description_encoded=None, x_registry_name=None, x_registry_name_encoded=None, x_registry_content_hash=None, x_registry_hash_algorithm=None) -> web.Response:
    """Create artifact

    Creates a new artifact by posting the artifact content.  The body of the request should be the raw content of the artifact.  This is typically in JSON format for *most* of the  supported types, but may be in another format for a few (for example, &#x60;PROTOBUF&#x60;).  The registry attempts to figure out what kind of artifact is being added from the following supported list:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  Alternatively, you can specify the artifact type using the &#x60;X-Registry-ArtifactType&#x60;  HTTP request header, or include a hint in the request&#39;s &#x60;Content-Type&#x60;.  For example:  &#x60;&#x60;&#x60; Content-Type: application/json; artifactType&#x3D;AVRO &#x60;&#x60;&#x60;  An artifact is created using the content provided in the body of the request.  This content is created under a unique artifact ID that can be provided in the request using the &#x60;X-Registry-ArtifactId&#x60; request header.  If not provided in the request, the server generates a unique ID for the artifact.  It is typically recommended that callers provide the ID, because this is typically a meaningful identifier,  and for most use cases should be supplied by the caller.  If an artifact with the provided artifact ID already exists, the default behavior is for the server to reject the content with a 409 error.  However, the caller can supply the &#x60;ifExists&#x60; query parameter to alter this default behavior. The &#x60;ifExists&#x60; query parameter can have one of the following values:  * &#x60;FAIL&#x60; (*default*) - server rejects the content with a 409 error * &#x60;UPDATE&#x60; - server updates the existing artifact and returns the new metadata * &#x60;RETURN&#x60; - server does not create or add content to the server, but instead  returns the metadata for the existing artifact * &#x60;RETURN_OR_UPDATE&#x60; - server returns an existing **version** that matches the  provided content if such a version exists, otherwise a new version is created  This operation may fail for one of the following reasons:  * An invalid &#x60;ArtifactType&#x60; was indicated (HTTP error &#x60;400&#x60;) * No &#x60;ArtifactType&#x60; was indicated and the server could not determine one from the content (HTTP error &#x60;400&#x60;) * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * An artifact with the provided ID already exists (HTTP error &#x60;409&#x60;) * The content violates one of the configured global rules (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param body: The content of the artifact being created. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;) 
    :type body: str
    :param x_registry_artifact_type: Specifies the type of the artifact being added. Possible values include:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)
    :type x_registry_artifact_type: str
    :param x_registry_artifact_id: A client-provided, globally unique identifier for the new artifact.
    :type x_registry_artifact_id: str
    :param x_registry_version: Specifies the version number of this initial version of the artifact content.  This would typically be a simple integer or a SemVer value.  If not provided, the server will assign a version number automatically (starting with version &#x60;1&#x60;).
    :type x_registry_version: str
    :param if_exists: Set this option to instruct the server on what to do if the artifact already exists.
    :type if_exists: dict | bytes
    :param canonical: Used only when the &#x60;ifExists&#x60; query parameter is set to &#x60;RETURN_OR_UPDATE&#x60;, this parameter can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for a matching version.  The canonicalization algorithm is unique to each artifact type, but typically involves removing extra whitespace and formatting the content in a consistent manner.
    :type canonical: bool
    :param x_registry_description: Specifies the description of artifact being added. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.
    :type x_registry_description: str
    :param x_registry_description_encoded: Specifies the description of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.
    :type x_registry_description_encoded: str
    :param x_registry_name: Specifies the name of artifact being added. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content.
    :type x_registry_name: str
    :param x_registry_name_encoded: Specifies the name of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.
    :type x_registry_name_encoded: str
    :param x_registry_content_hash: Specifies the (optional) hash of the artifact to be verified.
    :type x_registry_content_hash: str
    :param x_registry_hash_algorithm: The algorithm to use when checking the content validity. (available: SHA256, MD5; default: SHA256)
    :type x_registry_hash_algorithm: str

    """
    if_exists = .from_dict(if_exists)
    return web.Response(status=200)


async def delete_artifact(request: web.Request, group_id, artifact_id) -> web.Response:
    """Delete artifact

    Deletes an artifact completely, resulting in all versions of the artifact also being deleted.  This may fail for one of the following reasons:  * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str

    """
    return web.Response(status=200)


async def delete_artifacts_in_group(request: web.Request, group_id) -> web.Response:
    """Delete artifacts in group

    Deletes all of the artifacts that exist in a given group.

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str

    """
    return web.Response(status=200)


async def get_content_by_global_id(request: web.Request, global_id, dereference=None) -> web.Response:
    """Get artifact by global ID

    Gets the content for an artifact version in the registry using its globally unique identifier.  This operation may fail for one of the following reasons:  * No artifact version with this &#x60;globalId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param global_id: Global identifier for an artifact version.
    :type global_id: int
    :param dereference: Allows the user to specify if the content should be dereferenced when being returned
    :type dereference: bool

    """
    return web.Response(status=200)


async def get_content_by_hash(request: web.Request, content_hash) -> web.Response:
    """Get artifact content by SHA-256 hash

    Gets the content for an artifact version in the registry using the  SHA-256 hash of the content.  This content hash may be shared by multiple artifact versions in the case where the artifact versions have identical content.  This operation may fail for one of the following reasons:  * No content with this &#x60;contentHash&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param content_hash: SHA-256 content hash for a single artifact content.
    :type content_hash: str

    """
    return web.Response(status=200)


async def get_content_by_id(request: web.Request, content_id) -> web.Response:
    """Get artifact content by ID

    Gets the content for an artifact version in the registry using the unique content identifier for that content.  This content ID may be shared by multiple artifact versions in the case where the artifact versions are identical.  This operation may fail for one of the following reasons:  * No content with this &#x60;contentId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param content_id: Global identifier for a single artifact content.
    :type content_id: int

    """
    return web.Response(status=200)


async def get_latest_artifact(request: web.Request, group_id, artifact_id, dereference=None) -> web.Response:
    """Get latest artifact

    Returns the latest version of the artifact in its raw form.  The &#x60;Content-Type&#x60; of the response depends on the artifact type.  In most cases, this is &#x60;application/json&#x60;, but  for some types it may be different (for example, &#x60;PROTOBUF&#x60;). If the latest version of the artifact is marked as &#x60;DISABLED&#x60;, the next available non-disabled version will be used.  This operation may fail for one of the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists or all versions are &#x60;DISABLED&#x60; (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param dereference: Allows the user to specify if the content should be dereferenced when being returned
    :type dereference: bool

    """
    return web.Response(status=200)


async def list_artifacts_in_group(request: web.Request, group_id, limit=None, offset=None, order=None, orderby=None) -> web.Response:
    """List artifacts in group

    Returns a list of all artifacts in the group.  This list is paged.

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param limit: The number of artifacts to return.  Defaults to 20.
    :type limit: int
    :param offset: The number of artifacts to skip before starting the result set.  Defaults to 0.
    :type offset: int
    :param order: Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;).
    :type order: dict | bytes
    :param orderby: The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60; 
    :type orderby: dict | bytes

    """
    order = .from_dict(order)
    orderby = .from_dict(orderby)
    return web.Response(status=200)


async def references_by_content_hash(request: web.Request, content_hash) -> web.Response:
    """List artifact references by hash

    Returns a list containing all the artifact references using the artifact content hash.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param content_hash: SHA-256 content hash for a single artifact content.
    :type content_hash: str

    """
    return web.Response(status=200)


async def references_by_content_id(request: web.Request, content_id) -> web.Response:
    """List artifact references by content ID

    Returns a list containing all the artifact references using the artifact content ID.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;)

    :param content_id: Global identifier for a single artifact content.
    :type content_id: int

    """
    return web.Response(status=200)


async def references_by_global_id(request: web.Request, global_id) -> web.Response:
    """List artifact references by global ID

    Returns a list containing all the artifact references using the artifact global ID.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;)

    :param global_id: Global identifier for an artifact version.
    :type global_id: int

    """
    return web.Response(status=200)


async def search_artifacts_0(request: web.Request, name=None, offset=None, limit=None, order=None, orderby=None, labels=None, properties=None, description=None, group=None, global_id=None, content_id=None) -> web.Response:
    """Search for artifacts

    Returns a paginated list of all artifacts that match the provided filter criteria. 

    :param name: Filter by artifact name.
    :type name: str
    :param offset: The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
    :type offset: int
    :param limit: The number of artifacts to return.  Defaults to 20.
    :type limit: int
    :param order: Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;).
    :type order: dict | bytes
    :param orderby: The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60; 
    :type orderby: dict | bytes
    :param labels: Filter by label.  Include one or more label to only return artifacts containing all of the specified labels.
    :type labels: List[str]
    :param properties: Filter by one or more name/value property.  Separate each name/value pair using a colon.  For example &#x60;properties&#x3D;foo:bar&#x60; will return only artifacts with a custom property named &#x60;foo&#x60; and value &#x60;bar&#x60;.
    :type properties: List[str]
    :param description: Filter by description.
    :type description: str
    :param group: Filter by artifact group.
    :type group: str
    :param global_id: Filter by globalId.
    :type global_id: int
    :param content_id: Filter by contentId.
    :type content_id: int

    """
    order = .from_dict(order)
    orderby = .from_dict(orderby)
    return web.Response(status=200)


async def search_artifacts_by_content_0(request: web.Request, body, canonical=None, artifact_type=None, offset=None, limit=None, order=None, orderby=None) -> web.Response:
    """Search for artifacts by content

    Returns a paginated list of all artifacts with at least one version that matches the posted content. 

    :param body: The content to search for.
    :type body: str
    :param canonical: Parameter that can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the &#x60;artifactType&#x60; query parameter.
    :type canonical: bool
    :param artifact_type: Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the &#x60;canonical&#x60; query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts.
    :type artifact_type: str
    :param offset: The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
    :type offset: int
    :param limit: The number of artifacts to return.  Defaults to 20.
    :type limit: int
    :param order: Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;).
    :type order: str
    :param orderby: The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60; 
    :type orderby: str

    """
    return web.Response(status=200)


async def update_artifact(request: web.Request, group_id, artifact_id, body, x_registry_version=None, x_registry_name=None, x_registry_name_encoded=None, x_registry_description=None, x_registry_description_encoded=None) -> web.Response:
    """Update artifact

    Updates an artifact by uploading new content.  The body of the request can be the raw content of the artifact or a JSON object containing both the raw content and a set of references to other artifacts..  This is typically in JSON format for *most* of the supported types, but may be in another format for a few (for example, &#x60;PROTOBUF&#x60;). The type of the content should be compatible with the artifact&#39;s type (it would be an error to update an &#x60;AVRO&#x60; artifact with new &#x60;OPENAPI&#x60; content, for example).  The update could fail for a number of reasons including:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * The new content violates one of the rules configured for the artifact (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)  When successful, this creates a new version of the artifact, making it the most recent (and therefore official) version of the artifact.

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param body: The new content of the artifact being updated. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;) 
    :type body: str
    :param x_registry_version: Specifies the version number of this new version of the artifact content.  This would typically be a simple integer or a SemVer value.  If not provided, the server will assign a version number automatically.
    :type x_registry_version: str
    :param x_registry_name: Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content.
    :type x_registry_name: str
    :param x_registry_name_encoded: Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.
    :type x_registry_name_encoded: str
    :param x_registry_description: Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.
    :type x_registry_description: str
    :param x_registry_description_encoded: Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.
    :type x_registry_description_encoded: str

    """
    return web.Response(status=200)


async def update_artifact_state(request: web.Request, group_id, artifact_id, body) -> web.Response:
    """Update artifact state

    Updates the state of the artifact.  For example, you can use this to mark the latest version of an artifact as &#x60;DEPRECATED&#x60;. The operation changes the state of the latest version of the artifact, even if this version is &#x60;DISABLED&#x60;. If multiple versions exist, only the most recent is changed.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateState.from_dict(body)
    return web.Response(status=200)
