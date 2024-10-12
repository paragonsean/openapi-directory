from typing import List, Dict
from aiohttp import web

from openapi_server.models.encrypt_request import EncryptRequest
from openapi_server.models.error import Error
from openapi_server.models.project import Project
from openapi_server.models.project_addition import ProjectAddition
from openapi_server.models.project_build_number_update import ProjectBuildNumberUpdate
from openapi_server.models.project_build_results import ProjectBuildResults
from openapi_server.models.project_deployments_results import ProjectDeploymentsResults
from openapi_server.models.project_history import ProjectHistory
from openapi_server.models.project_settings_results import ProjectSettingsResults
from openapi_server.models.project_with_configuration import ProjectWithConfiguration
from openapi_server.models.stored_name_value import StoredNameValue
from openapi_server import util


async def add_project(request: web.Request, body) -> web.Response:
    """Add project

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProjectAddition.from_dict(body)
    return web.Response(status=200)


async def delete_project(request: web.Request, account_name, project_slug) -> web.Response:
    """Delete project

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str

    """
    return web.Response(status=200)


async def delete_project_build_cache(request: web.Request, account_name, project_slug) -> web.Response:
    """Delete project build cache

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str

    """
    return web.Response(status=200)


async def encrypt_value(request: web.Request, body) -> web.Response:
    """Encrypt a value for use in StoredValue.

    

    :param body: 
    :type body: dict | bytes

    """
    body = EncryptRequest.from_dict(body)
    return web.Response(status=200)


async def get_project_artifact(request: web.Request, account_name, project_slug, artifact_file_name, branch=None, tag=None, job=None, all=None, pr=None) -> web.Response:
    """Get last successful build artifact

    The &#x60;job&#x60; parameter is mandatory if the build contains multiple jobs.

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str
    :param artifact_file_name: File name (or path) of a build artifact file. Corresponds to the &#x60;fileName&#x60; property of &#x60;ArtifactModel&#x60;. URL-encoding of slashes in parameter values is optional.
    :type artifact_file_name: str
    :param branch: Repository Branch
    :type branch: str
    :param tag: A git (or other VCS) tag
    :type tag: str
    :param job: Name of the build job.
    :type job: str
    :param all: Include not only &#x60;successful&#x60;, but also jobs with &#x60;failed&#x60;, and &#x60;cancelled&#x60; status.
    :type all: bool
    :param pr: Include PR builds in the search results? &#x60;true&#x60; - take artifact from PR builds only; &#x60;false&#x60; - do not look for artifact in PR builds; default/unspecified - look for artifact in both PR an non-PR builds. 
    :type pr: bool

    """
    return web.Response(status=200)


async def get_project_branch_status_badge(request: web.Request, status_badge_id, build_branch, svg=None, retina=None, passing_text=None, failing_text=None, pending_text=None) -> web.Response:
    """Get project branch status badge image

    

    :param status_badge_id: ID of the status badge (&#x60;statusBadgeId&#x60; from &#x60;ProjectWithConfiguration&#x60;).
    :type status_badge_id: str
    :param build_branch: Build Branch
    :type build_branch: str
    :param svg: Return an SVG image instead of PNG?  Exclusive with &#x60;retina&#x60;.
    :type svg: bool
    :param retina: Return a larger image suitable for retina displays?  Exclusive with &#x60;svg&#x60;.
    :type retina: bool
    :param passing_text: Text to show in badge when build is passing.
    :type passing_text: str
    :param failing_text: Text to show in badge when build is failing.
    :type failing_text: str
    :param pending_text: Text to show in badge when build is pending.
    :type pending_text: str

    """
    return web.Response(status=200)


async def get_project_build_by_version(request: web.Request, account_name, project_slug, build_version) -> web.Response:
    """Get project build by version

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str
    :param build_version: Build Version (&#x60;version&#x60; property of &#x60;Build&#x60;)
    :type build_version: str

    """
    return web.Response(status=200)


async def get_project_deployments(request: web.Request, account_name, project_slug, records_number) -> web.Response:
    """Get project deployments

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str
    :param records_number: Number of results to include in the response. getProjectDeployments is documented to have a maximum of 20. It currently returns 500 Internal Server Error for recordsNumber &lt;&#x3D; 5. In the past it has returned 500 Internal Server Error for many different values which did not match the value used by the ci.appveyor.com web interface at the time.  As of 2018-09-08, the value used by the web interface is 10.
    :type records_number: int

    """
    return web.Response(status=200)


async def get_project_environment_variables(request: web.Request, account_name, project_slug) -> web.Response:
    """Get project environment variables

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str

    """
    return web.Response(status=200)


async def get_project_history(request: web.Request, account_name, project_slug, records_number, start_build_id=None, branch=None) -> web.Response:
    """Get project history

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str
    :param records_number: Number of results to include in the response. getProjectDeployments is documented to have a maximum of 20. It currently returns 500 Internal Server Error for recordsNumber &lt;&#x3D; 5. In the past it has returned 500 Internal Server Error for many different values which did not match the value used by the ci.appveyor.com web interface at the time.  As of 2018-09-08, the value used by the web interface is 10.
    :type records_number: int
    :param start_build_id: Maximum &#x60;buildId&#x60; to include in the results (exclusive).
    :type start_build_id: int
    :param branch: Repository Branch
    :type branch: str

    """
    return web.Response(status=200)


async def get_project_last_build(request: web.Request, account_name, project_slug) -> web.Response:
    """Get project last build

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str

    """
    return web.Response(status=200)


async def get_project_last_build_branch(request: web.Request, account_name, project_slug, build_branch) -> web.Response:
    """Get project last branch build

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str
    :param build_branch: Build Branch
    :type build_branch: str

    """
    return web.Response(status=200)


async def get_project_settings(request: web.Request, account_name, project_slug) -> web.Response:
    """Get project settings

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str

    """
    return web.Response(status=200)


async def get_project_settings_yaml(request: web.Request, account_name, project_slug) -> web.Response:
    """Get project settings in YAML

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str

    """
    return web.Response(status=200)


async def get_project_status_badge(request: web.Request, status_badge_id, svg=None, retina=None, passing_text=None, failing_text=None, pending_text=None) -> web.Response:
    """Get project status badge image

    

    :param status_badge_id: ID of the status badge (&#x60;statusBadgeId&#x60; from &#x60;ProjectWithConfiguration&#x60;).
    :type status_badge_id: str
    :param svg: Return an SVG image instead of PNG?  Exclusive with &#x60;retina&#x60;.
    :type svg: bool
    :param retina: Return a larger image suitable for retina displays?  Exclusive with &#x60;svg&#x60;.
    :type retina: bool
    :param passing_text: Text to show in badge when build is passing.
    :type passing_text: str
    :param failing_text: Text to show in badge when build is failing.
    :type failing_text: str
    :param pending_text: Text to show in badge when build is pending.
    :type pending_text: str

    """
    return web.Response(status=200)


async def get_projects(request: web.Request, ) -> web.Response:
    """Get projects

    


    """
    return web.Response(status=200)


async def get_public_project_status_badge(request: web.Request, badge_repo_provider, repo_account_name, repo_slug, branch=None, svg=None, retina=None, passing_text=None, failing_text=None, pending_text=None) -> web.Response:
    """Get status badge image for a project with a public repository

    

    :param badge_repo_provider: Repository provider supported for badges
    :type badge_repo_provider: str
    :param repo_account_name: Account name with repository provider
    :type repo_account_name: str
    :param repo_slug: Slug (URL component) of repository.
    :type repo_slug: str
    :param branch: Repository Branch
    :type branch: str
    :param svg: Return an SVG image instead of PNG?  Exclusive with &#x60;retina&#x60;.
    :type svg: bool
    :param retina: Return a larger image suitable for retina displays?  Exclusive with &#x60;svg&#x60;.
    :type retina: bool
    :param passing_text: Text to show in badge when build is passing.
    :type passing_text: str
    :param failing_text: Text to show in badge when build is failing.
    :type failing_text: str
    :param pending_text: Text to show in badge when build is pending.
    :type pending_text: str

    """
    return web.Response(status=200)


async def update_project(request: web.Request, body) -> web.Response:
    """Update project

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProjectWithConfiguration.from_dict(body)
    return web.Response(status=200)


async def update_project_build_number(request: web.Request, account_name, project_slug, body) -> web.Response:
    """Update project build number

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectBuildNumberUpdate.from_dict(body)
    return web.Response(status=200)


async def update_project_environment_variables(request: web.Request, account_name, project_slug, body) -> web.Response:
    """Update project environment variables

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str
    :param body: 
    :type body: list | bytes

    """
    body = [StoredNameValue.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_project_settings_yaml(request: web.Request, account_name, project_slug, body) -> web.Response:
    """Update project settings in YAML

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str
    :param body: The body of requests should contain YAML data.  It is unclear how to specify this since the OpenAPI spec requires &#x60;schema&#x60; without &#x60;type&#x60; for &#x60;in: body&#x60; parameters and does not allow &#x60;type: file&#x60; in &#x60;schema&#x60;.  See https://github.com/OAI/OpenAPI-Specification/issues/326 swagger-codegen (for Java, probably others) allows a binary string body parameter with non-application/json &#x60;consumes&#x60; to be passed through in the request body without conversion to JSON. 
    :type body: str

    """
    return web.Response(status=200)
