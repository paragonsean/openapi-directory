from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_custom_field_setting_for_portfolio200_response import AddCustomFieldSettingForPortfolio200Response
from openapi_server.models.add_custom_field_setting_for_portfolio_request import AddCustomFieldSettingForPortfolioRequest
from openapi_server.models.add_followers_for_project_request import AddFollowersForProjectRequest
from openapi_server.models.add_members_for_portfolio_request import AddMembersForPortfolioRequest
from openapi_server.models.create_project201_response import CreateProject201Response
from openapi_server.models.create_project_request import CreateProjectRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.duplicate_project_request import DuplicateProjectRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_items_for_portfolio200_response import GetItemsForPortfolio200Response
from openapi_server.models.get_job200_response import GetJob200Response
from openapi_server.models.get_task_counts_for_project200_response import GetTaskCountsForProject200Response
from openapi_server.models.project_save_as_template_request import ProjectSaveAsTemplateRequest
from openapi_server.models.remove_custom_field_setting_for_portfolio_request import RemoveCustomFieldSettingForPortfolioRequest
from openapi_server.models.remove_followers_for_project_request import RemoveFollowersForProjectRequest
from openapi_server.models.remove_members_for_portfolio_request import RemoveMembersForPortfolioRequest
from openapi_server import util


async def add_custom_field_setting_for_project(request: web.Request, project_gid, body, opt_pretty=None) -> web.Response:
    """Add a custom field to a project

    Custom fields are associated with projects by way of custom field settings.  This method creates a setting for the project.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param body: Information about the custom field setting.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool

    """
    body = AddCustomFieldSettingForPortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def add_followers_for_project(request: web.Request, project_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Add followers to a project

    Adds the specified list of users as followers to the project. Followers are a subset of members who have opted in to receive \&quot;tasks added\&quot; notifications for a project. Therefore, if the users are not already members of the project, they will also become members as a result of this operation. Returns the updated project record.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param body: Information about the followers being added.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddFollowersForProjectRequest.from_dict(body)
    return web.Response(status=200)


async def add_members_for_project(request: web.Request, project_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Add users to a project

    Adds the specified list of users as members of the project. Note that a user being added as a member may also be added as a *follower* as a result of this operation. This is because the user&#39;s default notification settings (i.e., in the \&quot;Notifcations\&quot; tab of \&quot;My Profile Settings\&quot;) will override this endpoint&#39;s default behavior of setting \&quot;Tasks added\&quot; notifications to &#x60;false&#x60;. Returns the updated project record.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param body: Information about the members being added.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddMembersForPortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def create_project(request: web.Request, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Create a project

    Create a new project in a workspace or team.  Every project is required to be created in a specific workspace or organization, and this cannot be changed once set. Note that you can use the &#x60;workspace&#x60; parameter regardless of whether or not it is an organization.  If the workspace for your project is an organization, you must also supply a &#x60;team&#x60; to share the project with.  Returns the full record of the newly created project.

    :param body: The project to create.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreateProjectRequest.from_dict(body)
    return web.Response(status=200)


async def create_project_for_team(request: web.Request, team_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Create a project in a team

    Creates a project shared with the given team.  Returns the full record of the newly created project.

    :param team_gid: Globally unique identifier for the team.
    :type team_gid: str
    :param body: The new project to create.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreateProjectRequest.from_dict(body)
    return web.Response(status=200)


async def create_project_for_workspace(request: web.Request, workspace_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Create a project in a workspace

    Returns the compact project records for all projects in the workspace.  If the workspace for your project is an organization, you must also supply a team to share the project with.  Returns the full record of the newly created project.

    :param workspace_gid: Globally unique identifier for the workspace or organization.
    :type workspace_gid: str
    :param body: The new project to create.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreateProjectRequest.from_dict(body)
    return web.Response(status=200)


async def delete_project(request: web.Request, project_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Delete a project

    A specific, existing project can be deleted by making a DELETE request on the URL for that project.  Returns an empty data record.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def duplicate_project(request: web.Request, project_gid, opt_pretty=None, opt_fields=None, body=None) -> web.Response:
    """Duplicate a project

    Creates and returns a job that will asynchronously handle the duplication.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param body: Describes the duplicate&#39;s name and the elements that will be duplicated.
    :type body: dict | bytes

    """
    body = DuplicateProjectRequest.from_dict(body)
    return web.Response(status=200)


async def get_project(request: web.Request, project_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get a project

    Returns the complete project record for a single project.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_projects(request: web.Request, opt_pretty=None, opt_fields=None, limit=None, offset=None, workspace=None, team=None, archived=None) -> web.Response:
    """Get multiple projects

    Returns the compact project records for some filtered set of projects. Use one or more of the parameters provided to filter the projects returned. *Note: This endpoint may timeout for large domains. Try filtering by team!*

    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str
    :param workspace: The workspace or organization to filter projects on.
    :type workspace: str
    :param team: The team to filter projects on.
    :type team: str
    :param archived: Only return projects whose &#x60;archived&#x60; field takes on the value of this parameter.
    :type archived: bool

    """
    return web.Response(status=200)


async def get_projects_for_task(request: web.Request, task_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get projects a task is in

    Returns a compact representation of all of the projects the task is in.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str

    """
    return web.Response(status=200)


async def get_projects_for_team(request: web.Request, team_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None, archived=None) -> web.Response:
    """Get a team&#39;s projects

    Returns the compact project records for all projects in the team.

    :param team_gid: Globally unique identifier for the team.
    :type team_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str
    :param archived: Only return projects whose &#x60;archived&#x60; field takes on the value of this parameter.
    :type archived: bool

    """
    return web.Response(status=200)


async def get_projects_for_workspace(request: web.Request, workspace_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None, archived=None) -> web.Response:
    """Get all projects in a workspace

    Returns the compact project records for all projects in the workspace. *Note: This endpoint may timeout for large domains. Prefer the &#x60;/teams/{team_gid}/projects&#x60; endpoint.*

    :param workspace_gid: Globally unique identifier for the workspace or organization.
    :type workspace_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str
    :param archived: Only return projects whose &#x60;archived&#x60; field takes on the value of this parameter.
    :type archived: bool

    """
    return web.Response(status=200)


async def get_task_counts_for_project(request: web.Request, project_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get task count of a project

    Get an object that holds task count fields. **All fields are excluded by default**. You must [opt in](/docs/input-output-options) using &#x60;opt_fields&#x60; to get any information from this endpoint.  This endpoint has an additional [rate limit](/docs/standard-rate-limits) and each field counts especially high against our [cost limits](/docs/cost-limits).  Milestones are just tasks, so they are included in the &#x60;num_tasks&#x60;, &#x60;num_incomplete_tasks&#x60;, and &#x60;num_completed_tasks&#x60; counts.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str

    """
    return web.Response(status=200)


async def project_save_as_template(request: web.Request, project_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Create a project template from a project

    Creates and returns a job that will asynchronously handle the project template creation. Note that while the resulting project template can be accessed with the API, it won&#39;t be visible in the Asana UI until Project Templates 2.0 is launched in the app. See more in [this forum post](https://forum.asana.com/t/a-new-api-for-project-templates/156432).

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param body: Describes the inputs used for creating a project template, such as the resulting project template&#39;s name, which team it should be created in.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = ProjectSaveAsTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def remove_custom_field_setting_for_project(request: web.Request, project_gid, body, opt_pretty=None) -> web.Response:
    """Remove a custom field from a project

    Removes a custom field setting from a project.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param body: Information about the custom field setting being removed.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool

    """
    body = RemoveCustomFieldSettingForPortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def remove_followers_for_project(request: web.Request, project_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Remove followers from a project

    Removes the specified list of users from following the project, this will not affect project membership status. Returns the updated project record.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param body: Information about the followers being removed.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = RemoveFollowersForProjectRequest.from_dict(body)
    return web.Response(status=200)


async def remove_members_for_project(request: web.Request, project_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Remove users from a project

    Removes the specified list of users from members of the project. Returns the updated project record.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param body: Information about the members being removed.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = RemoveMembersForPortfolioRequest.from_dict(body)
    return web.Response(status=200)


async def update_project(request: web.Request, project_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Update a project

    A specific, existing project can be updated by making a PUT request on the URL for that project. Only the fields provided in the &#x60;data&#x60; block will be updated; any unspecified fields will remain unchanged.  When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the task.  Returns the complete updated project record.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param body: The updated fields for the project.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreateProjectRequest.from_dict(body)
    return web.Response(status=200)
