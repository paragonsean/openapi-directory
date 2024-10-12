from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_and_replace_version_bean import DeleteAndReplaceVersionBean
from openapi_server.models.page_bean_version import PageBeanVersion
from openapi_server.models.version import Version
from openapi_server.models.version_issue_counts import VersionIssueCounts
from openapi_server.models.version_move_bean import VersionMoveBean
from openapi_server.models.version_unresolved_issues_count import VersionUnresolvedIssuesCount
from openapi_server import util


async def create_version(request: web.Request, body) -> web.Response:
    """Create version

    Creates a project version.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the version is added to.

    :param body: 
    :type body: dict | bytes

    """
    body = Version.from_dict(body)
    return web.Response(status=200)


async def delete_and_replace_version(request: web.Request, id, body) -> web.Response:
    """Delete and replace version

    Deletes a project version.  Alternative versions can be provided to update issues that use the deleted version in &#x60;fixVersion&#x60;, &#x60;affectedVersion&#x60;, or any version picker custom fields. If alternatives are not provided, occurrences of &#x60;fixVersion&#x60;, &#x60;affectedVersion&#x60;, and any version picker custom field, that contain the deleted version, are cleared. Any replacement version must be in the same project as the version being deleted and cannot be the version being deleted.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

    :param id: The ID of the version.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteAndReplaceVersionBean.from_dict(body)
    return web.Response(status=200)


async def delete_version(request: web.Request, id, move_fix_issues_to=None, move_affected_issues_to=None) -> web.Response:
    """Delete version

    Deletes a project version.  Deprecated, use [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) that supports swapping version values in custom fields, in addition to the swapping for &#x60;fixVersion&#x60; and &#x60;affectedVersion&#x60; provided in this resource.  Alternative versions can be provided to update issues that use the deleted version in &#x60;fixVersion&#x60; or &#x60;affectedVersion&#x60;. If alternatives are not provided, occurrences of &#x60;fixVersion&#x60; and &#x60;affectedVersion&#x60; that contain the deleted version are cleared.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

    :param id: The ID of the version.
    :type id: str
    :param move_fix_issues_to: The ID of the version to update &#x60;fixVersion&#x60; to when the field contains the deleted version. The replacement version must be in the same project as the version being deleted and cannot be the version being deleted.
    :type move_fix_issues_to: str
    :param move_affected_issues_to: The ID of the version to update &#x60;affectedVersion&#x60; to when the field contains the deleted version. The replacement version must be in the same project as the version being deleted and cannot be the version being deleted.
    :type move_affected_issues_to: str

    """
    return web.Response(status=200)


async def get_project_versions(request: web.Request, project_id_or_key, expand=None) -> web.Response:
    """Get project versions

    Returns all versions in a project. The response is not paginated. Use [Get project versions paginated](#api-rest-api-3-project-projectIdOrKey-version-get) if you want to get the versions in a project with pagination.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts &#x60;operations&#x60;, which returns actions that can be performed on the version.
    :type expand: str

    """
    return web.Response(status=200)


async def get_project_versions_paginated(request: web.Request, project_id_or_key, start_at=None, max_results=None, order_by=None, query=None, status=None, expand=None) -> web.Response:
    """Get project versions paginated

    Returns a [paginated](#pagination) list of all versions in a project. See the [Get project versions](#api-rest-api-3-project-projectIdOrKey-versions-get) resource if you want to get a full list of versions without pagination.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param order_by: [Order](#ordering) the results by a field:   *  &#x60;description&#x60; Sorts by version description.  *  &#x60;name&#x60; Sorts by version name.  *  &#x60;releaseDate&#x60; Sorts by release date, starting with the oldest date. Versions with no release date are listed last.  *  &#x60;sequence&#x60; Sorts by the order of appearance in the user interface.  *  &#x60;startDate&#x60; Sorts by start date, starting with the oldest date. Versions with no start date are listed last.
    :type order_by: str
    :param query: Filter the results using a literal string. Versions with matching &#x60;name&#x60; or &#x60;description&#x60; are returned (case insensitive).
    :type query: str
    :param status: A list of status values used to filter the results by version status. This parameter accepts a comma-separated list. The status values are &#x60;released&#x60;, &#x60;unreleased&#x60;, and &#x60;archived&#x60;.
    :type status: str
    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;issuesstatus&#x60; Returns the number of issues in each status category for each version.  *  &#x60;operations&#x60; Returns actions that can be performed on the specified version.
    :type expand: str

    """
    return web.Response(status=200)


async def get_version(request: web.Request, id, expand=None) -> web.Response:
    """Get version

    Returns a project version.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.

    :param id: The ID of the version.
    :type id: str
    :param expand: Use [expand](#expansion) to include additional information about version in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;operations&#x60; Returns the list of operations available for this version.  *  &#x60;issuesstatus&#x60; Returns the count of issues in this version for each of the status categories *to do*, *in progress*, *done*, and *unmapped*. The *unmapped* property represents the number of issues with a status other than *to do*, *in progress*, and *done*.
    :type expand: str

    """
    return web.Response(status=200)


async def get_version_related_issues(request: web.Request, id) -> web.Response:
    """Get version&#39;s related issues count

    Returns the following counts for a version:   *  Number of issues where the &#x60;fixVersion&#x60; is set to the version.  *  Number of issues where the &#x60;affectedVersion&#x60; is set to the version.  *  Number of issues where a version custom field is set to the version.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.

    :param id: The ID of the version.
    :type id: str

    """
    return web.Response(status=200)


async def get_version_unresolved_issues(request: web.Request, id) -> web.Response:
    """Get version&#39;s unresolved issues count

    Returns counts of the issues and unresolved issues for the project version.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.

    :param id: The ID of the version.
    :type id: str

    """
    return web.Response(status=200)


async def merge_versions(request: web.Request, id, move_issues_to) -> web.Response:
    """Merge versions

    Merges two project versions. The merge is completed by deleting the version specified in &#x60;id&#x60; and replacing any occurrences of its ID in &#x60;fixVersion&#x60; with the version ID specified in &#x60;moveIssuesTo&#x60;.  Consider using [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) instead. This resource supports swapping version values in &#x60;fixVersion&#x60;, &#x60;affectedVersion&#x60;, and custom fields.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

    :param id: The ID of the version to delete.
    :type id: str
    :param move_issues_to: The ID of the version to merge into.
    :type move_issues_to: str

    """
    return web.Response(status=200)


async def move_version(request: web.Request, id, body) -> web.Response:
    """Move version

    Modifies the version&#39;s sequence within the project, which affects the display order of the versions in Jira.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.

    :param id: The ID of the version to be moved.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = VersionMoveBean.from_dict(body)
    return web.Response(status=200)


async def update_version(request: web.Request, id, body) -> web.Response:
    """Update version

    Updates a project version.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

    :param id: The ID of the version.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Version.from_dict(body)
    return web.Response(status=200)
