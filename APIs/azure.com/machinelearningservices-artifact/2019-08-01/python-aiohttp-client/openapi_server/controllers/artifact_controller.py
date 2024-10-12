from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact import Artifact
from openapi_server.models.artifact_container_sas import ArtifactContainerSas
from openapi_server.models.artifact_content_information import ArtifactContentInformation
from openapi_server.models.artifact_id_list import ArtifactIdList
from openapi_server.models.artifact_path_list import ArtifactPathList
from openapi_server.models.batch_artifact_content_information_result import BatchArtifactContentInformationResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.paginated_artifact_content_information_list import PaginatedArtifactContentInformationList
from openapi_server.models.paginated_artifact_list import PaginatedArtifactList
from openapi_server import util


async def artifacts_batch_create_empty_artifacts(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, artifact_paths) -> web.Response:
    """Create a batch of empty Artifacts.

    Create a Batch of empty Artifacts from the supplied paths.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param artifact_paths: The list of Artifact paths to create.
    :type artifact_paths: dict | bytes

    """
    artifact_paths = ArtifactPathList.from_dict(artifact_paths)
    return web.Response(status=200)


async def artifacts_batch_get_by_id(request: web.Request, subscription_id, resource_group_name, workspace_name, artifact_ids) -> web.Response:
    """Get Batch Artifacts by Ids.

    Get Batch Artifacts by the specific Ids.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param artifact_ids: The command for Batch Artifact get request.
    :type artifact_ids: dict | bytes

    """
    artifact_ids = ArtifactIdList.from_dict(artifact_ids)
    return web.Response(status=200)


async def artifacts_batch_get_storage_by_id(request: web.Request, subscription_id, resource_group_name, workspace_name, artifact_ids) -> web.Response:
    """Get Batch Artifacts storage by Ids.

    Get Batch Artifacts storage by specific Ids.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param artifact_ids: The list of artifactIds to get.
    :type artifact_ids: dict | bytes

    """
    artifact_ids = ArtifactIdList.from_dict(artifact_ids)
    return web.Response(status=200)


async def artifacts_batch_ingest_from_sas(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, artifact_container_sas) -> web.Response:
    """Batch ingest using shared access signature.

    Ingest Batch Artifacts using shared access signature.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param artifact_container_sas: The artifact container shared access signature to use for batch ingest.
    :type artifact_container_sas: dict | bytes

    """
    artifact_container_sas = ArtifactContainerSas.from_dict(artifact_container_sas)
    return web.Response(status=200)


async def artifacts_create(request: web.Request, subscription_id, resource_group_name, workspace_name, artifact) -> web.Response:
    """Create Artifact.

    Create an Artifact.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param artifact: The Artifact details.
    :type artifact: dict | bytes

    """
    artifact = Artifact.from_dict(artifact)
    return web.Response(status=200)


async def artifacts_delete_batch_meta_data(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, artifact_paths, hard_delete=None) -> web.Response:
    """Delete Batch of Artifact Metadata.

    Delete a Batch of Artifact Metadata.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param artifact_paths: The list of Artifact paths to delete.
    :type artifact_paths: dict | bytes
    :param hard_delete: If set to true, the delete cannot be reverted at a later time.
    :type hard_delete: bool

    """
    artifact_paths = ArtifactPathList.from_dict(artifact_paths)
    return web.Response(status=200)


async def artifacts_delete_meta_data(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, path=None, hard_delete=None) -> web.Response:
    """Delete Artifact Metadata.

    Delete an Artifact Metadata.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param path: The Artifact Path.
    :type path: str
    :param hard_delete: If set to true. The delete cannot be revert at later time.
    :type hard_delete: bool

    """
    return web.Response(status=200)


async def artifacts_delete_meta_data_in_container(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, hard_delete=None) -> web.Response:
    """Delete Artifact Metadata.

    Delete Artifact Metadata in a specific container.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param hard_delete: If set to true. The delete cannot be revert at later time.
    :type hard_delete: bool

    """
    return web.Response(status=200)


async def artifacts_download(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, path=None) -> web.Response:
    """Get Artifact content by Id.

    Get Artifact content of a specific Id.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param path: The Artifact Path.
    :type path: str

    """
    return web.Response(status=200)


async def artifacts_get(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, path) -> web.Response:
    """Get Artifact metadata by Id.

    Get Artifact metadata for a specific Id.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param path: The Artifact Path.
    :type path: str

    """
    return web.Response(status=200)


async def artifacts_get_content_information(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, path=None) -> web.Response:
    """Get Artifact content information.

    Get content information of an Artifact.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param path: The Artifact Path.
    :type path: str

    """
    return web.Response(status=200)


async def artifacts_get_sas(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, path=None) -> web.Response:
    """Get writable shared access signature for Artifact.

    Get writable shared access signature for a specific Artifact.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param path: The Artifact Path.
    :type path: str

    """
    return web.Response(status=200)


async def artifacts_get_storage_content_information(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, path=None) -> web.Response:
    """Get Artifact storage content information.

    Get storage content information of an Artifact.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param path: The Artifact Path.
    :type path: str

    """
    return web.Response(status=200)


async def artifacts_list_in_container(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, path=None, continuation_token=None) -> web.Response:
    """Get Artifacts metadata in a container or path.

    Get Artifacts metadata in a specific container or path.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param path: The Artifact Path.
    :type path: str
    :param continuation_token: The continuation token.
    :type continuation_token: str

    """
    return web.Response(status=200)


async def artifacts_list_sas_by_prefix(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, path=None, continuation_token=None) -> web.Response:
    """Get shared access signature for an Artifact

    Get shared access signature for an Artifact in specific path.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param path: The Artifact Path.
    :type path: str
    :param continuation_token: The continuation token.
    :type continuation_token: str

    """
    return web.Response(status=200)


async def artifacts_list_storage_uri_by_prefix(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, path=None, continuation_token=None) -> web.Response:
    """Get storage Uri for Artifacts in a path.

    Get storage Uri for Artifacts in a specific path.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param path: The Artifact Path.
    :type path: str
    :param continuation_token: The continuation token.
    :type continuation_token: str

    """
    return web.Response(status=200)


async def artifacts_register(request: web.Request, subscription_id, resource_group_name, workspace_name, artifact) -> web.Response:
    """Create an Artifact for an existing data location.

    Create an Artifact for an existing dataPath.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param artifact: The Artifact creation details.
    :type artifact: dict | bytes

    """
    artifact = Artifact.from_dict(artifact)
    return web.Response(status=200)


async def artifacts_upload(request: web.Request, subscription_id, resource_group_name, workspace_name, origin, container, content, path=None, index=None, append=None, allow_overwrite=None) -> web.Response:
    """Upload Artifact content.

    Upload content to an Artifact.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The Name of the resource group in which the workspace is located.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param origin: The origin of the Artifact.
    :type origin: str
    :param container: The container name.
    :type container: str
    :param content: The file upload.
    :type content: str
    :param path: The Artifact Path.
    :type path: str
    :param index: The index.
    :type index: int
    :param append: Whether or not to append the content or replace it.
    :type append: bool
    :param allow_overwrite: whether to allow overwrite if Artifact Content exist already. when set to true, Overwrite happens if Artifact Content already exists
    :type allow_overwrite: bool

    """
    return web.Response(status=200)
