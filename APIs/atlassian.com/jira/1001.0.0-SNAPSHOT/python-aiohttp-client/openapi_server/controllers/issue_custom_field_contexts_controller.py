from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_custom_field_context import CreateCustomFieldContext
from openapi_server.models.custom_field_context_default_value_update import CustomFieldContextDefaultValueUpdate
from openapi_server.models.custom_field_context_update_details import CustomFieldContextUpdateDetails
from openapi_server.models.issue_type_ids import IssueTypeIds
from openapi_server.models.page_bean_context_for_project_and_issue_type import PageBeanContextForProjectAndIssueType
from openapi_server.models.page_bean_custom_field_context import PageBeanCustomFieldContext
from openapi_server.models.page_bean_custom_field_context_default_value import PageBeanCustomFieldContextDefaultValue
from openapi_server.models.page_bean_custom_field_context_project_mapping import PageBeanCustomFieldContextProjectMapping
from openapi_server.models.page_bean_issue_type_to_context_mapping import PageBeanIssueTypeToContextMapping
from openapi_server.models.project_ids import ProjectIds
from openapi_server.models.project_issue_type_mappings import ProjectIssueTypeMappings
from openapi_server import util


async def add_issue_types_to_context(request: web.Request, field_id, context_id, body) -> web.Response:
    """Add issue types to context

    Adds issue types to a custom field context, appending the issue types to the issue types list.  A custom field context without any issue types applies to all issue types. Adding issue types to such a custom field context would result in it applying to only the listed issue types.  If any of the issue types exists in the custom field context, the operation fails and no issue types are added.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context.
    :type context_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssueTypeIds.from_dict(body)
    return web.Response(status=200)


async def assign_projects_to_custom_field_context(request: web.Request, field_id, context_id, body) -> web.Response:
    """Assign custom field context to projects

    Assigns a custom field context to projects.  If any project in the request is assigned to any context of the custom field, the operation fails.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context.
    :type context_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectIds.from_dict(body)
    return web.Response(status=200)


