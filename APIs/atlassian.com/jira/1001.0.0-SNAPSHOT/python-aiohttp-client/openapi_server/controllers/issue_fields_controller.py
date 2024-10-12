from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_field_definition_json_bean import CustomFieldDefinitionJsonBean
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.field_details import FieldDetails
from openapi_server.models.page_bean_context import PageBeanContext
from openapi_server.models.page_bean_field import PageBeanField
from openapi_server.models.task_progress_bean_object import TaskProgressBeanObject
from openapi_server.models.update_custom_field_details import UpdateCustomFieldDetails
from openapi_server import util


async def create_custom_field(request: web.Request, body) -> web.Response:
    """Create custom field

    Creates a custom field.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: Definition of the custom field to be created
    :type body: dict | bytes

    """
    body = CustomFieldDefinitionJsonBean.from_dict(body)
    return web.Response(status=200)


async def delete_custom_field(request: web.Request, id) -> web.Response:
    """Delete custom field

    Deletes a custom field. The custom field is deleted whether it is in the trash or not. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom fields.  This operation is [asynchronous](#async). Follow the &#x60;location&#x60; link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of a custom field.
    :type id: str

    """
    return web.Response(status=200)


async def get_contexts_for_field_deprecated(request: web.Request, field_id, start_at=None, max_results=None) -> web.Response:
    """Get contexts for a field

    Returns a [paginated](#pagination) list of the contexts a field is used in. Deprecated, use [ Get custom field contexts](#api-rest-api-3-field-fieldId-context-get).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the field to return contexts for.
    :type field_id: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_fields(request: web.Request, ) -> web.Response:
    """Get fields

    Returns system and custom issue fields according to the following rules:   *  Fields that cannot be added to the issue navigator are always returned.  *  Fields that cannot be placed on an issue screen are always returned.  *  Fields that depend on global Jira settings are only returned if the setting is enabled. That is, timetracking fields, subtasks, votes, and watches.  *  For all other fields, this operation only returns the fields that the user has permission to view (that is, the field is used in at least one project that the user has *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.)  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.


    """
    return web.Response(status=200)


async def get_fields_paginated(request: web.Request, start_at=None, max_results=None, type=None, id=None, query=None, order_by=None, expand=None) -> web.Response:
    """Get fields paginated

    Returns a [paginated](#pagination) list of fields for Classic Jira projects. The list can include:   *  all fields  *  specific fields, by defining &#x60;id&#x60;  *  fields that contain a string in the field name or description, by defining &#x60;query&#x60;  *  specific fields that contain a string in the field name or description, by defining &#x60;id&#x60; and &#x60;query&#x60;  Only custom fields can be queried, &#x60;type&#x60; must be set to &#x60;custom&#x60;.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param type: The type of fields to search.
    :type type: List[str]
    :param id: The IDs of the custom fields to return or, where &#x60;query&#x60; is specified, filter.
    :type id: List[str]
    :param query: String used to perform a case-insensitive partial match with field names or descriptions.
    :type query: str
    :param order_by: [Order](#ordering) the results by a field:   *  &#x60;contextsCount&#x60; sorts by the number of contexts related to a field  *  &#x60;lastUsed&#x60; sorts by the date when the value of the field last changed  *  &#x60;name&#x60; sorts by the field name  *  &#x60;screensCount&#x60; sorts by the number of screens related to a field
    :type order_by: str
    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;key&#x60; returns the key for each field  *  &#x60;lastUsed&#x60; returns the date when the value of the field last changed  *  &#x60;screensCount&#x60; returns the number of screens related to a field  *  &#x60;contextsCount&#x60; returns the number of contexts related to a field  *  &#x60;isLocked&#x60; returns information about whether the field is [locked](https://confluence.atlassian.com/x/ZSN7Og)  *  &#x60;searcherKey&#x60; returns the searcher key for each custom field
    :type expand: str

    """
    return web.Response(status=200)


async def get_trashed_fields_paginated(request: web.Request, start_at=None, max_results=None, id=None, query=None, expand=None, order_by=None) -> web.Response:
    """Get fields in trash paginated

    Returns a [paginated](#pagination) list of fields in the trash. The list may be restricted to fields whose field name or description partially match a string.  Only custom fields can be queried, &#x60;type&#x60; must be set to &#x60;custom&#x60;.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param id: 
    :type id: List[str]
    :param query: String used to perform a case-insensitive partial match with field names or descriptions.
    :type query: str
    :param expand: 
    :type expand: str
    :param order_by: [Order](#ordering) the results by a field:   *  &#x60;name&#x60; sorts by the field name  *  &#x60;trashDate&#x60; sorts by the date the field was moved to the trash  *  &#x60;plannedDeletionDate&#x60; sorts by the planned deletion date
    :type order_by: str

    """
    return web.Response(status=200)


async def restore_custom_field(request: web.Request, id) -> web.Response:
    """Restore custom field from trash

    Restores a custom field from trash. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom fields.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of a custom field.
    :type id: str

    """
    return web.Response(status=200)


async def trash_custom_field(request: web.Request, id) -> web.Response:
    """Move custom field to trash

    Moves a custom field to trash. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom fields.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of a custom field.
    :type id: str

    """
    return web.Response(status=200)


async def update_custom_field(request: web.Request, field_id, body) -> web.Response:
    """Update custom field

    Updates a custom field.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param body: The custom field update details.
    :type body: dict | bytes

    """
    body = UpdateCustomFieldDetails.from_dict(body)
    return web.Response(status=200)
