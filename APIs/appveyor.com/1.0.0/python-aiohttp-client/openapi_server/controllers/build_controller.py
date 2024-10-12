from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact_model import ArtifactModel
from openapi_server.models.build import Build
from openapi_server.models.build_start_request import BuildStartRequest
from openapi_server.models.error import Error
from openapi_server.models.re_run_build_request import ReRunBuildRequest
from openapi_server import util


async def cancel_build(request: web.Request, account_name, project_slug, build_version) -> web.Response:
    """Cancel build

    

    :param account_name: AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;.
    :type account_name: str
    :param project_slug: Project Slug
    :type project_slug: str
    :param build_version: Build Version (&#x60;version&#x60; property of &#x60;Build&#x60;)
    :type build_version: str

    """
    return web.Response(status=200)


async def get_build_artifact(request: web.Request, job_id, artifact_file_name) -> web.Response:
    """Download build artifact

    

    :param job_id: Build ID (&#x60;jobId&#x60; property of &#x60;BuildJob&#x60;)
    :type job_id: str
    :param artifact_file_name: File name (or path) of a build artifact file. Corresponds to the &#x60;fileName&#x60; property of &#x60;ArtifactModel&#x60;. URL-encoding of slashes in parameter values is optional.
    :type artifact_file_name: str

    """
    return web.Response(status=200)


async def get_build_artifacts(request: web.Request, job_id) -> web.Response:
    """Get build artifacts

    

    :param job_id: Build ID (&#x60;jobId&#x60; property of &#x60;BuildJob&#x60;)
    :type job_id: str

    """
    return web.Response(status=200)


async def get_build_log(request: web.Request, job_id) -> web.Response:
    """Download build log

    

    :param job_id: Build ID (&#x60;jobId&#x60; property of &#x60;BuildJob&#x60;)
    :type job_id: str

    """
    return web.Response(status=200)


async def re_run_build(request: web.Request, body) -> web.Response:
    """Re-run build

    If &#x60;reRunIncomplete&#x60; is &#x60;true&#x60; and all jobs in the referenced build completed successfully, a 500 Internal Server Error is returned with the message \&quot;No failed or cancelled jobs in build with ID {buildId}\&quot;.

    :param body: 
    :type body: dict | bytes

    """
    body = ReRunBuildRequest.from_dict(body)
    return web.Response(status=200)


async def start_build(request: web.Request, body) -> web.Response:
    """Start build of branch most recent commit

    

    :param body: 
    :type body: dict | bytes

    """
    body = BuildStartRequest.from_dict(body)
    return web.Response(status=200)
