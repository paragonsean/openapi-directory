from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_dependencies_for_task_request import AddDependenciesForTaskRequest
from openapi_server.models.add_dependents_for_task_request import AddDependentsForTaskRequest
from openapi_server.models.add_followers_request import AddFollowersRequest
from openapi_server.models.add_project_for_task_request import AddProjectForTaskRequest
from openapi_server.models.add_tag_for_task_request import AddTagForTaskRequest
from openapi_server.models.create_task201_response import CreateTask201Response
from openapi_server.models.create_task_request import CreateTaskRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.duplicate_task_request import DuplicateTaskRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_job200_response import GetJob200Response
from openapi_server.models.get_tasks_for_project200_response import GetTasksForProject200Response
from openapi_server.models.remove_follower_for_task_request import RemoveFollowerForTaskRequest
from openapi_server.models.remove_project_for_task_request import RemoveProjectForTaskRequest
from openapi_server.models.remove_tag_for_task_request import RemoveTagForTaskRequest
from openapi_server.models.set_parent_for_task_request import SetParentForTaskRequest
from openapi_server import util


async def add_dependencies_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Set dependencies for a task

    Marks a set of tasks as dependencies of this task, if they are not already dependencies. *A task can have at most 30 dependents and dependencies combined*.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The list of tasks to set as dependencies.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddDependenciesForTaskRequest.from_dict(body)
    return web.Response(status=200)


async def add_dependents_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Set dependents for a task

    Marks a set of tasks as dependents of this task, if they are not already dependents. *A task can have at most 30 dependents and dependencies combined*.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The list of tasks to add as dependents.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddDependentsForTaskRequest.from_dict(body)
    return web.Response(status=200)


async def add_followers_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Add followers to a task

    Adds followers to a task. Returns an empty data block. Each task can be associated with zero or more followers in the system. Requests to add/remove followers, if successful, will return the complete updated task record, described above.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The followers to add to the task.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddFollowersRequest.from_dict(body)
    return web.Response(status=200)


async def add_project_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Add a project to a task

    Adds the task to the specified project, in the optional location specified. If no location arguments are given, the task will be added to the end of the project.  &#x60;addProject&#x60; can also be used to reorder a task within a project or section that already contains it.  At most one of &#x60;insert_before&#x60;, &#x60;insert_after&#x60;, or &#x60;section&#x60; should be specified. Inserting into a section in an non-order-dependent way can be done by specifying section, otherwise, to insert within a section in a particular place, specify &#x60;insert_before&#x60; or &#x60;insert_after&#x60; and a task within the section to anchor the position of this task.  Returns an empty data block.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The project to add the task to.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddProjectForTaskRequest.from_dict(body)
    return web.Response(status=200)


async def add_tag_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Add a tag to a task

    Adds a tag to a task. Returns an empty data block.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The tag to add to the task.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddTagForTaskRequest.from_dict(body)
    return web.Response(status=200)


async def create_subtask_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Create a subtask

    Creates a new subtask and adds it to the parent task. Returns the full record for the newly created subtask.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The new subtask to create.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreateTaskRequest.from_dict(body)
    return web.Response(status=200)


