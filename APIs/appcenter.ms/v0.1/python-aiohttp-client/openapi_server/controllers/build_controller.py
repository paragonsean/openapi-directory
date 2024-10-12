from typing import List, Dict
from aiohttp import web

from openapi_server.models.branch_configurations_delete200_response import BranchConfigurationsDelete200Response
from openapi_server.models.branch_configurations_get200_response import BranchConfigurationsGet200Response
from openapi_server.models.branch_configurations_update_request import BranchConfigurationsUpdateRequest
from openapi_server.models.build_configurations_get200_response import BuildConfigurationsGet200Response
from openapi_server.models.builds_create_request import BuildsCreateRequest
from openapi_server.models.builds_distribute200_response import BuildsDistribute200Response
from openapi_server.models.builds_distribute_request import BuildsDistributeRequest
from openapi_server.models.builds_get_download_uri200_response import BuildsGetDownloadUri200Response
from openapi_server.models.builds_get_log200_response import BuildsGetLog200Response
from openapi_server.models.builds_get_status_by_app_id200_response import BuildsGetStatusByAppId200Response
from openapi_server.models.builds_list_branches200_response_inner import BuildsListBranches200ResponseInner
from openapi_server.models.builds_list_branches200_response_inner_last_build import BuildsListBranches200ResponseInnerLastBuild
from openapi_server.models.builds_list_branches_default_response import BuildsListBranchesDefaultResponse
from openapi_server.models.builds_list_toolset_projects200_response import BuildsListToolsetProjects200Response
from openapi_server.models.builds_list_toolsets200_response import BuildsListToolsets200Response
from openapi_server.models.builds_list_toolsets200_response_xamarin_inner import BuildsListToolsets200ResponseXamarinInner
from openapi_server.models.builds_list_toolsets200_response_xcode_inner import BuildsListToolsets200ResponseXcodeInner
from openapi_server.models.builds_update_request import BuildsUpdateRequest
from openapi_server.models.commits_list_by_sha_list200_response_inner import CommitsListByShaList200ResponseInner
from openapi_server.models.file_assets_create200_response import FileAssetsCreate200Response
from openapi_server.models.repositories_list200_response_inner import RepositoriesList200ResponseInner
from openapi_server.models.repository_configurations_create_or_update_request import RepositoryConfigurationsCreateOrUpdateRequest
from openapi_server.models.repository_configurations_list200_response_inner import RepositoryConfigurationsList200ResponseInner
from openapi_server import util


async def branch_configurations_create(request: web.Request, branch, owner_name, app_name, body) -> web.Response:
    """branch_configurations_create

    Configures the branch for build

    :param branch: The branch name
    :type branch: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Parameters of the configuration
    :type body: dict | bytes

    """
    body = BranchConfigurationsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def branch_configurations_delete(request: web.Request, branch, owner_name, app_name, body=None) -> web.Response:
    """branch_configurations_delete

    Deletes the branch build configuration

    :param branch: The branch name
    :type branch: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def branch_configurations_get(request: web.Request, branch, owner_name, app_name) -> web.Response:
    """branch_configurations_get

    Gets the branch configuration

    :param branch: The branch name
    :type branch: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def branch_configurations_update(request: web.Request, branch, owner_name, app_name, body) -> web.Response:
    """branch_configurations_update

    Reconfigures the branch for build

    :param branch: The branch name
    :type branch: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Parameters of the configuration
    :type body: dict | bytes

    """
    body = BranchConfigurationsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def build_configurations_get(request: web.Request, branch, owner_name, app_name, format=None) -> web.Response:
    """build_configurations_get

    Gets the build configuration in Azure pipeline YAML format

    :param branch: The branch name
    :type branch: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param format: Configuration format
    :type format: str

    """
    return web.Response(status=200)


async def builds_create(request: web.Request, branch, owner_name, app_name, body=None) -> web.Response:
    """builds_create

    Create a build

    :param branch: The branch name
    :type branch: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Parameters of the build
    :type body: dict | bytes

    """
    body = BuildsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def builds_distribute(request: web.Request, build_id, owner_name, app_name, body) -> web.Response:
    """builds_distribute

    Distribute a build

    :param build_id: The build ID
    :type build_id: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The distribution details
    :type body: dict | bytes

    """
    body = BuildsDistributeRequest.from_dict(body)
    return web.Response(status=200)


