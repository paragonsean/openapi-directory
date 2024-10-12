from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_project_details import CreateProjectDetails
from openapi_server.models.issue_type_with_status import IssueTypeWithStatus
from openapi_server.models.notification_scheme import NotificationScheme
from openapi_server.models.page_bean_project import PageBeanProject
from openapi_server.models.project import Project
from openapi_server.models.project_identifiers import ProjectIdentifiers
from openapi_server.models.project_issue_type_hierarchy import ProjectIssueTypeHierarchy
from openapi_server.models.task_progress_bean_object import TaskProgressBeanObject
from openapi_server.models.update_project_details import UpdateProjectDetails
from openapi_server import util


async def archive_project(request: web.Request, project_id_or_key) -> web.Response:
    """Archive project

    Archives a project. You can&#39;t delete a project if it&#39;s archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def create_project(request: web.Request, body) -> web.Response:
    """Create project

    Creates a project based on a project type template, as shown in the following table:  | Project Type Key | Project Template Key |   |--|--|   | &#x60;business&#x60; | &#x60;com.atlassian.jira-core-project-templates:jira-core-simplified-content-management&#x60;, &#x60;com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval&#x60;, &#x60;com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking&#x60;, &#x60;com.atlassian.jira-core-project-templates:jira-core-simplified-process-control&#x60;, &#x60;com.atlassian.jira-core-project-templates:jira-core-simplified-procurement&#x60;, &#x60;com.atlassian.jira-core-project-templates:jira-core-simplified-project-management&#x60;, &#x60;com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment&#x60;, &#x60;com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking&#x60; |   | &#x60;service_desk&#x60; | &#x60;com.atlassian.servicedesk:simplified-it-service-management&#x60;, &#x60;com.atlassian.servicedesk:simplified-general-service-desk-it&#x60;, &#x60;com.atlassian.servicedesk:simplified-general-service-desk-business&#x60;, &#x60;com.atlassian.servicedesk:simplified-internal-service-desk&#x60;, &#x60;com.atlassian.servicedesk:simplified-external-service-desk&#x60;, &#x60;com.atlassian.servicedesk:simplified-hr-service-desk&#x60;, &#x60;com.atlassian.servicedesk:simplified-facilities-service-desk&#x60;, &#x60;com.atlassian.servicedesk:simplified-legal-service-desk&#x60;, &#x60;com.atlassian.servicedesk:simplified-analytics-service-desk&#x60;, &#x60;com.atlassian.servicedesk:simplified-marketing-service-desk&#x60;, &#x60;com.atlassian.servicedesk:simplified-design-service-desk&#x60;, &#x60;com.atlassian.servicedesk:simplified-sales-service-desk&#x60;, &#x60;com.atlassian.servicedesk:simplified-finance-service-desk&#x60; |   | &#x60;software&#x60; | &#x60;com.pyxis.greenhopper.jira:gh-simplified-agility-kanban&#x60;, &#x60;com.pyxis.greenhopper.jira:gh-simplified-agility-scrum&#x60;, &#x60;com.pyxis.greenhopper.jira:gh-simplified-basic&#x60;, &#x60;com.pyxis.greenhopper.jira:gh-simplified-kanban-classic&#x60;, &#x60;com.pyxis.greenhopper.jira:gh-simplified-scrum-classic&#x60; |   The project types are available according to the installed Jira features as follows:   *  Jira Core, the default, enables &#x60;business&#x60; projects.  *  Jira Service Management enables &#x60;service_desk&#x60; projects.  *  Jira Software enables &#x60;software&#x60; projects.  To determine which features are installed, go to **Jira settings** &gt; **Apps** &gt; **Manage apps** and review the System Apps list. To add Jira Software or Jira Service Management into a JIRA instance, use **Jira settings** &gt; **Apps** &gt; **Finding new apps**. For more information, see [ Managing add-ons](https://confluence.atlassian.com/x/S31NLg).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: The JSON representation of the project being created.
    :type body: dict | bytes

    """
    body = CreateProjectDetails.from_dict(body)
    return web.Response(status=200)


async def delete_project(request: web.Request, project_id_or_key, enable_undo=None) -> web.Response:
    """Delete project

    Deletes a project.  You can&#39;t delete a project if it&#39;s archived. To delete an archived project, restore the project and then delete it. To restore a project, use the Jira UI.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param enable_undo: Whether this project is placed in the Jira recycle bin where it will be available for restoration.
    :type enable_undo: bool

    """
    return web.Response(status=200)


async def delete_project_asynchronously(request: web.Request, project_id_or_key) -> web.Response:
    """Delete project asynchronously

    Deletes a project asynchronously.  This operation is:   *  transactional, that is, if part of the delete fails the project is not deleted.  *  [asynchronous](#async). Follow the &#x60;location&#x60; link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def get_all_projects(request: web.Request, expand=None, recent=None, properties=None) -> web.Response:
    """Get all projects

    Returns all projects visible to the user. Deprecated, use [ Get projects paginated](#api-rest-api-3-project-search-get) that supports search and pagination.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Projects are returned only where the user has *Browse Projects* or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:   *  &#x60;description&#x60; Returns the project description.  *  &#x60;issueTypes&#x60; Returns all issue types associated with the project.  *  &#x60;lead&#x60; Returns information about the project lead.  *  &#x60;projectKeys&#x60; Returns all project keys associated with the project.
    :type expand: str
    :param recent: Returns the user&#39;s most recently accessed projects. You may specify the number of results to return up to a maximum of 20. If access is anonymous, then the recently accessed projects are based on the current HTTP session.
    :type recent: int
    :param properties: A list of project properties to return for the project. This parameter accepts a comma-separated list.
    :type properties: List[str]

    """
    return web.Response(status=200)


async def get_all_statuses(request: web.Request, project_id_or_key) -> web.Response:
    """Get all statuses for project

    Returns the valid statuses for a project. The statuses are grouped by issue type, as each project has a set of valid issue types and each issue type has a set of valid statuses.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def get_hierarchy(request: web.Request, project_id) -> web.Response:
    """Get project issue type hierarchy

    Get the issue type hierarchy for a next-gen project.  The issue type hierarchy for a project consists of:   *  *Epic* at level 1 (optional).  *  One or more issue types at level 0 such as *Story*, *Task*, or *Bug*. Where the issue type *Epic* is defined, these issue types are used to break down the content of an epic.  *  *Subtask* at level -1 (optional). This issue type enables level 0 issue types to be broken down into components. Issues based on a level -1 issue type must have a parent issue.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param project_id: The ID of the project.
    :type project_id: int

    """
    return web.Response(status=200)


async def get_notification_scheme_for_project(request: web.Request, project_key_or_id, expand=None) -> web.Response:
    """Get project notification scheme

    Gets a [notification scheme](https://confluence.atlassian.com/x/8YdKLg) associated with the project. Deprecated, use [Get notification schemes paginated](#api-rest-api-3-notificationscheme-get) supporting search and pagination.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

    :param project_key_or_id: The project ID or project key (case sensitive).
    :type project_key_or_id: str
    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;all&#x60; Returns all expandable information  *  &#x60;field&#x60; Returns information about any custom fields assigned to receive an event  *  &#x60;group&#x60; Returns information about any groups assigned to receive an event  *  &#x60;notificationSchemeEvents&#x60; Returns a list of event associations. This list is returned for all expandable information  *  &#x60;projectRole&#x60; Returns information about any project roles assigned to receive an event  *  &#x60;user&#x60; Returns information about any users assigned to receive an event
    :type expand: str

    """
    return web.Response(status=200)


async def get_project(request: web.Request, project_id_or_key, expand=None, properties=None) -> web.Response:
    """Get project

    Returns the [project details](https://confluence.atlassian.com/x/ahLpNw) for a project.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that the project description, issue types, and project lead are included in all responses by default. Expand options include:   *  &#x60;description&#x60; The project description.  *  &#x60;issueTypes&#x60; The issue types associated with the project.  *  &#x60;lead&#x60; The project lead.  *  &#x60;projectKeys&#x60; All project keys associated with the project.  *  &#x60;issueTypeHierarchy&#x60; The project issue type hierarchy.
    :type expand: str
    :param properties: A list of project properties to return for the project. This parameter accepts a comma-separated list.
    :type properties: List[str]

    """
    return web.Response(status=200)


async def get_recent(request: web.Request, expand=None, properties=None) -> web.Response:
    """Get recent projects

    Returns a list of up to 20 projects recently viewed by the user that are still visible to the user.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Projects are returned only where the user has one of:   *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:   *  &#x60;description&#x60; Returns the project description.  *  &#x60;projectKeys&#x60; Returns all project keys associated with a project.  *  &#x60;lead&#x60; Returns information about the project lead.  *  &#x60;issueTypes&#x60; Returns all issue types associated with the project.  *  &#x60;url&#x60; Returns the URL associated with the project.  *  &#x60;permissions&#x60; Returns the permissions associated with the project.  *  &#x60;insight&#x60; EXPERIMENTAL. Returns the insight details of total issue count and last issue update time for the project.  *  &#x60;*&#x60; Returns the project with all available expand options.
    :type expand: str
    :param properties: EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list. Invalid property names are ignored.
    :type properties: List[]

    """
    return web.Response(status=200)


async def restore(request: web.Request, project_id_or_key) -> web.Response:
    """Restore deleted or archived project

    Restores a project that has been archived or placed in the Jira recycle bin.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def search_projects(request: web.Request, start_at=None, max_results=None, order_by=None, id=None, keys=None, query=None, type_key=None, category_id=None, action=None, expand=None, status=None, properties=None, property_query=None) -> web.Response:
    """Get projects paginated

    Returns a [paginated](#pagination) list of projects visible to the user.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Projects are returned only where the user has one of:   *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param order_by: [Order](#ordering) the results by a field.   *  &#x60;category&#x60; Sorts by project category. A complete list of category IDs is found using [Get all project categories](#api-rest-api-3-projectCategory-get).  *  &#x60;issueCount&#x60; Sorts by the total number of issues in each project.  *  &#x60;key&#x60; Sorts by project key.  *  &#x60;lastIssueUpdatedTime&#x60; Sorts by the last issue update time.  *  &#x60;name&#x60; Sorts by project name.  *  &#x60;owner&#x60; Sorts by project lead.  *  &#x60;archivedDate&#x60; EXPERIMENTAL. Sorts by project archived date.  *  &#x60;deletedDate&#x60; EXPERIMENTAL. Sorts by project deleted date.
    :type order_by: str
    :param id: The project IDs to filter the results by. To include multiple IDs, provide an ampersand-separated list. For example, &#x60;id&#x3D;10000&amp;id&#x3D;10001&#x60;. Up to 50 project IDs can be provided.
    :type id: List[int]
    :param keys: The project keys to filter the results by. To include multiple keys, provide an ampersand-separated list. For example, &#x60;keys&#x3D;PA&amp;keys&#x3D;PB&#x60;. Up to 50 project keys can be provided.
    :type keys: List[str]
    :param query: Filter the results using a literal string. Projects with a matching &#x60;key&#x60; or &#x60;name&#x60; are returned (case insensitive).
    :type query: str
    :param type_key: Orders results by the [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes). This parameter accepts a comma-separated list. Valid values are &#x60;business&#x60;, &#x60;service_desk&#x60;, and &#x60;software&#x60;.
    :type type_key: str
    :param category_id: The ID of the project&#39;s category. A complete list of category IDs is found using the [Get all project categories](#api-rest-api-3-projectCategory-get) operation.
    :type category_id: int
    :param action: Filter results by projects for which the user can:   *  &#x60;view&#x60; the project, meaning that they have one of the following permissions:           *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.      *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.      *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  &#x60;browse&#x60; the project, meaning that they have the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  &#x60;edit&#x60; the project, meaning that they have one of the following permissions:           *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.      *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
    :type action: str
    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include:   *  &#x60;description&#x60; Returns the project description.  *  &#x60;projectKeys&#x60; Returns all project keys associated with a project.  *  &#x60;lead&#x60; Returns information about the project lead.  *  &#x60;issueTypes&#x60; Returns all issue types associated with the project.  *  &#x60;url&#x60; Returns the URL associated with the project.  *  &#x60;insight&#x60; EXPERIMENTAL. Returns the insight details of total issue count and last issue update time for the project.
    :type expand: str
    :param status: EXPERIMENTAL. Filter results by project status:   *  &#x60;live&#x60; Search live projects.  *  &#x60;archived&#x60; Search archived projects.  *  &#x60;deleted&#x60; Search deleted projects, those in the recycle bin.
    :type status: List[str]
    :param properties: EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list.
    :type properties: List[]
    :param property_query: EXPERIMENTAL. A query string used to search properties. The query string cannot be specified using a JSON object. For example, to search for the value of &#x60;nested&#x60; from &#x60;{\&quot;something\&quot;:{\&quot;nested\&quot;:1,\&quot;other\&quot;:2}}&#x60; use &#x60;[thepropertykey].something.nested&#x3D;1&#x60;. Note that the propertyQuery key is enclosed in square brackets to enable searching where the propertyQuery key includes dot (.) or equals (&#x3D;) characters. Note that &#x60;thepropertykey&#x60; is only returned when included in &#x60;properties&#x60;.
    :type property_query: str

    """
    return web.Response(status=200)


async def update_project(request: web.Request, project_id_or_key, body, expand=None) -> web.Response:
    """Update project

    Updates the [project details](https://confluence.atlassian.com/x/ahLpNw) of a project.  All parameters are optional in the body of the request.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param body: The project details to be updated.
    :type body: dict | bytes
    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that the project description, issue types, and project lead are included in all responses by default. Expand options include:   *  &#x60;description&#x60; The project description.  *  &#x60;issueTypes&#x60; The issue types associated with the project.  *  &#x60;lead&#x60; The project lead.  *  &#x60;projectKeys&#x60; All project keys associated with the project.
    :type expand: str

    """
    body = UpdateProjectDetails.from_dict(body)
    return web.Response(status=200)


async def update_project_type(request: web.Request, project_id_or_key, new_project_type_key) -> web.Response:
    """Update project type

    Deprecated, this feature is no longer supported and no alternatives are available, see [Convert project to a different template or type](https://confluence.atlassian.com/x/yEKeOQ). Updates a [project type](https://confluence.atlassian.com/x/GwiiLQ). The project type can be updated for classic projects only, project type cannot be updated for next-gen projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param new_project_type_key: The key of the new project type.
    :type new_project_type_key: str

    """
    return web.Response(status=200)