async def create_task(request: web.Request, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Create a task

    Creating a new task is as easy as POSTing to the &#x60;/tasks&#x60; endpoint with a data block containing the fields you’d like to set on the task. Any unspecified fields will take on default values.  Every task is required to be created in a specific workspace, and this workspace cannot be changed once set. The workspace need not be set explicitly if you specify &#x60;projects&#x60; or a &#x60;parent&#x60; task instead.

    :param body: The task to create.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreateTaskRequest.from_dict(body)
    return web.Response(status=200)


async def delete_task(request: web.Request, task_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Delete a task

    A specific, existing task can be deleted by making a DELETE request on the URL for that task. Deleted tasks go into the “trash” of the user making the delete request. Tasks can be recovered from the trash within a period of 30 days; afterward they are completely removed from the system.  Returns an empty data record.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def duplicate_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Duplicate a task

    Creates and returns a job that will asynchronously handle the duplication.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: Describes the duplicate&#39;s name and the fields that will be duplicated.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = DuplicateTaskRequest.from_dict(body)
    return web.Response(status=200)


async def get_dependencies_for_task(request: web.Request, task_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get dependencies from a task

    Returns the compact representations of all of the dependencies of a task.

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


async def get_dependents_for_task(request: web.Request, task_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get dependents from a task

    Returns the compact representations of all of the dependents of a task.

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


async def get_subtasks_for_task(request: web.Request, task_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get subtasks from a task

    Returns a compact representation of all of the subtasks of a task.

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


async def get_task(request: web.Request, task_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get a task

    Returns the complete task record for a single task.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_tasks(request: web.Request, opt_pretty=None, opt_fields=None, limit=None, offset=None, assignee=None, project=None, section=None, workspace=None, completed_since=None, modified_since=None) -> web.Response:
    """Get multiple tasks

    Returns the compact task records for some filtered set of tasks. Use one or more of the parameters provided to filter the tasks returned. You must specify a &#x60;project&#x60; or &#x60;tag&#x60; if you do not specify &#x60;assignee&#x60; and &#x60;workspace&#x60;.  For more complex task retrieval, use [workspaces/{workspace_gid}/tasks/search](/docs/search-tasks-in-a-workspace).

    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str
    :param assignee: The assignee to filter tasks on. If searching for unassigned tasks, assignee.any &#x3D; null can be specified. *Note: If you specify &#x60;assignee&#x60;, you must also specify the &#x60;workspace&#x60; to filter on.*
    :type assignee: str
    :param project: The project to filter tasks on.
    :type project: str
    :param section: The section to filter tasks on. *Note: Currently, this is only supported in board views.*
    :type section: str
    :param workspace: The workspace to filter tasks on. *Note: If you specify &#x60;workspace&#x60;, you must also specify the &#x60;assignee&#x60; to filter on.*
    :type workspace: str
    :param completed_since: Only return tasks that are either incomplete or that have been completed since this time.
    :type completed_since: str
    :param modified_since: Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.*
    :type modified_since: str

    """
    completed_since = util.deserialize_datetime(completed_since)
    modified_since = util.deserialize_datetime(modified_since)
    return web.Response(status=200)


async def get_tasks_for_project(request: web.Request, project_gid, completed_since=None, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get tasks from a project

    Returns the compact task records for all tasks within the given project, ordered by their priority within the project. Tasks can exist in more than one project at a time.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param completed_since: Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. 
    :type completed_since: str
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


async def get_tasks_for_section(request: web.Request, section_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get tasks from a section

    *Board view only*: Returns the compact section records for all tasks within the given section.

    :param section_gid: The globally unique identifier for the section.
    :type section_gid: str
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


async def get_tasks_for_tag(request: web.Request, tag_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get tasks from a tag

    Returns the compact task records for all tasks with the given tag. Tasks can have more than one tag at a time.

    :param tag_gid: Globally unique identifier for the tag.
    :type tag_gid: str
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


async def get_tasks_for_user_task_list(request: web.Request, user_task_list_gid, completed_since=None, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get tasks from a user task list

    Returns the compact list of tasks in a user’s My Tasks list. *Note: Access control is enforced for this endpoint as with all Asana API endpoints, meaning a user’s private tasks will be filtered out if the API-authenticated user does not have access to them.* *Note: Both complete and incomplete tasks are returned by default unless they are filtered out (for example, setting &#x60;completed_since&#x3D;now&#x60; will return only incomplete tasks, which is the default view for “My Tasks” in Asana.)*

    :param user_task_list_gid: Globally unique identifier for the user task list.
    :type user_task_list_gid: str
    :param completed_since: Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. 
    :type completed_since: str
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


async def remove_dependencies_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Unlink dependencies from a task

    Unlinks a set of dependencies from this task.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The list of tasks to unlink as dependencies.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddDependenciesForTaskRequest.from_dict(body)
    return web.Response(status=200)


async def remove_dependents_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Unlink dependents from a task

    Unlinks a set of dependents from this task.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The list of tasks to remove as dependents.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddDependentsForTaskRequest.from_dict(body)
    return web.Response(status=200)


async def remove_follower_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Remove followers from a task

    Removes each of the specified followers from the task if they are following. Returns the complete, updated record for the affected task.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The followers to remove from the task.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = RemoveFollowerForTaskRequest.from_dict(body)
    return web.Response(status=200)


async def remove_project_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Remove a project from a task

    Removes the task from the specified project. The task will still exist in the system, but it will not be in the project anymore.  Returns an empty data block.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The project to remove the task from.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = RemoveProjectForTaskRequest.from_dict(body)
    return web.Response(status=200)


async def remove_tag_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Remove a tag from a task

    Removes a tag from a task. Returns an empty data block.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The tag to remove from the task.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = RemoveTagForTaskRequest.from_dict(body)
    return web.Response(status=200)


async def search_tasks_for_workspace(request: web.Request, workspace_gid, opt_pretty=None, opt_fields=None, text=None, resource_subtype=None, assignee_any=None, assignee_not=None, portfolios_any=None, projects_any=None, projects_not=None, projects_all=None, sections_any=None, sections_not=None, sections_all=None, tags_any=None, tags_not=None, tags_all=None, teams_any=None, followers_not=None, created_by_any=None, created_by_not=None, assigned_by_any=None, assigned_by_not=None, liked_by_not=None, commented_on_by_not=None, due_on_before=None, due_on_after=None, due_on=None, due_at_before=None, due_at_after=None, start_on_before=None, start_on_after=None, start_on=None, created_on_before=None, created_on_after=None, created_on=None, created_at_before=None, created_at_after=None, completed_on_before=None, completed_on_after=None, completed_on=None, completed_at_before=None, completed_at_after=None, modified_on_before=None, modified_on_after=None, modified_on=None, modified_at_before=None, modified_at_after=None, is_blocking=None, is_blocked=None, has_attachment=None, completed=None, is_subtask=None, sort_by=None, sort_ascending=None) -> web.Response:
    """Search tasks in a workspace

    To mirror the functionality of the Asana web app&#39;s advanced search feature, the Asana API has a task search endpoint that allows you to build complex filters to find and retrieve the exact data you need. #### Premium access Like the Asana web product&#39;s advance search feature, this search endpoint will only be available to premium Asana users. A user is premium if any of the following is true:  - The workspace in which the search is being performed is a premium workspace - The user is a member of a premium team inside the workspace  Even if a user is only a member of a premium team inside a non-premium workspace, search will allow them to find data anywhere in the workspace, not just inside the premium team. Making a search request using credentials of a non-premium user will result in a &#x60;402 Payment Required&#x60; error. #### Pagination Search results are not stable; repeating the same query multiple times may return the data in a different order, even if the data do not change. Because of this, the traditional [pagination](https://developers.asana.com/docs/#pagination) available elsewhere in the Asana API is not available here. However, you can paginate manually by sorting the search results by their creation time and then modifying each subsequent query to exclude data you have already seen. Page sizes are limited to a maximum of 100 items, and can be specified by the &#x60;limit&#x60; query parameter. #### Eventual consistency Changes in Asana (regardless of whether they’re made though the web product or the API) are forwarded to our search infrastructure to be indexed. This process can take between 10 and 60 seconds to complete under normal operation, and longer during some production incidents. Making a change to a task that would alter its presence in a particular search query will not be reflected immediately. This is also true of the advanced search feature in the web product. #### Rate limits You may receive a &#x60;429 Too Many Requests&#x60; response if you hit any of our [rate limits](https://developers.asana.com/docs/#rate-limits). #### Custom field parameters | Parameter name | Custom field type | Accepted type | |---|---|---| | custom_fields.{gid}.is_set | All | Boolean | | custom_fields.{gid}.value | Text | String | | custom_fields.{gid}.value | Number | Number | | custom_fields.{gid}.value | Enum | Enum option ID | | custom_fields.{gid}.starts_with | Text only | String | | custom_fields.{gid}.ends_with | Text only | String | | custom_fields.{gid}.contains | Text only | String | | custom_fields.{gid}.less_than | Number only | Number | | custom_fields.{gid}.greater_than | Number only | Number |   For example, if the gid of the custom field is 12345, these query parameter to find tasks where it is set would be &#x60;custom_fields.12345.is_set&#x3D;true&#x60;. To match an exact value for an enum custom field, use the gid of the desired enum option and not the name of the enum option: &#x60;custom_fields.12345.value&#x3D;67890&#x60;.  **Not Supported**: searching for multiple exact matches of a custom field, searching for multi-enum custom field  *Note: If you specify &#x60;projects.any&#x60; and &#x60;sections.any&#x60;, you will receive tasks for the project **and** tasks for the section. If you&#39;re looking for only tasks in a section, omit the &#x60;projects.any&#x60; from the request.*

    :param workspace_gid: Globally unique identifier for the workspace or organization.
    :type workspace_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param text: Performs full-text search on both task name and description
    :type text: str
    :param resource_subtype: Filters results by the task&#39;s resource_subtype
    :type resource_subtype: str
    :param assignee_any: Comma-separated list of user identifiers
    :type assignee_any: str
    :param assignee_not: Comma-separated list of user identifiers
    :type assignee_not: str
    :param portfolios_any: Comma-separated list of portfolio IDs
    :type portfolios_any: str
    :param projects_any: Comma-separated list of project IDs
    :type projects_any: str
    :param projects_not: Comma-separated list of project IDs
    :type projects_not: str
    :param projects_all: Comma-separated list of project IDs
    :type projects_all: str
    :param sections_any: Comma-separated list of section or column IDs
    :type sections_any: str
    :param sections_not: Comma-separated list of section or column IDs
    :type sections_not: str
    :param sections_all: Comma-separated list of section or column IDs
    :type sections_all: str
    :param tags_any: Comma-separated list of tag IDs
    :type tags_any: str
    :param tags_not: Comma-separated list of tag IDs
    :type tags_not: str
    :param tags_all: Comma-separated list of tag IDs
    :type tags_all: str
    :param teams_any: Comma-separated list of team IDs
    :type teams_any: str
    :param followers_not: Comma-separated list of user identifiers
    :type followers_not: str
    :param created_by_any: Comma-separated list of user identifiers
    :type created_by_any: str
    :param created_by_not: Comma-separated list of user identifiers
    :type created_by_not: str
    :param assigned_by_any: Comma-separated list of user identifiers
    :type assigned_by_any: str
    :param assigned_by_not: Comma-separated list of user identifiers
    :type assigned_by_not: str
    :param liked_by_not: Comma-separated list of user identifiers
    :type liked_by_not: str
    :param commented_on_by_not: Comma-separated list of user identifiers
    :type commented_on_by_not: str
    :param due_on_before: ISO 8601 date string
    :type due_on_before: str
    :param due_on_after: ISO 8601 date string
    :type due_on_after: str
    :param due_on: ISO 8601 date string or &#x60;null&#x60;
    :type due_on: str
    :param due_at_before: ISO 8601 datetime string
    :type due_at_before: str
    :param due_at_after: ISO 8601 datetime string
    :type due_at_after: str
    :param start_on_before: ISO 8601 date string
    :type start_on_before: str
    :param start_on_after: ISO 8601 date string
    :type start_on_after: str
    :param start_on: ISO 8601 date string or &#x60;null&#x60;
    :type start_on: str
    :param created_on_before: ISO 8601 date string
    :type created_on_before: str
    :param created_on_after: ISO 8601 date string
    :type created_on_after: str
    :param created_on: ISO 8601 date string or &#x60;null&#x60;
    :type created_on: str
    :param created_at_before: ISO 8601 datetime string
    :type created_at_before: str
    :param created_at_after: ISO 8601 datetime string
    :type created_at_after: str
    :param completed_on_before: ISO 8601 date string
    :type completed_on_before: str
    :param completed_on_after: ISO 8601 date string
    :type completed_on_after: str
    :param completed_on: ISO 8601 date string or &#x60;null&#x60;
    :type completed_on: str
    :param completed_at_before: ISO 8601 datetime string
    :type completed_at_before: str
    :param completed_at_after: ISO 8601 datetime string
    :type completed_at_after: str
    :param modified_on_before: ISO 8601 date string
    :type modified_on_before: str
    :param modified_on_after: ISO 8601 date string
    :type modified_on_after: str
    :param modified_on: ISO 8601 date string or &#x60;null&#x60;
    :type modified_on: str
    :param modified_at_before: ISO 8601 datetime string
    :type modified_at_before: str
    :param modified_at_after: ISO 8601 datetime string
    :type modified_at_after: str
    :param is_blocking: Filter to incomplete tasks with dependents
    :type is_blocking: bool
    :param is_blocked: Filter to tasks with incomplete dependencies
    :type is_blocked: bool
    :param has_attachment: Filter to tasks with attachments
    :type has_attachment: bool
    :param completed: Filter to completed tasks
    :type completed: bool
    :param is_subtask: Filter to subtasks
    :type is_subtask: bool
    :param sort_by: One of &#x60;due_date&#x60;, &#x60;created_at&#x60;, &#x60;completed_at&#x60;, &#x60;likes&#x60;, or &#x60;modified_at&#x60;, defaults to &#x60;modified_at&#x60;
    :type sort_by: str
    :param sort_ascending: Default &#x60;false&#x60;
    :type sort_ascending: bool

    """
    due_on_before = util.deserialize_date(due_on_before)
    due_on_after = util.deserialize_date(due_on_after)
    due_on = util.deserialize_date(due_on)
    due_at_before = util.deserialize_datetime(due_at_before)
    due_at_after = util.deserialize_datetime(due_at_after)
    start_on_before = util.deserialize_date(start_on_before)
    start_on_after = util.deserialize_date(start_on_after)
    start_on = util.deserialize_date(start_on)
    created_on_before = util.deserialize_date(created_on_before)
    created_on_after = util.deserialize_date(created_on_after)
    created_on = util.deserialize_date(created_on)
    created_at_before = util.deserialize_datetime(created_at_before)
    created_at_after = util.deserialize_datetime(created_at_after)
    completed_on_before = util.deserialize_date(completed_on_before)
    completed_on_after = util.deserialize_date(completed_on_after)
    completed_on = util.deserialize_date(completed_on)
    completed_at_before = util.deserialize_datetime(completed_at_before)
    completed_at_after = util.deserialize_datetime(completed_at_after)
    modified_on_before = util.deserialize_date(modified_on_before)
    modified_on_after = util.deserialize_date(modified_on_after)
    modified_on = util.deserialize_date(modified_on)
    modified_at_before = util.deserialize_datetime(modified_at_before)
    modified_at_after = util.deserialize_datetime(modified_at_after)
    return web.Response(status=200)


async def set_parent_for_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Set the parent of a task

    parent, or no parent task at all. Returns an empty data block. When using &#x60;insert_before&#x60; and &#x60;insert_after&#x60;, at most one of those two options can be specified, and they must already be subtasks of the parent.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The new parent of the subtask.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = SetParentForTaskRequest.from_dict(body)
    return web.Response(status=200)


async def update_task(request: web.Request, task_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Update a task

    A specific, existing task can be updated by making a PUT request on the URL for that task. Only the fields provided in the &#x60;data&#x60; block will be updated; any unspecified fields will remain unchanged.  When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the task.  Returns the complete updated task record.

    :param task_gid: The task to operate on.
    :type task_gid: str
    :param body: The task to update.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreateTaskRequest.from_dict(body)
    return web.Response(status=200)
