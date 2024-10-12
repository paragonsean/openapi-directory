from typing import List, Dict
from aiohttp import web

from openapi_server.models.issue_type_ids import IssueTypeIds
from openapi_server.models.issue_type_screen_scheme_details import IssueTypeScreenSchemeDetails
from openapi_server.models.issue_type_screen_scheme_id import IssueTypeScreenSchemeId
from openapi_server.models.issue_type_screen_scheme_mapping_details import IssueTypeScreenSchemeMappingDetails
from openapi_server.models.issue_type_screen_scheme_project_association import IssueTypeScreenSchemeProjectAssociation
from openapi_server.models.issue_type_screen_scheme_update_details import IssueTypeScreenSchemeUpdateDetails
from openapi_server.models.page_bean_issue_type_screen_scheme import PageBeanIssueTypeScreenScheme
from openapi_server.models.page_bean_issue_type_screen_scheme_item import PageBeanIssueTypeScreenSchemeItem
from openapi_server.models.page_bean_issue_type_screen_schemes_projects import PageBeanIssueTypeScreenSchemesProjects
from openapi_server.models.page_bean_project_details import PageBeanProjectDetails
from openapi_server.models.update_default_screen_scheme import UpdateDefaultScreenScheme
from openapi_server import util


async def append_mappings_for_issue_type_screen_scheme(request: web.Request, issue_type_screen_scheme_id, body) -> web.Response:
    """Append mappings to issue type screen scheme

    Appends issue type to screen scheme mappings to an issue type screen scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param issue_type_screen_scheme_id: The ID of the issue type screen scheme.
    :type issue_type_screen_scheme_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssueTypeScreenSchemeMappingDetails.from_dict(body)
    return web.Response(status=200)


async def assign_issue_type_screen_scheme_to_project(request: web.Request, body) -> web.Response:
    """Assign issue type screen scheme to project

    Assigns an issue type screen scheme to a project.  Issue type screen schemes can only be assigned to classic projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = IssueTypeScreenSchemeProjectAssociation.from_dict(body)
    return web.Response(status=200)


async def create_issue_type_screen_scheme(request: web.Request, body) -> web.Response:
    """Create issue type screen scheme

    Creates an issue type screen scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: An issue type screen scheme bean.
    :type body: dict | bytes

    """
    body = IssueTypeScreenSchemeDetails.from_dict(body)
    return web.Response(status=200)


async def delete_issue_type_screen_scheme(request: web.Request, issue_type_screen_scheme_id) -> web.Response:
    """Delete issue type screen scheme

    Deletes an issue type screen scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param issue_type_screen_scheme_id: The ID of the issue type screen scheme.
    :type issue_type_screen_scheme_id: str

    """
    return web.Response(status=200)


async def get_issue_type_screen_scheme_mappings(request: web.Request, start_at=None, max_results=None, issue_type_screen_scheme_id=None) -> web.Response:
    """Get issue type screen scheme items

    Returns a [paginated](#pagination) list of issue type screen scheme items.  Only issue type screen schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param issue_type_screen_scheme_id: The list of issue type screen scheme IDs. To include multiple issue type screen schemes, separate IDs with ampersand: &#x60;issueTypeScreenSchemeId&#x3D;10000&amp;issueTypeScreenSchemeId&#x3D;10001&#x60;.
    :type issue_type_screen_scheme_id: List[int]

    """
    return web.Response(status=200)


async def get_issue_type_screen_scheme_project_associations(request: web.Request, project_id, start_at=None, max_results=None) -> web.Response:
    """Get issue type screen schemes for projects

    Returns a [paginated](#pagination) list of issue type screen schemes and, for each issue type screen scheme, a list of the projects that use it.  Only issue type screen schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id: The list of project IDs. To include multiple projects, separate IDs with ampersand: &#x60;projectId&#x3D;10000&amp;projectId&#x3D;10001&#x60;.
    :type project_id: List[int]
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_issue_type_screen_schemes(request: web.Request, start_at=None, max_results=None, id=None, query_string=None, order_by=None, expand=None) -> web.Response:
    """Get issue type screen schemes

    Returns a [paginated](#pagination) list of issue type screen schemes.  Only issue type screen schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param id: The list of issue type screen scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, &#x60;id&#x3D;10000&amp;id&#x3D;10001&#x60;.
    :type id: List[int]
    :param query_string: String used to perform a case-insensitive partial match with issue type screen scheme name.
    :type query_string: str
    :param order_by: [Order](#ordering) the results by a field:   *  &#x60;name&#x60; Sorts by issue type screen scheme name.  *  &#x60;id&#x60; Sorts by issue type screen scheme ID.
    :type order_by: str
    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts &#x60;projects&#x60; that, for each issue type screen schemes, returns information about the projects the issue type screen scheme is assigned to.
    :type expand: str

    """
    return web.Response(status=200)


async def get_projects_for_issue_type_screen_scheme(request: web.Request, issue_type_screen_scheme_id, start_at=None, max_results=None, query=None) -> web.Response:
    """Get issue type screen scheme projects

    Returns a [paginated](#pagination) list of projects associated with an issue type screen scheme.  Only company-managed projects associated with an issue type screen scheme are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param issue_type_screen_scheme_id: The ID of the issue type screen scheme.
    :type issue_type_screen_scheme_id: int
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param query: 
    :type query: str

    """
    return web.Response(status=200)


async def remove_mappings_from_issue_type_screen_scheme(request: web.Request, issue_type_screen_scheme_id, body) -> web.Response:
    """Remove mappings from issue type screen scheme

    Removes issue type to screen scheme mappings from an issue type screen scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param issue_type_screen_scheme_id: The ID of the issue type screen scheme.
    :type issue_type_screen_scheme_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssueTypeIds.from_dict(body)
    return web.Response(status=200)


async def update_default_screen_scheme(request: web.Request, issue_type_screen_scheme_id, body) -> web.Response:
    """Update issue type screen scheme default screen scheme

    Updates the default screen scheme of an issue type screen scheme. The default screen scheme is used for all unmapped issue types.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param issue_type_screen_scheme_id: The ID of the issue type screen scheme.
    :type issue_type_screen_scheme_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDefaultScreenScheme.from_dict(body)
    return web.Response(status=200)


async def update_issue_type_screen_scheme(request: web.Request, issue_type_screen_scheme_id, body) -> web.Response:
    """Update issue type screen scheme

    Updates an issue type screen scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param issue_type_screen_scheme_id: The ID of the issue type screen scheme.
    :type issue_type_screen_scheme_id: str
    :param body: The issue type screen scheme update details.
    :type body: dict | bytes

    """
    body = IssueTypeScreenSchemeUpdateDetails.from_dict(body)
    return web.Response(status=200)
