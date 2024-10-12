from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def tasks0_get(request: web.Request, api_key, filter_by_event_id=None, filter_by_general_tasks_only=None, filter_by_incomplete_only=None, filter_by_completed_only=None, filter_by_no_due_date=None, filter_by_due_date_greater_than_or_equal_to=None, filter_by_due_date_smaller_than_or_equal_to=None, filter_by_has_assignee=None, filter_by_assignee_user_id=None, filter_by_task_name_contains_text=None, filter_by_integration_metadata_field_1=None, filter_by_integration_metadata_field_2=None, filter_by_integration_metadata_field_3=None, filter_by_integration_metadata_field_4=None, filter_by_integration_metadata_field_5=None, hydrate_task_comments=None) -> web.Response:
    """tasks0_get

    Retrieve Tasks

    :param api_key: 
    :type api_key: str
    :param filter_by_event_id: Only include tasks from this given event.
    :type filter_by_event_id: 
    :param filter_by_general_tasks_only: Only include general tasks (tasks on the main task board that do not belong to a particular event). Note: this filter cannot be used in conjunction with the filter_by_event_id filter.
    :type filter_by_general_tasks_only: 
    :param filter_by_incomplete_only: If you pass in the value \&quot;true\&quot; for this parameter, the result will only include tasks that are NOT marked as Completed.
    :type filter_by_incomplete_only: str
    :param filter_by_completed_only: If you pass in the value \&quot;true\&quot; for this parameter, the result will only include tasks that are marked as Completed.
    :type filter_by_completed_only: str
    :param filter_by_no_due_date: If you pass in the value \&quot;true\&quot; for this parameter, the result will only include tasks that do not have a due date set.
    :type filter_by_no_due_date: str
    :param filter_by_due_date_greater_than_or_equal_to: Only include tasks that have a due date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD. Note: this filter cannot be used in conjunction with the filter_by_no_due_date filter.
    :type filter_by_due_date_greater_than_or_equal_to: str
    :param filter_by_due_date_smaller_than_or_equal_to: Only include tasks that have a due date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD. Note: this filter cannot be used in conjunction with the filter_by_no_due_date filter.
    :type filter_by_due_date_smaller_than_or_equal_to: str
    :param filter_by_has_assignee: Only include tasks that have an assignee. Unassigned tasks will get excluded.
    :type filter_by_has_assignee: str
    :param filter_by_assignee_user_id: Only include tasks that are assigned to this user. You can get a list of UserId&#39;s in your workspace from the /v1/references/users_and_resources endpoint. Note: If you want to retrieve the tasks that are unassigned, include this parameter and pass in the word \&quot;null\&quot; as the value for it.
    :type filter_by_assignee_user_id: str
    :param filter_by_task_name_contains_text: Only include tasks that have the given text in the task Name. For example: If you want to retrieve all the tasks that have the word “order” in the task Name field, pass in the value “order” for the filter_by_task_name_contains_text parameter. Note: this text search is not case-sensitive.
    :type filter_by_task_name_contains_text: str
    :param filter_by_integration_metadata_field_1: Only include tasks that have their integration_metadata_field_1 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField1 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with).
    :type filter_by_integration_metadata_field_1: str
    :param filter_by_integration_metadata_field_2: Only include tasks that have their integration_metadata_field_2 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField2 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with).
    :type filter_by_integration_metadata_field_2: str
    :param filter_by_integration_metadata_field_3: Only include tasks that have their integration_metadata_field_3 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField3 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with).
    :type filter_by_integration_metadata_field_3: str
    :param filter_by_integration_metadata_field_4: Only include tasks that have their integration_metadata_field_4 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField4 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with).
    :type filter_by_integration_metadata_field_4: str
    :param filter_by_integration_metadata_field_5: Only include tasks that have their integration_metadata_field_5 property equal to the value you pass in for this parameter. Note: A task&#39;s IntegrationMetadataField5 property is an integration-specific text field only accessible via the ExhibitDay API. This field is typically used to store metadata or information about a particular task (e.g., the \&quot;external id\&quot; of the task from another system you&#39;re integrating with).
    :type filter_by_integration_metadata_field_5: str
    :param hydrate_task_comments: Include the comments collection for each task in the result set. Note: hydrating the comments collection for each task in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the list of comments for each task in the result set.
    :type hydrate_task_comments: str

    """
    filter_by_due_date_greater_than_or_equal_to = util.deserialize_date(filter_by_due_date_greater_than_or_equal_to)
    filter_by_due_date_smaller_than_or_equal_to = util.deserialize_date(filter_by_due_date_smaller_than_or_equal_to)
    return web.Response(status=200)


