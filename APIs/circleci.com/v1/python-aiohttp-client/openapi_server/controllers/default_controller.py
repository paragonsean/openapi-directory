from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact import Artifact
from openapi_server.models.build import Build
from openapi_server.models.build_detail import BuildDetail
from openapi_server.models.build_summary import BuildSummary
from openapi_server.models.envvar import Envvar
from openapi_server.models.key import Key
from openapi_server.models.project import Project
from openapi_server.models.project_username_project_build_cache_delete200_response import ProjectUsernameProjectBuildCacheDelete200Response
from openapi_server.models.project_username_project_checkout_key_fingerprint_delete200_response import ProjectUsernameProjectCheckoutKeyFingerprintDelete200Response
from openapi_server.models.project_username_project_post_request import ProjectUsernameProjectPostRequest
from openapi_server.models.project_username_project_ssh_key_post_default_response import ProjectUsernameProjectSshKeyPostDefaultResponse
from openapi_server.models.project_username_project_ssh_key_post_request import ProjectUsernameProjectSshKeyPostRequest
from openapi_server.models.project_username_project_tree_branch_post_request import ProjectUsernameProjectTreeBranchPostRequest
from openapi_server.models.tests import Tests
from openapi_server.models.user import User
from openapi_server import util


async def me_get(request: web.Request, ) -> web.Response:
    """me_get

    Provides information about the signed in user. 


    """
    return web.Response(status=200)


async def project_username_project_build_cache_delete(request: web.Request, username, project) -> web.Response:
    """project_username_project_build_cache_delete

    Clears the cache for a project. 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str

    """
    return web.Response(status=200)


async def project_username_project_build_num_artifacts_get(request: web.Request, username, project, build_num) -> web.Response:
    """project_username_project_build_num_artifacts_get

    List the artifacts produced by a given build. 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param build_num: XXXXXXXXXX 
    :type build_num: int

    """
    return web.Response(status=200)


async def project_username_project_build_num_cancel_post(request: web.Request, username, project, build_num) -> web.Response:
    """project_username_project_build_num_cancel_post

    Cancels the build, returns a summary of the build. 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param build_num: XXXXXXXXXX 
    :type build_num: int

    """
    return web.Response(status=200)


async def project_username_project_build_num_get(request: web.Request, username, project, build_num) -> web.Response:
    """project_username_project_build_num_get

    Full details for a single build. The response includes all of the fields from the build summary. This is also the payload for the [notification webhooks](/docs/configuration/#notify), in which case this object is the value to a key named &#39;payload&#39;. 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param build_num: XXXXXXXXXX 
    :type build_num: int

    """
    return web.Response(status=200)


async def project_username_project_build_num_retry_post(request: web.Request, username, project, build_num) -> web.Response:
    """project_username_project_build_num_retry_post

    Retries the build, returns a summary of the new build. 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param build_num: XXXXXXXXXX 
    :type build_num: int

    """
    return web.Response(status=200)


async def project_username_project_build_num_tests_get(request: web.Request, username, project, build_num) -> web.Response:
    """project_username_project_build_num_tests_get

    Provides test metadata for a build Note: [Learn how to set up your builds to collect test metadata](https://circleci.com/docs/test-metadata/) 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param build_num: XXXXXXXXXX 
    :type build_num: int

    """
    return web.Response(status=200)


async def project_username_project_checkout_key_fingerprint_delete(request: web.Request, username, project, fingerprint) -> web.Response:
    """project_username_project_checkout_key_fingerprint_delete

    Delete a checkout key. 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param fingerprint: XXXXXXXXXX 
    :type fingerprint: str

    """
    return web.Response(status=200)


async def project_username_project_checkout_key_fingerprint_get(request: web.Request, username, project, fingerprint) -> web.Response:
    """project_username_project_checkout_key_fingerprint_get

    Get a checkout key. 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param fingerprint: XXXXXXXXXX 
    :type fingerprint: str

    """
    return web.Response(status=200)


async def project_username_project_checkout_key_get(request: web.Request, username, project) -> web.Response:
    """project_username_project_checkout_key_get

    Lists checkout keys. 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str

    """
    return web.Response(status=200)


