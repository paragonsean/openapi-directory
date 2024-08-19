from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_annotation import CheckAnnotation
from openapi_server.models.check_run import CheckRun
from openapi_server.models.check_suite import CheckSuite
from openapi_server.models.check_suite_preference import CheckSuitePreference
from openapi_server.models.checks_create_request import ChecksCreateRequest
from openapi_server.models.checks_create_suite_request import ChecksCreateSuiteRequest
from openapi_server.models.checks_list_for_suite200_response import ChecksListForSuite200Response
from openapi_server.models.checks_list_suites_for_ref200_response import ChecksListSuitesForRef200Response
from openapi_server.models.checks_set_suites_preferences_request import ChecksSetSuitesPreferencesRequest
from openapi_server.models.checks_update_request import ChecksUpdateRequest
from openapi_server import util


async def checks_create(request: web.Request, owner, repo, body) -> web.Response:
    """Create a check run

    **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array.  Creates a new check run for a specific commit in a repository. Your GitHub App must have the &#x60;checks:write&#x60; permission to create check runs.  In a check suite, GitHub limits the number of check runs with the same name to 1000. Once these check runs exceed 1000, GitHub will start to automatically delete older check runs.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChecksCreateRequest.from_dict(body)
    return web.Response(status=200)


async def checks_create_suite(request: web.Request, owner, repo, body=None) -> web.Response:
    """Create a check suite

    **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array and a &#x60;null&#x60; value for &#x60;head_branch&#x60;.  By default, check suites are automatically created when you create a [check run](https://docs.github.com/enterprise-server@2.19/rest/reference/checks#check-runs). You only need to use this endpoint for manually creating check suites when you&#39;ve disabled automatic creation using \&quot;[Update repository preferences for check suites](https://docs.github.com/enterprise-server@2.19/rest/reference/checks#update-repository-preferences-for-check-suites)\&quot;. Your GitHub App must have the &#x60;checks:write&#x60; permission to create check suites.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChecksCreateSuiteRequest.from_dict(body)
    return web.Response(status=200)


async def checks_get(request: web.Request, owner, repo, check_run_id) -> web.Response:
    """Get a check run

    **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array.  Gets a single check run using its &#x60;id&#x60;. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to get check runs. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get check runs in a private repository.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param check_run_id: check_run_id parameter
    :type check_run_id: int

    """
    return web.Response(status=200)


async def checks_get_suite(request: web.Request, owner, repo, check_suite_id) -> web.Response:
    """Get a check suite

    **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array and a &#x60;null&#x60; value for &#x60;head_branch&#x60;.  Gets a single check suite using its &#x60;id&#x60;. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to get check suites. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get check suites in a private repository.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param check_suite_id: check_suite_id parameter
    :type check_suite_id: int

    """
    return web.Response(status=200)


async def checks_list_annotations(request: web.Request, owner, repo, check_run_id, per_page=None, page=None) -> web.Response:
    """List check run annotations

    Lists annotations for a check run using the annotation &#x60;id&#x60;. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to get annotations for a check run. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get annotations for a check run in a private repository.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param check_run_id: check_run_id parameter
    :type check_run_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def checks_list_for_ref(request: web.Request, owner, repo, ref, check_name=None, status=None, filter=None, per_page=None, page=None, app_id=None) -> web.Response:
    """List check runs for a Git reference

    **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array.  Lists check runs for a commit ref. The &#x60;ref&#x60; can be a SHA, branch name, or a tag name. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to get check runs. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get check runs in a private repository.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: ref parameter
    :type ref: str
    :param check_name: Returns check runs with the specified &#x60;name&#x60;.
    :type check_name: str
    :param status: Returns check runs with the specified &#x60;status&#x60;. Can be one of &#x60;queued&#x60;, &#x60;in_progress&#x60;, or &#x60;completed&#x60;.
    :type status: str
    :param filter: Filters check runs by their &#x60;completed_at&#x60; timestamp. Can be one of &#x60;latest&#x60; (returning the most recent check runs) or &#x60;all&#x60;.
    :type filter: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def checks_list_for_suite(request: web.Request, owner, repo, check_suite_id, check_name=None, status=None, filter=None, per_page=None, page=None) -> web.Response:
    """List check runs in a check suite

    **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array.  Lists check runs for a check suite using its &#x60;id&#x60;. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to get check runs. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get check runs in a private repository.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param check_suite_id: check_suite_id parameter
    :type check_suite_id: int
    :param check_name: Returns check runs with the specified &#x60;name&#x60;.
    :type check_name: str
    :param status: Returns check runs with the specified &#x60;status&#x60;. Can be one of &#x60;queued&#x60;, &#x60;in_progress&#x60;, or &#x60;completed&#x60;.
    :type status: str
    :param filter: Filters check runs by their &#x60;completed_at&#x60; timestamp. Can be one of &#x60;latest&#x60; (returning the most recent check runs) or &#x60;all&#x60;.
    :type filter: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def checks_list_suites_for_ref(request: web.Request, owner, repo, ref, app_id=None, check_name=None, per_page=None, page=None) -> web.Response:
    """List check suites for a Git reference

    **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array and a &#x60;null&#x60; value for &#x60;head_branch&#x60;.  Lists check suites for a commit &#x60;ref&#x60;. The &#x60;ref&#x60; can be a SHA, branch name, or a tag name. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to list check suites. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get check suites in a private repository.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param ref: ref parameter
    :type ref: str
    :param app_id: Filters check suites by GitHub App &#x60;id&#x60;.
    :type app_id: int
    :param check_name: Returns check runs with the specified &#x60;name&#x60;.
    :type check_name: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def checks_rerequest_suite(request: web.Request, owner, repo, check_suite_id) -> web.Response:
    """Rerequest a check suite

    Triggers GitHub to rerequest an existing check suite, without pushing new code to a repository. This endpoint will trigger the [&#x60;check_suite&#x60; webhook](https://docs.github.com/enterprise-server@2.19/webhooks/event-payloads/#check_suite) event with the action &#x60;rerequested&#x60;. When a check suite is &#x60;rerequested&#x60;, its &#x60;status&#x60; is reset to &#x60;queued&#x60; and the &#x60;conclusion&#x60; is cleared.  To rerequest a check suite, your GitHub App must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param check_suite_id: check_suite_id parameter
    :type check_suite_id: int

    """
    return web.Response(status=200)


async def checks_set_suites_preferences(request: web.Request, owner, repo, body) -> web.Response:
    """Update repository preferences for check suites

    Changes the default automatic flow when creating check suites. By default, a check suite is automatically created each time code is pushed to a repository. When you disable the automatic creation of check suites, you can manually [Create a check suite](https://docs.github.com/enterprise-server@2.19/rest/reference/checks#create-a-check-suite). You must have admin permissions in the repository to set preferences for check suites.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChecksSetSuitesPreferencesRequest.from_dict(body)
    return web.Response(status=200)


async def checks_update(request: web.Request, owner, repo, check_run_id, body=None) -> web.Response:
    """Update a check run

    **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array.  Updates a check run for a specific commit in a repository. Your GitHub App must have the &#x60;checks:write&#x60; permission to edit check runs.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param check_run_id: check_run_id parameter
    :type check_run_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ChecksUpdateRequest.from_dict(body)
    return web.Response(status=200)