async def tasks1_post(request: web.Request, api_key, name, event_id=None, task_section_id=None, is_completed=None, due_date=None, assignee_user_id=None, details=None, integration_metadata_field_1=None, integration_metadata_field_2=None, integration_metadata_field_3=None, integration_metadata_field_4=None, integration_metadata_field_5=None) -> web.Response:
    """tasks1_post

    Add a Task

    :param api_key: 
    :type api_key: str
    :param name: The name/short description of the task.
    :type name: str
    :param event_id: The id of the event you would like to add the task under. If this value is not provided, the task will be added as a general (non-event-specific) task in your workspace (under the main Task Board).
    :type event_id: 
    :param task_section_id: The id of the event task section that the task should be placed under. Leave this value blank if you don&#39;t want to place/categorize the task under a specific event task section. Note: you can get a list of available Task Section Ids for a given event using the /v1/event/info endpoint.
    :type task_section_id: 
    :param is_completed: Boolean representing whether or not the task has been completed.
    :type is_completed: str
    :param due_date: Task due date (format: YYYY-MM-DD).
    :type due_date: str
    :param assignee_user_id: The id of the user you would like to assign the task to. If you want the task to be unassigned, leave the value for this parameter blank. To get a list of all the user ids in your workspace, use the /v1/references/users_and_resources API endpoint. Users that can have tasks assigned to them will have their can_have_tasks_assigned property set to true.
    :type assignee_user_id: str
    :param details: The details/description of the task. Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag.
    :type details: str
    :param integration_metadata_field_1: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_1: str
    :param integration_metadata_field_2: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_2: str
    :param integration_metadata_field_3: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_3: str
    :param integration_metadata_field_4: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_4: str
    :param integration_metadata_field_5: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_5: str

    """
    due_date = util.deserialize_date(due_date)
    return web.Response(status=200)


async def tasks2_patch(request: web.Request, api_key, id, name=None, task_section_id=None, is_completed=None, due_date=None, assignee_user_id=None, details=None, integration_metadata_field_1=None, integration_metadata_field_2=None, integration_metadata_field_3=None, integration_metadata_field_4=None, integration_metadata_field_5=None) -> web.Response:
    """tasks2_patch

    Update a Task

    :param api_key: 
    :type api_key: str
    :param id: The Id of the task you would like to update.
    :type id: 
    :param name: The name/short description of the task.
    :type name: str
    :param task_section_id: The id of the event task section that the task should be placed under. If you don&#39;t want to place/categorize the task under a specific event task section, pass in the value  ull\&quot; for this parameter. Note: you can get a list of available Task Section Ids for a given event using the /v1/event/info endpoint.
    :type task_section_id: 
    :param is_completed: Boolean representing whether or not the task has been completed.
    :type is_completed: str
    :param due_date: Task due date (format: YYYY-MM-DD). If you don&#39;t want the task to have a due date, pass in the value \&quot;null\&quot; for this parameter.
    :type due_date: str
    :param assignee_user_id: The User Id of the user you would like to assign the task to. If you want the task to be unassigned, pass in the value \&quot;null\&quot; for this parameter. To get a list of all the User Ids in your workspace, use the /v1/references/users_and_resources API endpoint; users who can have tasks assigned to them will have their can_have_tasks_assigned property set to true.
    :type assignee_user_id: str
    :param details: The details/description of the task. Only accepts plain text. Any html tags in the value you pass in will be stripped. New line characters will get replaced with a &lt;br/&gt; tag.
    :type details: str
    :param integration_metadata_field_1: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_1: str
    :param integration_metadata_field_2: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_2: str
    :param integration_metadata_field_3: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_3: str
    :param integration_metadata_field_4: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_4: str
    :param integration_metadata_field_5: This is an integration-specific text field only accessible via the ExhibitDay API. This field can be used to store whatever metadata or information you&#39;d like about a particular task. For example, you can use it to store the \&quot;external id\&quot; of the task (from another system you&#39;re integrating with). Or, you can use it to store the last sync timestamp. Note: when you retrieve a list of tasks (using the /v1/tasks endpoint), you can filter down the results by the value of this field.
    :type integration_metadata_field_5: str

    """
    due_date = util.deserialize_date(due_date)
    return web.Response(status=200)


