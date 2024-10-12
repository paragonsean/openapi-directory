from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_issue_property_update_request import BulkIssuePropertyUpdateRequest
from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.issue_entity_properties import IssueEntityProperties
from openapi_server.models.issue_filter_for_bulk_property_delete import IssueFilterForBulkPropertyDelete
from openapi_server.models.multi_issue_entity_properties import MultiIssueEntityProperties
from openapi_server.models.property_keys import PropertyKeys
from openapi_server import util


async def bulk_delete_issue_property(request: web.Request, property_key, body) -> web.Response:
    """Bulk delete issue property

    Deletes a property value from multiple issues. The issues to be updated can be specified by filter criteria.  The criteria the filter used to identify eligible issues are:   *  &#x60;entityIds&#x60; Only issues from this list are eligible.  *  &#x60;currentValue&#x60; Only issues with the property set to this value are eligible.  If both criteria is specified, they are joined with the logical *AND*: only issues that satisfy both criteria are considered eligible.  If no filter criteria are specified, all the issues visible to the user and where the user has the EDIT\\_ISSUES permission for the issue are considered eligible.  This operation is:   *  transactional, either the property is deleted from all eligible issues or, when errors occur, no properties are deleted.  *  [asynchronous](#async). Follow the &#x60;location&#x60; link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.  **[Permissions](#permissions) required:**   *  *Browse projects* [ project permission](https://confluence.atlassian.com/x/yodKLg) for each project containing issues.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.

    :param property_key: The key of the property.
    :type property_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssueFilterForBulkPropertyDelete.from_dict(body)
    return web.Response(status=200)


async def bulk_set_issue_properties_by_issue(request: web.Request, body) -> web.Response:
    """Bulk set issue properties by issue

    Sets or updates entity property values on issues. Up to 10 entity properties can be specified for each issue and up to 100 issues included in the request.  The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON.  This operation is:   *  [asynchronous](#async). Follow the &#x60;location&#x60; link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.  *  non-transactional. Updating some entities may fail. Such information will available in the task result.  **[Permissions](#permissions) required:**   *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param body: Details of the issue properties to be set or updated. Note that if an issue is not found, it is ignored.
    :type body: dict | bytes

    """
    body = MultiIssueEntityProperties.from_dict(body)
    return web.Response(status=200)


async def bulk_set_issue_property(request: web.Request, property_key, body) -> web.Response:
    """Bulk set issue property

    Sets a property value on multiple issues.  The value set can be a constant or determined by a [Jira expression](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/). Expressions must be computable with constant complexity when applied to a set of issues. Expressions must also comply with the [restrictions](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#restrictions) that apply to all Jira expressions.  The issues to be updated can be specified by a filter.  The filter identifies issues eligible for update using these criteria:   *  &#x60;entityIds&#x60; Only issues from this list are eligible.  *  &#x60;currentValue&#x60; Only issues with the property set to this value are eligible.  *  &#x60;hasProperty&#x60;:           *  If *true*, only issues with the property are eligible.      *  If *false*, only issues without the property are eligible.  If more than one criteria is specified, they are joined with the logical *AND*: only issues that satisfy all criteria are eligible.  If an invalid combination of criteria is provided, an error is returned. For example, specifying a &#x60;currentValue&#x60; and &#x60;hasProperty&#x60; as *false* would not match any issues (because without the property the property cannot have a value).  The filter is optional. Without the filter all the issues visible to the user and where the user has the EDIT\\_ISSUES permission for the issue are considered eligible.  This operation is:   *  transactional, either all eligible issues are updated or, when errors occur, none are updated.  *  [asynchronous](#async). Follow the &#x60;location&#x60; link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for each project containing issues.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.

    :param property_key: The key of the property. The maximum length is 255 characters.
    :type property_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = BulkIssuePropertyUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_set_issues_properties_list(request: web.Request, body) -> web.Response:
    """Bulk set issues properties by list

    Sets or updates a list of entity property values on issues. A list of up to 10 entity properties can be specified along with up to 10,000 issues on which to set or update that list of entity properties.  The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON. The maximum length of single issue property value is 32768 characters. This operation can be accessed anonymously.  This operation is:   *  transactional, either all properties are updated in all eligible issues or, when errors occur, no properties are updated.  *  [asynchronous](#async). Follow the &#x60;location&#x60; link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.  **[Permissions](#permissions) required:**   *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param body: Issue properties to be set or updated with values.
    :type body: dict | bytes

    """
    body = IssueEntityProperties.from_dict(body)
    return web.Response(status=200)


async def delete_issue_property(request: web.Request, issue_id_or_key, property_key) -> web.Response:
    """Delete issue property

    Deletes an issue&#39;s property.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The key or ID of the issue.
    :type issue_id_or_key: str
    :param property_key: The key of the property.
    :type property_key: str

    """
    return web.Response(status=200)


async def get_issue_property(request: web.Request, issue_id_or_key, property_key) -> web.Response:
    """Get issue property

    Returns the key and value of an issue&#39;s property.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The key or ID of the issue.
    :type issue_id_or_key: str
    :param property_key: The key of the property.
    :type property_key: str

    """
    return web.Response(status=200)


async def get_issue_property_keys(request: web.Request, issue_id_or_key) -> web.Response:
    """Get issue property keys

    Returns the URLs and keys of an issue&#39;s properties.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Property details are only returned where the user has:   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The key or ID of the issue.
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def set_issue_property(request: web.Request, issue_id_or_key, property_key, body) -> web.Response:
    """Set issue property

    Sets the value of an issue&#39;s property. Use this resource to store custom data against an issue.  The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param property_key: The key of the issue property. The maximum length is 255 characters.
    :type property_key: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)
