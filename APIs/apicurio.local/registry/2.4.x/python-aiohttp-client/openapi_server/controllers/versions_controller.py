from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact_content import ArtifactContent
from openapi_server.models.artifact_reference import ArtifactReference
from openapi_server.models.error import Error
from openapi_server.models.rule_violation_error import RuleViolationError
from openapi_server.models.update_state import UpdateState
from openapi_server.models.version_meta_data import VersionMetaData
from openapi_server.models.version_search_results import VersionSearchResults
from openapi_server import util


async def create_artifact_version(request: web.Request, group_id, artifact_id, body, x_registry_version=None, x_registry_name=None, x_registry_description=None, x_registry_description_encoded=None, x_registry_name_encoded=None) -> web.Response:
    """Create artifact version

    Creates a new version of the artifact by uploading new content.  The configured rules for the artifact are applied, and if they all pass, the new content is added as the most recent  version of the artifact.  If any of the rules fail, an error is returned.  The body of the request can be the raw content of the new artifact version, or the raw content  and a set of references pointing to other artifacts, and the type of that content should match the artifact&#39;s type (for example if the artifact type is &#x60;AVRO&#x60; then the content of the request should be an Apache Avro document).  This operation can fail for the following reasons:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * The new content violates one of the rules configured for the artifact (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param body: The content of the artifact version being created or the content and a set of references to other artifacts. This is often, but not always, JSON data representing one of the supported artifact types:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;) 
    :type body: str
    :param x_registry_version: Specifies the version number of this new version of the artifact content.  This would typically be a simple integer or a SemVer value.  It must be unique within the artifact.  If this is not provided, the server will generate a new, unique version number for this new updated content.
    :type x_registry_version: str
    :param x_registry_name: Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content.
    :type x_registry_name: str
    :param x_registry_description: Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.
    :type x_registry_description: str
    :param x_registry_description_encoded: Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.
    :type x_registry_description_encoded: str
    :param x_registry_name_encoded: Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.
    :type x_registry_name_encoded: str

    """
    return web.Response(status=200)


async def delete_artifact_version(request: web.Request, group_id, artifact_id, version) -> web.Response:
    """Delete artifact version

    Deletes a single version of the artifact. Parameters &#x60;groupId&#x60;, &#x60;artifactId&#x60; and the unique &#x60;version&#x60; are needed. If this is the only version of the artifact, this operation is the same as  deleting the entire artifact.  This feature is disabled by default and it&#39;s discouraged for normal usage. To enable it, set the &#x60;registry.rest.artifact.deletion.enabled&#x60; property to true. This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;)  * Feature is disabled (HTTP error &#x60;405&#x60;)  * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param version: The unique identifier of a specific version of the artifact content.
    :type version: str

    """
    return web.Response(status=200)


async def get_artifact_version(request: web.Request, group_id, artifact_id, version, dereference=None) -> web.Response:
    """Get artifact version

    Retrieves a single version of the artifact content.  Both the &#x60;artifactId&#x60; and the unique &#x60;version&#x60; number must be provided.  The &#x60;Content-Type&#x60; of the response depends  on the artifact type.  In most cases, this is &#x60;application/json&#x60;, but for some types  it may be different (for example, &#x60;PROTOBUF&#x60;).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param version: The unique identifier of a specific version of the artifact content.
    :type version: str
    :param dereference: Allows the user to specify if the content should be dereferenced when being returned
    :type dereference: bool

    """
    return web.Response(status=200)


async def get_artifact_version_references(request: web.Request, group_id, artifact_id, version) -> web.Response:
    """Get artifact version

    Retrieves a single version of the artifact content.  Both the &#x60;artifactId&#x60; and the unique &#x60;version&#x60; number must be provided.  The &#x60;Content-Type&#x60; of the response depends  on the artifact type.  In most cases, this is &#x60;application/json&#x60;, but for some types  it may be different (for example, &#x60;PROTOBUF&#x60;).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param version: The unique identifier of a specific version of the artifact content.
    :type version: str

    """
    return web.Response(status=200)


async def list_artifact_versions(request: web.Request, group_id, artifact_id, offset=None, limit=None) -> web.Response:
    """List artifact versions

    Returns a list of all versions of the artifact.  The result set is paged.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param offset: The number of versions to skip before starting to collect the result set.  Defaults to 0.
    :type offset: int
    :param limit: The number of versions to return.  Defaults to 20.
    :type limit: int

    """
    return web.Response(status=200)


async def update_artifact_version_state(request: web.Request, group_id, artifact_id, version, body) -> web.Response:
    """Update artifact version state

    Updates the state of a specific version of an artifact.  For example, you can use  this operation to disable a specific version.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param version: The unique identifier of a specific version of the artifact content.
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateState.from_dict(body)
    return web.Response(status=200)
