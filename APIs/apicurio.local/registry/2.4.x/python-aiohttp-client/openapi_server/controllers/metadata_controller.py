from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact_content import ArtifactContent
from openapi_server.models.artifact_meta_data import ArtifactMetaData
from openapi_server.models.artifact_owner import ArtifactOwner
from openapi_server.models.editable_meta_data import EditableMetaData
from openapi_server.models.error import Error
from openapi_server.models.version_meta_data import VersionMetaData
from openapi_server import util


async def delete_artifact_version_meta_data(request: web.Request, group_id, artifact_id, version) -> web.Response:
    """Delete artifact version metadata

    Deletes the user-editable metadata properties of the artifact version.  Any properties that are not user-editable are preserved.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param version: The unique identifier of a specific version of the artifact content.
    :type version: str

    """
    return web.Response(status=200)


async def get_artifact_meta_data(request: web.Request, group_id, artifact_id) -> web.Response:
    """Get artifact metadata

    Gets the metadata for an artifact in the registry, based on the latest version. If the latest version of the artifact is marked as &#x60;DISABLED&#x60;, the next available non-disabled version will be used. The returned metadata includes both generated (read-only) and editable metadata (such as name and description).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists  or all versions are &#x60;DISABLED&#x60; (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str

    """
    return web.Response(status=200)


async def get_artifact_owner(request: web.Request, group_id, artifact_id) -> web.Response:
    """Get artifact owner

    Gets the owner of an artifact in the registry.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str

    """
    return web.Response(status=200)


async def get_artifact_version_meta_data(request: web.Request, group_id, artifact_id, version) -> web.Response:
    """Get artifact version metadata

    Retrieves the metadata for a single version of the artifact.  The version metadata is  a subset of the artifact metadata and only includes the metadata that is specific to the version (for example, this doesn&#39;t include &#x60;modifiedOn&#x60;).  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param version: The unique identifier of a specific version of the artifact content.
    :type version: str

    """
    return web.Response(status=200)


async def get_artifact_version_meta_data_by_content(request: web.Request, group_id, artifact_id, body, canonical=None) -> web.Response:
    """Get artifact version metadata by content

    Gets the metadata for an artifact that matches the raw content.  Searches the registry for a version of the given artifact matching the content provided in the body of the POST.  This operation can fail for the following reasons:  * Provided content (request body) was empty (HTTP error &#x60;400&#x60;) * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No artifact version matching the provided content exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param body: The content of an artifact version.
    :type body: str
    :param canonical: Parameter that can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for a matching version.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.
    :type canonical: bool

    """
    return web.Response(status=200)


async def update_artifact_meta_data(request: web.Request, group_id, artifact_id, body) -> web.Response:
    """Update artifact metadata

    Updates the editable parts of the artifact&#39;s metadata.  Not all metadata fields can be updated.  For example, &#x60;createdOn&#x60; and &#x60;createdBy&#x60; are both read-only properties.  This operation can fail for the following reasons:  * No artifact with the &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param body: Updated artifact metadata.
    :type body: dict | bytes

    """
    body = EditableMetaData.from_dict(body)
    return web.Response(status=200)


async def update_artifact_owner(request: web.Request, group_id, artifact_id, body) -> web.Response:
    """Update artifact owner

    Changes the ownership of an artifact.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;)

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ArtifactOwner.from_dict(body)
    return web.Response(status=200)


async def update_artifact_version_meta_data(request: web.Request, group_id, artifact_id, version, body) -> web.Response:
    """Update artifact version metadata

    Updates the user-editable portion of the artifact version&#39;s metadata.  Only some of  the metadata fields are editable by the user.  For example, &#x60;description&#x60; is editable,  but &#x60;createdOn&#x60; is not.  This operation can fail for the following reasons:  * No artifact with this &#x60;artifactId&#x60; exists (HTTP error &#x60;404&#x60;) * No version with this &#x60;version&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

    :param group_id: The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.
    :type group_id: str
    :param artifact_id: The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.
    :type artifact_id: str
    :param version: The unique identifier of a specific version of the artifact content.
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = EditableMetaData.from_dict(body)
    return web.Response(status=200)
