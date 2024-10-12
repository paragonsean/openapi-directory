from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_custom_field_option_create_request import BulkCustomFieldOptionCreateRequest
from openapi_server.models.bulk_custom_field_option_update_request import BulkCustomFieldOptionUpdateRequest
from openapi_server.models.custom_field_created_context_options_list import CustomFieldCreatedContextOptionsList
from openapi_server.models.custom_field_option import CustomFieldOption
from openapi_server.models.custom_field_updated_context_options_list import CustomFieldUpdatedContextOptionsList
from openapi_server.models.order_of_custom_field_options import OrderOfCustomFieldOptions
from openapi_server.models.page_bean_custom_field_context_option import PageBeanCustomFieldContextOption
from openapi_server import util


async def create_custom_field_option(request: web.Request, field_id, context_id, body) -> web.Response:
    """Create custom field options (context)

    Creates options and, where the custom select field is of the type Select List (cascading), cascading options for a custom select field. The options are added to a context of the field.  The maximum number of options that can be created per request is 1000 and each field can have a maximum of 10000 options.  This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context.
    :type context_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = BulkCustomFieldOptionCreateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_custom_field_option(request: web.Request, field_id, context_id, option_id) -> web.Response:
    """Delete custom field options (context)

    Deletes a custom field option.  Options with cascading options cannot be deleted without deleting the cascading options first.  This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context from which an option should be deleted.
    :type context_id: int
    :param option_id: The ID of the option to delete.
    :type option_id: int

    """
    return web.Response(status=200)


async def get_custom_field_option(request: web.Request, id) -> web.Response:
    """Get custom field option

    Returns a custom field option. For example, an option in a select list.  Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** The custom field option is returned as follows:   *  if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the custom field is used in, and the field is visible in at least one layout the user has permission to view.

    :param id: The ID of the custom field option.
    :type id: str

    """
    return web.Response(status=200)


async def get_options_for_context(request: web.Request, field_id, context_id, option_id=None, only_options=None, start_at=None, max_results=None) -> web.Response:
    """Get custom field options (context)

    Returns a [paginated](#pagination) list of all custom field option for a context. Options are returned first then cascading options, in the order they display in Jira.  This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context.
    :type context_id: int
    :param option_id: The ID of the option.
    :type option_id: int
    :param only_options: Whether only options are returned.
    :type only_options: bool
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def reorder_custom_field_options(request: web.Request, field_id, context_id, body) -> web.Response:
    """Reorder custom field options (context)

    Changes the order of custom field options or cascading options in a context.  This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context.
    :type context_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = OrderOfCustomFieldOptions.from_dict(body)
    return web.Response(status=200)


async def update_custom_field_option(request: web.Request, field_id, context_id, body) -> web.Response:
    """Update custom field options (context)

    Updates the options of a custom field.  If any of the options are not found, no options are updated. Options where the values in the request match the current values aren&#39;t updated and aren&#39;t reported in the response.  Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context.
    :type context_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = BulkCustomFieldOptionUpdateRequest.from_dict(body)
    return web.Response(status=200)