async def create_custom_field_context(request: web.Request, field_id, body) -> web.Response:
    """Create custom field context

    Creates a custom field context.  If &#x60;projectIds&#x60; is empty, a global context is created. A global context is one that applies to all project. If &#x60;issueTypeIds&#x60; is empty, the context applies to all issue types.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCustomFieldContext.from_dict(body)
    return web.Response(status=200)


async def delete_custom_field_context(request: web.Request, field_id, context_id) -> web.Response:
    """Delete custom field context

    Deletes a [ custom field context](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context.
    :type context_id: int

    """
    return web.Response(status=200)


async def get_contexts_for_field(request: web.Request, field_id, is_any_issue_type=None, is_global_context=None, context_id=None, start_at=None, max_results=None) -> web.Response:
    """Get custom field contexts

    Returns a [paginated](#pagination) list of [ contexts](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html) for a custom field. Contexts can be returned as follows:   *  With no other parameters set, all contexts.  *  By defining &#x60;id&#x60; only, all contexts from the list of IDs.  *  By defining &#x60;isAnyIssueType&#x60;, limit the list of contexts returned to either those that apply to all issue types (true) or those that apply to only a subset of issue types (false)  *  By defining &#x60;isGlobalContext&#x60;, limit the list of contexts return to either those that apply to all projects (global contexts) (true) or those that apply to only a subset of projects (false).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param is_any_issue_type: Whether to return contexts that apply to all issue types.
    :type is_any_issue_type: bool
    :param is_global_context: Whether to return contexts that apply to all projects.
    :type is_global_context: bool
    :param context_id: The list of context IDs. To include multiple contexts, separate IDs with ampersand: &#x60;contextId&#x3D;10000&amp;contextId&#x3D;10001&#x60;.
    :type context_id: List[int]
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_custom_field_contexts_for_projects_and_issue_types(request: web.Request, field_id, body, start_at=None, max_results=None) -> web.Response:
    """Get custom field contexts for projects and issue types

    Returns a [paginated](#pagination) list of project and issue type mappings and, for each mapping, the ID of a [custom field context](https://confluence.atlassian.com/x/k44fOw) that applies to the project and issue type.  If there is no custom field context assigned to the project then, if present, the custom field context that applies to all projects is returned if it also applies to the issue type or all issue types. If a custom field context is not found, the returned custom field context ID is &#x60;null&#x60;.  Duplicate project and issue type mappings cannot be provided in the request.  The order of the returned values is the same as provided in the request.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param body: The list of project and issue type mappings.
    :type body: dict | bytes
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    body = ProjectIssueTypeMappings.from_dict(body)
    return web.Response(status=200)


async def get_default_values(request: web.Request, field_id, context_id=None, start_at=None, max_results=None) -> web.Response:
    """Get custom field contexts default values

    Returns a [paginated](#pagination) list of defaults for a custom field. The results can be filtered by &#x60;contextId&#x60;, otherwise all values are returned. If no defaults are set for a context, nothing is returned.   The returned object depends on type of the custom field:   *  &#x60;CustomFieldContextDefaultValueDate&#x60; (type &#x60;datepicker&#x60;) for date fields.  *  &#x60;CustomFieldContextDefaultValueDateTime&#x60; (type &#x60;datetimepicker&#x60;) for date-time fields.  *  &#x60;CustomFieldContextDefaultValueSingleOption&#x60; (type &#x60;option.single&#x60;) for single choice select lists and radio buttons.  *  &#x60;CustomFieldContextDefaultValueMultipleOption&#x60; (type &#x60;option.multiple&#x60;) for multiple choice select lists and checkboxes.  *  &#x60;CustomFieldContextDefaultValueCascadingOption&#x60; (type &#x60;option.cascading&#x60;) for cascading select lists.  *  &#x60;CustomFieldContextSingleUserPickerDefaults&#x60; (type &#x60;single.user.select&#x60;) for single users.  *  &#x60;CustomFieldContextDefaultValueMultiUserPicker&#x60; (type &#x60;multi.user.select&#x60;) for user lists.  *  &#x60;CustomFieldContextDefaultValueSingleGroupPicker&#x60; (type &#x60;grouppicker.single&#x60;) for single choice group pickers.  *  &#x60;CustomFieldContextDefaultValueMultipleGroupPicker&#x60; (type &#x60;grouppicker.multiple&#x60;) for multiple choice group pickers.  *  &#x60;CustomFieldContextDefaultValueURL&#x60; (type &#x60;url&#x60;) for URLs.  *  &#x60;CustomFieldContextDefaultValueProject&#x60; (type &#x60;project&#x60;) for project pickers.  *  &#x60;CustomFieldContextDefaultValueFloat&#x60; (type &#x60;float&#x60;) for floats (floating-point numbers).  *  &#x60;CustomFieldContextDefaultValueLabels&#x60; (type &#x60;labels&#x60;) for labels.  *  &#x60;CustomFieldContextDefaultValueTextField&#x60; (type &#x60;textfield&#x60;) for text fields.  *  &#x60;CustomFieldContextDefaultValueTextArea&#x60; (type &#x60;textarea&#x60;) for text area fields.  *  &#x60;CustomFieldContextDefaultValueReadOnly&#x60; (type &#x60;readonly&#x60;) for read only (text) fields.  *  &#x60;CustomFieldContextDefaultValueMultipleVersion&#x60; (type &#x60;version.multiple&#x60;) for single choice version pickers.  *  &#x60;CustomFieldContextDefaultValueSingleVersion&#x60; (type &#x60;version.single&#x60;) for multiple choice version pickers.  Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/#data-types) are also supported, returning:   *  &#x60;CustomFieldContextDefaultValueForgeStringFieldBean&#x60; (type &#x60;forge.string&#x60;) for Forge string fields.  *  &#x60;CustomFieldContextDefaultValueForgeMultiStringFieldBean&#x60; (type &#x60;forge.string.list&#x60;) for Forge string collection fields.  *  &#x60;CustomFieldContextDefaultValueForgeObjectFieldBean&#x60; (type &#x60;forge.object&#x60;) for Forge object fields.  *  &#x60;CustomFieldContextDefaultValueForgeDateTimeFieldBean&#x60; (type &#x60;forge.datetime&#x60;) for Forge date-time fields.  *  &#x60;CustomFieldContextDefaultValueForgeGroupFieldBean&#x60; (type &#x60;forge.group&#x60;) for Forge group fields.  *  &#x60;CustomFieldContextDefaultValueForgeMultiGroupFieldBean&#x60; (type &#x60;forge.group.list&#x60;) for Forge group collection fields.  *  &#x60;CustomFieldContextDefaultValueForgeNumberFieldBean&#x60; (type &#x60;forge.number&#x60;) for Forge number fields.  *  &#x60;CustomFieldContextDefaultValueForgeUserFieldBean&#x60; (type &#x60;forge.user&#x60;) for Forge user fields.  *  &#x60;CustomFieldContextDefaultValueForgeMultiUserFieldBean&#x60; (type &#x60;forge.user.list&#x60;) for Forge user collection fields.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field, for example &#x60;customfield\\_10000&#x60;.
    :type field_id: str
    :param context_id: The IDs of the contexts.
    :type context_id: List[int]
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_issue_type_mappings_for_contexts(request: web.Request, field_id, context_id=None, start_at=None, max_results=None) -> web.Response:
    """Get issue types for custom field context

    Returns a [paginated](#pagination) list of context to issue type mappings for a custom field. Mappings are returned for all contexts or a list of contexts. Mappings are ordered first by context ID and then by issue type ID.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context. To include multiple contexts, provide an ampersand-separated list. For example, &#x60;contextId&#x3D;10001&amp;contextId&#x3D;10002&#x60;.
    :type context_id: List[int]
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_project_context_mapping(request: web.Request, field_id, context_id=None, start_at=None, max_results=None) -> web.Response:
    """Get project mappings for custom field context

    Returns a [paginated](#pagination) list of context to project mappings for a custom field. The result can be filtered by &#x60;contextId&#x60;. Otherwise, all mappings are returned. Invalid IDs are ignored.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field, for example &#x60;customfield\\_10000&#x60;.
    :type field_id: str
    :param context_id: The list of context IDs. To include multiple context, separate IDs with ampersand: &#x60;contextId&#x3D;10000&amp;contextId&#x3D;10001&#x60;.
    :type context_id: List[int]
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def remove_custom_field_context_from_projects(request: web.Request, field_id, context_id, body) -> web.Response:
    """Remove custom field context from projects

    Removes a custom field context from projects.  A custom field context without any projects applies to all projects. Removing all projects from a custom field context would result in it applying to all projects.  If any project in the request is not assigned to the context, or the operation would result in two global contexts for the field, the operation fails.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context.
    :type context_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectIds.from_dict(body)
    return web.Response(status=200)


async def remove_issue_types_from_context(request: web.Request, field_id, context_id, body) -> web.Response:
    """Remove issue types from context

    Removes issue types from a custom field context.  A custom field context without any issue types applies to all issue types.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context.
    :type context_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = IssueTypeIds.from_dict(body)
    return web.Response(status=200)


async def set_default_values(request: web.Request, field_id, body) -> web.Response:
    """Set custom field contexts default values

    Sets default for contexts of a custom field. Default are defined using these objects:   *  &#x60;CustomFieldContextDefaultValueDate&#x60; (type &#x60;datepicker&#x60;) for date fields.  *  &#x60;CustomFieldContextDefaultValueDateTime&#x60; (type &#x60;datetimepicker&#x60;) for date-time fields.  *  &#x60;CustomFieldContextDefaultValueSingleOption&#x60; (type &#x60;option.single&#x60;) for single choice select lists and radio buttons.  *  &#x60;CustomFieldContextDefaultValueMultipleOption&#x60; (type &#x60;option.multiple&#x60;) for multiple choice select lists and checkboxes.  *  &#x60;CustomFieldContextDefaultValueCascadingOption&#x60; (type &#x60;option.cascading&#x60;) for cascading select lists.  *  &#x60;CustomFieldContextSingleUserPickerDefaults&#x60; (type &#x60;single.user.select&#x60;) for single users.  *  &#x60;CustomFieldContextDefaultValueMultiUserPicker&#x60; (type &#x60;multi.user.select&#x60;) for user lists.  *  &#x60;CustomFieldContextDefaultValueSingleGroupPicker&#x60; (type &#x60;grouppicker.single&#x60;) for single choice group pickers.  *  &#x60;CustomFieldContextDefaultValueMultipleGroupPicker&#x60; (type &#x60;grouppicker.multiple&#x60;) for multiple choice group pickers.  *  &#x60;CustomFieldContextDefaultValueURL&#x60; (type &#x60;url&#x60;) for URLs.  *  &#x60;CustomFieldContextDefaultValueProject&#x60; (type &#x60;project&#x60;) for project pickers.  *  &#x60;CustomFieldContextDefaultValueFloat&#x60; (type &#x60;float&#x60;) for floats (floating-point numbers).  *  &#x60;CustomFieldContextDefaultValueLabels&#x60; (type &#x60;labels&#x60;) for labels.  *  &#x60;CustomFieldContextDefaultValueTextField&#x60; (type &#x60;textfield&#x60;) for text fields.  *  &#x60;CustomFieldContextDefaultValueTextArea&#x60; (type &#x60;textarea&#x60;) for text area fields.  *  &#x60;CustomFieldContextDefaultValueReadOnly&#x60; (type &#x60;readonly&#x60;) for read only (text) fields.  *  &#x60;CustomFieldContextDefaultValueMultipleVersion&#x60; (type &#x60;version.multiple&#x60;) for single choice version pickers.  *  &#x60;CustomFieldContextDefaultValueSingleVersion&#x60; (type &#x60;version.single&#x60;) for multiple choice version pickers.  Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/#data-types) are also supported, returning:   *  &#x60;CustomFieldContextDefaultValueForgeStringFieldBean&#x60; (type &#x60;forge.string&#x60;) for Forge string fields.  *  &#x60;CustomFieldContextDefaultValueForgeMultiStringFieldBean&#x60; (type &#x60;forge.string.list&#x60;) for Forge string collection fields.  *  &#x60;CustomFieldContextDefaultValueForgeObjectFieldBean&#x60; (type &#x60;forge.object&#x60;) for Forge object fields.  *  &#x60;CustomFieldContextDefaultValueForgeDateTimeFieldBean&#x60; (type &#x60;forge.datetime&#x60;) for Forge date-time fields.  *  &#x60;CustomFieldContextDefaultValueForgeGroupFieldBean&#x60; (type &#x60;forge.group&#x60;) for Forge group fields.  *  &#x60;CustomFieldContextDefaultValueForgeMultiGroupFieldBean&#x60; (type &#x60;forge.group.list&#x60;) for Forge group collection fields.  *  &#x60;CustomFieldContextDefaultValueForgeNumberFieldBean&#x60; (type &#x60;forge.number&#x60;) for Forge number fields.  *  &#x60;CustomFieldContextDefaultValueForgeUserFieldBean&#x60; (type &#x60;forge.user&#x60;) for Forge user fields.  *  &#x60;CustomFieldContextDefaultValueForgeMultiUserFieldBean&#x60; (type &#x60;forge.user.list&#x60;) for Forge user collection fields.  Only one type of default object can be included in a request. To remove a default for a context, set the default parameter to &#x60;null&#x60;.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CustomFieldContextDefaultValueUpdate.from_dict(body)
    return web.Response(status=200)


async def update_custom_field_context(request: web.Request, field_id, context_id, body) -> web.Response:
    """Update custom field context

    Updates a [ custom field context](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param field_id: The ID of the custom field.
    :type field_id: str
    :param context_id: The ID of the context.
    :type context_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CustomFieldContextUpdateDetails.from_dict(body)
    return web.Response(status=200)
