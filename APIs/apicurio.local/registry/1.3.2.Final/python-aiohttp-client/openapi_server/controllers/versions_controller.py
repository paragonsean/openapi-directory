from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.update_state import UpdateState
from openapi_server.models.version_meta_data import VersionMetaData
from openapi_server.models.version_search_results import VersionSearchResults
from openapi_server import util


async def create_artifact_version(request: web.Request, artifact_id, x_registry_artifact_type=None) -> web.Response:
    """Create artifact version

    Creates a new version of the artifact by uploading new content.  The configured rules for the artifact are applied, and if they all pass, the new content is added as the most recent  version of the artifact.  If any of the rules fail, an error is returned.  The body of the request should be the raw content of the new artifact version.  This  is typically in JSON format for *most* of the supported types, but may be in another  format for a few (for example, &#x60;PROTOBUF&#x60;).  The registry attempts to figure out what kind of artifact is being added from the following supported list:  * Avro (&#x60;AVRO&#x60;) * Protobuf (&#x60;PROTOBUF&#x60;) * Protobuf File Descriptor (&#x60;PROTOBUF_FD&#x60;) * JSON Schema (&#x60;JSON&#x60;) * Kafka Connect (&#x60;KCONNECT&#x60;) * OpenAPI (&#x60;OPENAPI&#x60;) * AsyncAPI (&#x60;ASYNCAPI&#x60;) * GraphQL (&#x60;GRAPHQL&#x60;) * Web Services Description Language (&#x60;WSDL&#x60;) * XML Schema (&#x60;XSD&#x60;)  Alternatively, you can explicitly specify the artifact type using the &#x60;X-Registry-ArtifactType&#x60;  HTTP request header, or by including a hint in the request&#39;s &#x60;Content-Type&#x60;.  For example:  &#x60;&#x60;&#x60; Content-Type: application/json; artifactType&#x3D;AVRO &#x60;&#x60;&#x60;  This operation can fail for the following reasons:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * The new content violates one of the rules configured for the artifact (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param artifact_id: The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    :type artifact_id: str
    :param x_registry_artifact_type: This header parameter can be used to indicate the type of the artifact being added. Possible values include:  * Avro (&#x60;AVRO&#x60;)    * Protobuf (&#x60;PROTOBUF&#x60;)   * Protobuf File Descriptor (&#x60;PROTOBUF_FD&#x60;)    * JSON Schema (&#x60;JSON&#x60;)    * Kafka Connect (&#x60;KCONNECT&#x60;)    * OpenAPI (&#x60;OPENAPI&#x60;)    * AsyncAPI (&#x60;ASYNCAPI&#x60;)   * GraphQL (&#x60;GRAPHQL&#x60;)    * Web Services Description Language (&#x60;WSDL&#x60;)    * XML Schema (&#x60;XSD&#x60;)
    :type x_registry_artifact_type: str

    """
    return web.Response(status=200)


async def get_artifact_version(request: web.Request, version, artifact_id) -> web.Response:
    """Get artifact version

    Retrieves a single version of the artifact content.  Both the &#x60;artifactId&#x60; and the unique &#x60;version&#x60; number must be provided.  The &#x60;Content-Type&#x60; of the response depends  on the artifact type.  In most cases, this is &#x60;application/json&#x60;, but for some types  it may be different (for example, &#x60;PROTOBUF&#x60;).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param version: The unique identifier of a specific version of the artifact content.
    :type version: int
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    :type artifact_id: str

    """
    return web.Response(status=200)


async def list_artifact_versions(request: web.Request, artifact_id) -> web.Response:
    """List artifact versions

    Returns a list of all version numbers for the artifact.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param artifact_id: The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    :type artifact_id: str

    """
    return web.Response(status=200)


async def search_versions_0(request: web.Request, artifact_id, offset, limit) -> web.Response:
    """Search artifact versions

    Searches for versions of a specific artifact.  This is typically used to get a listing of all versions of an artifact (for example, in a user interface).

    :param artifact_id: The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    :type artifact_id: str
    :param offset: The number of versions to skip before starting to collect the result set.
    :type offset: int
    :param limit: The number of versions to return.
    :type limit: int

    """
    return web.Response(status=200)


async def update_artifact_version_state(request: web.Request, version, artifact_id, body) -> web.Response:
    """Update artifact version state

    Updates the state of a specific version of an artifact.  For example, you can use  this operation to disable a specific version.  The following state changes are supported:  * Enabled -&gt; Disabled * Enabled -&gt; Deprecated * Enabled -&gt; Deleted * Disabled -&gt; Enabled * Disabled -&gt; Deleted * Disabled -&gt; Deprecated * Deprecated -&gt; Deleted  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * Artifact version cannot transition to the given state (HTTP error &#x60;400&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param version: The unique identifier of a specific version of the artifact content.
    :type version: int
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
    :type artifact_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateState.from_dict(body)
    return web.Response(status=200)