async def tasks3_delete(request: web.Request, api_key, id) -> web.Response:
    """tasks3_delete

    Delete a Task

    :param api_key: 
    :type api_key: str
    :param id: The id of the task you would like to delete.
    :type id: 

    """
    return web.Response(status=200)


async def tasks_comment0_get(request: web.Request, api_key, id) -> web.Response:
    """tasks_comment0_get

    Retrieve a Single Task Comment by id

    :param api_key: 
    :type api_key: str
    :param id: Id of the specific task comment that you would like to retrieve.
    :type id: 

    """
    return web.Response(status=200)


async def tasks_comment1_post(request: web.Request, api_key, task_id, comment) -> web.Response:
    """tasks_comment1_post

    Add a Comment to a Task

    :param api_key: 
    :type api_key: str
    :param task_id: The id of the task you would like to add the comment to.
    :type task_id: 
    :param comment: The text of comment you would like to add. Only accepts plain text. Any html tags in the value you pass in will be stripped.
    :type comment: str

    """
    return web.Response(status=200)


async def tasks_comment2_patch(request: web.Request, api_key, id, comment) -> web.Response:
    """tasks_comment2_patch

    Update a Task Comment

    :param api_key: 
    :type api_key: str
    :param id: The Id of the task comment you would like to update.
    :type id: 
    :param comment: The text that you would like to replace the existing comment with. Only accepts plain text. Any html tags in the value you pass in will be stripped.
    :type comment: str

    """
    return web.Response(status=200)


async def tasks_comment3_delete(request: web.Request, api_key, id) -> web.Response:
    """tasks_comment3_delete

    Delete a Task Comment

    :param api_key: 
    :type api_key: str
    :param id: The Id of the task comment you would like to delete.
    :type id: 

    """
    return web.Response(status=200)


async def tasks_comments0_get(request: web.Request, api_key, filter_by_event_id=None, filter_by_task_id=None, hydrate_task=None) -> web.Response:
    """tasks_comments0_get

    Retrieve Task Comments

    :param api_key: 
    :type api_key: str
    :param filter_by_event_id: Only include task comment for tasks from this given event.
    :type filter_by_event_id: 
    :param filter_by_task_id: Only include task comments for this specific task.
    :type filter_by_task_id: 
    :param hydrate_task: Include the task object for each task comment in the result set. Note: hydrating the task object for each task comment in the results will naturally yield a larger response size and response time. Set the value for this parameter to true only if you need to include the task object each comment in the result set.
    :type hydrate_task: str

    """
    return web.Response(status=200)


async def tasks_info0_get(request: web.Request, api_key, id) -> web.Response:
    """tasks_info0_get

    Retrieve a Single Task by id

    :param api_key: 
    :type api_key: str
    :param id: Id of the specific task that you would like to retrieve.
    :type id: 

    """
    return web.Response(status=200)