async def builds_get(request: web.Request, build_id, owner_name, app_name) -> web.Response:
    """builds_get

    Returns the build detail for the given build ID

    :param build_id: The build ID
    :type build_id: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def builds_get_download_uri(request: web.Request, build_id, download_type, owner_name, app_name) -> web.Response:
    """builds_get_download_uri

    Gets the download URI

    :param build_id: The build ID
    :type build_id: int
    :param download_type: The download type
    :type download_type: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def builds_get_log(request: web.Request, build_id, owner_name, app_name) -> web.Response:
    """builds_get_log

    Get the build log

    :param build_id: The build ID
    :type build_id: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def builds_get_status_by_app_id(request: web.Request, owner_name, app_name) -> web.Response:
    """builds_get_status_by_app_id

    Application specific build service status

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def builds_list_branches(request: web.Request, owner_name, app_name) -> web.Response:
    """builds_list_branches

    Returns the list of Git branches for this application

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def builds_list_by_branch(request: web.Request, branch, owner_name, app_name) -> web.Response:
    """builds_list_by_branch

    Returns the list of builds for the branch

    :param branch: The branch name
    :type branch: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def builds_list_toolset_projects(request: web.Request, branch, os, platform, owner_name, app_name, max_search_depth=None) -> web.Response:
    """builds_list_toolset_projects

    Returns the projects in the repository for the branch, for all toolsets

    :param branch: The branch name
    :type branch: str
    :param os: The desired OS for the project scan; normally the same as the app OS
    :type os: str
    :param platform: The desired platform for the project scan
    :type platform: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param max_search_depth: The depth of the repository to search for project files
    :type max_search_depth: int

    """
    return web.Response(status=200)


async def builds_list_toolsets(request: web.Request, owner_name, app_name, tools=None) -> web.Response:
    """builds_list_toolsets

    Returns available toolsets for application

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param tools: Toolset name
    :type tools: str

    """
    return web.Response(status=200)


async def builds_list_xamarin_sdk_bundles(request: web.Request, owner_name, app_name) -> web.Response:
    """builds_list_xamarin_sdk_bundles

    Gets the Xamarin SDK bundles available to this app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def builds_list_xcode_versions(request: web.Request, owner_name, app_name) -> web.Response:
    """builds_list_xcode_versions

    Gets the Xcode versions available to this app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def builds_update(request: web.Request, build_id, owner_name, app_name, body) -> web.Response:
    """builds_update

    Cancels a build

    :param build_id: The build ID
    :type build_id: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = BuildsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def builds_webhook(request: web.Request, body=None) -> web.Response:
    """builds_webhook

    Public webhook sink

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def commits_list_by_sha_list(request: web.Request, hashes, owner_name, app_name) -> web.Response:
    """commits_list_by_sha_list

    Returns commit information for a batch of shas

    :param hashes: A collection of commit SHAs comma-delimited
    :type hashes: List[str]
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def file_assets_create(request: web.Request, owner_name, app_name, body=None) -> web.Response:
    """file_assets_create

    Create a new asset to upload a file

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def repositories_list(request: web.Request, source_host, owner_name, app_name, vsts_account_name=None, vsts_project_id=None, service_connection_id=None, form=None) -> web.Response:
    """repositories_list

    Gets the repositories available from the source code host

    :param source_host: The source host
    :type source_host: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param vsts_account_name: Filter repositories only for specified account and project, \&quot;vstsProjectId\&quot; is required
    :type vsts_account_name: str
    :param vsts_project_id: Filter repositories only for specified account and project, \&quot;vstsAccountName\&quot; is required
    :type vsts_project_id: str
    :param service_connection_id: The id of the service connection (private). Required for GitLab self-hosted repositories
    :type service_connection_id: str
    :param form: The selected form of the object
    :type form: str

    """
    return web.Response(status=200)


async def repository_configurations_create_or_update(request: web.Request, owner_name, app_name, body) -> web.Response:
    """repository_configurations_create_or_update

    Configures the repository for build

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The repository information
    :type body: dict | bytes

    """
    body = RepositoryConfigurationsCreateOrUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def repository_configurations_delete(request: web.Request, owner_name, app_name) -> web.Response:
    """repository_configurations_delete

    Removes the configuration for the repository

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def repository_configurations_list(request: web.Request, owner_name, app_name, include_inactive=None) -> web.Response:
    """repository_configurations_list

    Returns the repository build configuration status of the app

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param include_inactive: Include inactive configurations if none are active
    :type include_inactive: bool

    """
    return web.Response(status=200)
