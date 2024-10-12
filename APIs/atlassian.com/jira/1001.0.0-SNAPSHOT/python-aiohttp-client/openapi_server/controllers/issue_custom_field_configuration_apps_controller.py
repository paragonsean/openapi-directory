from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_field_configurations import CustomFieldConfigurations
from openapi_server.models.page_bean_contextual_configuration import PageBeanContextualConfiguration
from openapi_server import util


async def get_custom_field_configuration(request: web.Request, field_id_or_key, id=None, field_context_id=None, issue_id=None, project_key_or_id=None, issue_type_id=None, start_at=None, max_results=None) -> web.Response:
    """Get custom field configurations

    Returns a [paginated](#pagination) list of configurations for a custom field created by a [Forge app](https://developer.atlassian.com/platform/forge/).  The result can be filtered by one of these criteria:   *  &#x60;id&#x60;.  *  &#x60;fieldContextId&#x60;.  *  &#x60;issueId&#x60;.  *  &#x60;projectKeyOrId&#x60; and &#x60;issueTypeId&#x60;.  Otherwise, all configurations are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that created the custom field.

    :param field_id_or_key: The ID or key of the custom field, for example &#x60;customfield_10000&#x60;.
    :type field_id_or_key: str
    :param id: The list of configuration IDs. To include multiple configurations, separate IDs with an ampersand: &#x60;id&#x3D;10000&amp;id&#x3D;10001&#x60;. Can&#39;t be provided with &#x60;fieldContextId&#x60;, &#x60;issueId&#x60;, &#x60;projectKeyOrId&#x60;, or &#x60;issueTypeId&#x60;.
    :type id: List[int]
    :param field_context_id: The list of field context IDs. To include multiple field contexts, separate IDs with an ampersand: &#x60;fieldContextId&#x3D;10000&amp;fieldContextId&#x3D;10001&#x60;. Can&#39;t be provided with &#x60;id&#x60;, &#x60;issueId&#x60;, &#x60;projectKeyOrId&#x60;, or &#x60;issueTypeId&#x60;.
    :type field_context_id: List[int]
    :param issue_id: The ID of the issue to filter results by. If the issue doesn&#39;t exist, an empty list is returned. Can&#39;t be provided with &#x60;projectKeyOrId&#x60;, or &#x60;issueTypeId&#x60;.
    :type issue_id: int
    :param project_key_or_id: The ID or key of the project to filter results by. Must be provided with &#x60;issueTypeId&#x60;. Can&#39;t be provided with &#x60;issueId&#x60;.
    :type project_key_or_id: str
    :param issue_type_id: The ID of the issue type to filter results by. Must be provided with &#x60;projectKeyOrId&#x60;. Can&#39;t be provided with &#x60;issueId&#x60;.
    :type issue_type_id: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def update_custom_field_configuration(request: web.Request, field_id_or_key, body) -> web.Response:
    """Update custom field configurations

    Update the configuration for contexts of a custom field created by a [Forge app](https://developer.atlassian.com/platform/forge/).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that created the custom field.

    :param field_id_or_key: The ID or key of the custom field, for example &#x60;customfield_10000&#x60;.
    :type field_id_or_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = CustomFieldConfigurations.from_dict(body)
    return web.Response(status=200)