async def project_username_project_checkout_key_post(request: web.Request, username, project, body=None) -> web.Response:
    """project_username_project_checkout_key_post

    Creates a new checkout key. Only usable with a user API token. 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param body: The type of key to create. Can be &#39;deploy-key&#39; or &#39;github-user-key&#39;. 
    :type body: str

    """
    return web.Response(status=200)


async def project_username_project_envvar_get(request: web.Request, username, project) -> web.Response:
    """project_username_project_envvar_get

    Lists the environment variables for :project 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str

    """
    return web.Response(status=200)


async def project_username_project_envvar_name_delete(request: web.Request, username, project, name) -> web.Response:
    """project_username_project_envvar_name_delete

    Deletes the environment variable named &#39;:name&#39; 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param name: XXXXXXXXXX 
    :type name: str

    """
    return web.Response(status=200)


async def project_username_project_envvar_name_get(request: web.Request, username, project, name) -> web.Response:
    """project_username_project_envvar_name_get

    Gets the hidden value of environment variable :name 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param name: XXXXXXXXXX 
    :type name: str

    """
    return web.Response(status=200)


async def project_username_project_envvar_post(request: web.Request, username, project) -> web.Response:
    """project_username_project_envvar_post

    Creates a new environment variable 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str

    """
    return web.Response(status=200)


async def project_username_project_get(request: web.Request, username, project, limit=None, offset=None, filter=None) -> web.Response:
    """project_username_project_get

    Build summary for each of the last 30 builds for a single git repo. 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param limit: The number of builds to return. Maximum 100, defaults to 30. 
    :type limit: int
    :param offset: The API returns builds starting from this offset, defaults to 0. 
    :type offset: int
    :param filter: Restricts which builds are returned. Set to \&quot;completed\&quot;, \&quot;successful\&quot;, \&quot;failed\&quot;, \&quot;running\&quot;, or defaults to no filter. 
    :type filter: str

    """
    return web.Response(status=200)


async def project_username_project_post(request: web.Request, username, project, body=None) -> web.Response:
    """project_username_project_post

    Triggers a new build, returns a summary of the build. 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectUsernameProjectPostRequest.from_dict(body)
    return web.Response(status=200)


async def project_username_project_ssh_key_post(request: web.Request, username, project, content_type, body) -> web.Response:
    """project_username_project_ssh_key_post

    Create an ssh key used to access external systems that require SSH key-based authentication 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param content_type: 
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectUsernameProjectSshKeyPostRequest.from_dict(body)
    return web.Response(status=200)


async def project_username_project_tree_branch_post(request: web.Request, username, project, branch, body=None) -> web.Response:
    """project_username_project_tree_branch_post

    Triggers a new build, returns a summary of the build. Optional build parameters can be set using an experimental API.  Note: For more about build parameters, read about [using parameterized builds](https://circleci.com/docs/parameterized-builds/) 

    :param username: XXXXXXXXX 
    :type username: str
    :param project: XXXXXXXXX 
    :type project: str
    :param branch: The branch name should be url-encoded. 
    :type branch: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectUsernameProjectTreeBranchPostRequest.from_dict(body)
    return web.Response(status=200)


async def projects_get(request: web.Request, ) -> web.Response:
    """projects_get

    List of all the projects you&#39;re following on CircleCI, with build information organized by branch. 


    """
    return web.Response(status=200)


async def recent_builds_get(request: web.Request, limit=None, offset=None) -> web.Response:
    """recent_builds_get

    Build summary for each of the last 30 recent builds, ordered by build_num. 

    :param limit: The number of builds to return. Maximum 100, defaults to 30. 
    :type limit: int
    :param offset: The API returns builds starting from this offset, defaults to 0. 
    :type offset: int

    """
    return web.Response(status=200)


async def user_heroku_key_post(request: web.Request, ) -> web.Response:
    """user_heroku_key_post

    Adds your Heroku API key to CircleCI, takes apikey as form param name. 


    """
    return web.Response(status=200)
