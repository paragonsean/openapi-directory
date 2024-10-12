from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def acknowledge_errors(request: web.Request, ) -> web.Response:
    """acknowledge_errors

    


    """
    return web.Response(status=200)


async def add_actor_users(request: web.Request, project_id_or_key, id) -> web.Response:
    """add_actor_users

    Adds an actor (user or group) to a project role.

    :param project_id_or_key: the project id or project key
    :type project_id_or_key: str
    :param id: the project role id
    :type id: int

    """
    return web.Response(status=200)


async def add_attachment(request: web.Request, issue_id_or_key) -> web.Response:
    """add_attachment

    Add one or more attachments to an issue.  &lt;p&gt;  This resource expects a multipart post. The media-type multipart/form-data is defined in RFC 1867. Most client  libraries have classes that make dealing with multipart posts simple. For instance, in Java the Apache HTTP Components  library provides a  &lt;a href&#x3D;\&quot;http://hc.apache.org/httpcomponents-client-ga/httpmime/apidocs/org/apache/http/entity/mime/MultipartEntity.html\&quot;&gt;MultiPartEntity&lt;/a&gt;  that makes it simple to submit a multipart POST.  &lt;p&gt;  In order to protect against XSRF attacks, because this method accepts multipart/form-data, it has XSRF protection  on it.  This means you must submit a header of X-Atlassian-Token: no-check with the request, otherwise it will be  blocked.  &lt;p&gt;  The name of the multipart/form-data parameter that contains attachments must be \&quot;file\&quot;  &lt;p&gt;  A simple example to upload a file called \&quot;myfile.txt\&quot; to issue REST-123:  &lt;pre&gt;curl -D- -u admin:admin -X POST -H \&quot;X-Atlassian-Token: no-check\&quot; -F \&quot;file&#x3D;@myfile.txt\&quot; http://myhost/rest/api/2/issue/TEST-123/attachments&lt;/pre&gt;

    :param issue_id_or_key: the issue that you want to add the attachments to
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def add_comment(request: web.Request, issue_id_or_key, expand=None) -> web.Response:
    """add_comment

    Adds a new comment to an issue.

    :param issue_id_or_key: a string containing the issue id or key the comment will be added to
    :type issue_id_or_key: str
    :param expand: optional flags: renderedBody (provides body rendered in HTML)
    :type expand: str

    """
    return web.Response(status=200)


async def add_field(request: web.Request, screen_id, tab_id) -> web.Response:
    """add_field

    Adds field to the given tab.

    :param screen_id: id of screen
    :type screen_id: int
    :param tab_id: id of tab
    :type tab_id: int

    """
    return web.Response(status=200)


async def add_field_to_default_screen(request: web.Request, field_id) -> web.Response:
    """add_field_to_default_screen

    Adds field or custom field to the default tab

    :param field_id: id of field / custom field
    :type field_id: str

    """
    return web.Response(status=200)


async def add_project_role_actors_to_role(request: web.Request, id) -> web.Response:
    """add_project_role_actors_to_role

    Adds default actors to the given role. The request data should contain a list of usernames or a list of groups to add.

    :param id: the role id to remove the actors from
    :type id: int

    """
    return web.Response(status=200)


async def add_record(request: web.Request, ) -> web.Response:
    """add_record

    Store a record in Audit Log


    """
    return web.Response(status=200)


async def add_share_permission(request: web.Request, id) -> web.Response:
    """add_share_permission

    Adds a share permissions to the given filter. Adding a global permission removes all previous permissions from the filter.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def add_tab(request: web.Request, screen_id) -> web.Response:
    """add_tab

    Creates tab for given screen

    :param screen_id: id of screen
    :type screen_id: int

    """
    return web.Response(status=200)


async def add_user_to_application(request: web.Request, username=None, application_key=None) -> web.Response:
    """add_user_to_application

    Add user to given application. Admin permission will be required to perform this operation.

    :param username: username
    :type username: str
    :param application_key: application key
    :type application_key: str

    """
    return web.Response(status=200)


async def add_user_to_group(request: web.Request, groupname=None) -> web.Response:
    """add_user_to_group

    Adds given user to a group.  &lt;p&gt;  Returns the current state of the group.

    :param groupname: A name of requested group.
    :type groupname: str

    """
    return web.Response(status=200)


async def add_vote(request: web.Request, issue_id_or_key) -> web.Response:
    """add_vote

    Cast your vote in favour of an issue.

    :param issue_id_or_key: the issue to view voting information for
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def add_watcher(request: web.Request, issue_id_or_key) -> web.Response:
    """add_watcher

    Adds a user to an issue&#39;s watcher list.

    :param issue_id_or_key: a String containing an issue key.
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def add_worklog(request: web.Request, issue_id_or_key, adjust_estimate=None, new_estimate=None, reduce_by=None) -> web.Response:
    """add_worklog

    Adds a new worklog entry to an issue.

    :param issue_id_or_key: a string containing the issue id or key the worklog will be added to
    :type issue_id_or_key: str
    :param adjust_estimate: (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        &lt;ul&gt;                        &lt;li&gt;\&quot;new\&quot; - sets the estimate to a specific value&lt;/li&gt;                        &lt;li&gt;\&quot;leave\&quot;- leaves the estimate as is&lt;/li&gt;                        &lt;li&gt;\&quot;manual\&quot; - specify a specific amount to increase remaining estimate by&lt;/li&gt;                        &lt;li&gt;\&quot;auto\&quot;- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog&lt;/li&gt; &lt;/ul&gt;
    :type adjust_estimate: str
    :param new_estimate: (required when \&quot;new\&quot; is selected for adjustEstimate) the new value for the remaining estimate field. e.g. \&quot;2d\&quot;
    :type new_estimate: str
    :param reduce_by: (required when \&quot;manual\&quot; is selected for adjustEstimate) the amount to reduce the remaining estimate by e.g. \&quot;2d\&quot;
    :type reduce_by: str

    """
    return web.Response(status=200)


async def api2_application_properties_get(request: web.Request, key=None, permission_level=None, key_filter=None) -> web.Response:
    """api2_application_properties_get

    Returns an application property.

    :param key: a String containing the property key
    :type key: str
    :param permission_level: when fetching a list specifies the permission level of all items in the list                         see {@link com.atlassian.jira.bc.admin.ApplicationPropertiesService.EditPermissionLevel}
    :type permission_level: str
    :param key_filter: when fetching a list allows the list to be filtered by the property&#39;s start of key                         e.g. \&quot;jira.lf.*\&quot; whould fetch only those permissions that are editable and whose keys start with                         \&quot;jira.lf.\&quot;. This is a regex.
    :type key_filter: str

    """
    return web.Response(status=200)


async def api2_avatar_type_temporary_crop_post(request: web.Request, type) -> web.Response:
    """api2_avatar_type_temporary_crop_post

    Updates the cropping instructions of the temporary avatar.

    :param type: the avatar type
    :type type: str

    """
    return web.Response(status=200)


async def api2_comment_comment_id_properties_get(request: web.Request, comment_id) -> web.Response:
    """api2_comment_comment_id_properties_get

    Returns the keys of all properties for the comment identified by the key or by the id.

    :param comment_id: the comment from which keys will be returned.
    :type comment_id: str

    """
    return web.Response(status=200)


async def api2_comment_comment_id_properties_property_key_delete(request: web.Request, comment_id, property_key) -> web.Response:
    """api2_comment_comment_id_properties_property_key_delete

    Removes the property from the comment identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the comment.

    :param comment_id: the comment from which keys will be returned.
    :type comment_id: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_comment_comment_id_properties_property_key_get(request: web.Request, comment_id, property_key) -> web.Response:
    """api2_comment_comment_id_properties_property_key_get

    Returns the value of the property with a given key from the comment identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the comment.

    :param comment_id: the comment from which keys will be returned.
    :type comment_id: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_comment_comment_id_properties_property_key_put(request: web.Request, comment_id, property_key) -> web.Response:
    """api2_comment_comment_id_properties_property_key_put

    Sets the value of the specified comment&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the comment identified by the key or by the id. The user  who stores the data is required to have permissions to administer the comment.  &lt;/p&gt;

    :param comment_id: the comment from which keys will be returned.
    :type comment_id: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_component_id_delete(request: web.Request, id, move_issues_to=None) -> web.Response:
    """api2_component_id_delete

    Delete a project component.

    :param id: The component to delete.
    :type id: str
    :param move_issues_to: The new component applied to issues whose &#39;id&#39; component will be deleted.                      If this value is null, then the &#39;id&#39; component is simply removed from the related isues.
    :type move_issues_to: str

    """
    return web.Response(status=200)


async def api2_dashboard_dashboard_id_items_item_id_properties_get(request: web.Request, item_id, dashboard_id) -> web.Response:
    """api2_dashboard_dashboard_id_items_item_id_properties_get

    Returns the keys of all properties for the dashboard item identified by the id.

    :param item_id: the dashboard item from which keys will be returned.
    :type item_id: str
    :param dashboard_id: 
    :type dashboard_id: str

    """
    return web.Response(status=200)


async def api2_dashboard_dashboard_id_items_item_id_properties_property_key_delete(request: web.Request, item_id, dashboard_id, property_key) -> web.Response:
    """api2_dashboard_dashboard_id_items_item_id_properties_property_key_delete

    Removes the property from the dashboard item identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the dashboard item.

    :param item_id: the dashboard item from which keys will be returned.
    :type item_id: str
    :param dashboard_id: 
    :type dashboard_id: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_dashboard_dashboard_id_items_item_id_properties_property_key_get(request: web.Request, item_id, dashboard_id, property_key) -> web.Response:
    """api2_dashboard_dashboard_id_items_item_id_properties_property_key_get

    Returns the value of the property with a given key from the dashboard item identified by the id.  The user who retrieves the property is required to have permissions to read the dashboard item.

    :param item_id: the dashboard item from which keys will be returned.
    :type item_id: str
    :param dashboard_id: 
    :type dashboard_id: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_dashboard_dashboard_id_items_item_id_properties_property_key_put(request: web.Request, item_id, dashboard_id, property_key) -> web.Response:
    """api2_dashboard_dashboard_id_items_item_id_properties_property_key_put

    Sets the value of the specified dashboard item&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the dashboard item identified by the id.  The user who stores the data is required to have permissions to administer the dashboard item.  &lt;/p&gt;

    :param item_id: the dashboard item from which keys will be returned.
    :type item_id: str
    :param dashboard_id: 
    :type dashboard_id: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_filter_id_columns_delete(request: web.Request, id) -> web.Response:
    """api2_filter_id_columns_delete

    Resets the columns for the given filter such that the filter no longer has its own column config.

    :param id: id of the filter
    :type id: int

    """
    return web.Response(status=200)


async def api2_filter_id_columns_get(request: web.Request, id) -> web.Response:
    """api2_filter_id_columns_get

    Returns the default columns for the given filter. Currently logged in user will be used as  the user making such request.

    :param id: id of the filter
    :type id: int

    """
    return web.Response(status=200)


async def api2_filter_id_columns_put(request: web.Request, id) -> web.Response:
    """api2_filter_id_columns_put

    Sets the default columns for the given filter.

    :param id: id of the filter
    :type id: int

    """
    return web.Response(status=200)


async def api2_issue_issue_id_or_key_properties_get(request: web.Request, issue_id_or_key) -> web.Response:
    """api2_issue_issue_id_or_key_properties_get

    Returns the keys of all properties for the issue identified by the key or by the id.

    :param issue_id_or_key: the issue from which keys will be returned.
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def api2_issue_issue_id_or_key_properties_property_key_delete(request: web.Request, issue_id_or_key, property_key) -> web.Response:
    """api2_issue_issue_id_or_key_properties_property_key_delete

    Removes the property from the issue identified by the key or by the id. Ths user removing the property is required  to have permissions to edit the issue.

    :param issue_id_or_key: the issue from which keys will be returned.
    :type issue_id_or_key: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_issue_issue_id_or_key_properties_property_key_get(request: web.Request, issue_id_or_key, property_key) -> web.Response:
    """api2_issue_issue_id_or_key_properties_property_key_get

    Returns the value of the property with a given key from the issue identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the issue.

    :param issue_id_or_key: the issue from which keys will be returned.
    :type issue_id_or_key: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_issue_issue_id_or_key_properties_property_key_put(request: web.Request, issue_id_or_key, property_key) -> web.Response:
    """api2_issue_issue_id_or_key_properties_property_key_put

    Sets the value of the specified issue&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the issue identified by the key or by the id. The user  who stores the data is required to have permissions to edit the issue.  &lt;/p&gt;

    :param issue_id_or_key: the issue from which keys will be returned.
    :type issue_id_or_key: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_issuesecurityschemes_id_get(request: web.Request, id) -> web.Response:
    """api2_issuesecurityschemes_id_get

    Returns the issue security scheme along with that are defined.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api2_issuetype_id_avatar_post(request: web.Request, id) -> web.Response:
    """api2_issuetype_id_avatar_post

    Converts temporary avatar into a real avatar

    :param id: the id of the issue type, which avatar is updated.
    :type id: str

    """
    return web.Response(status=200)


async def api2_issuetype_id_avatar_temporary_post(request: web.Request, id) -> web.Response:
    """api2_issuetype_id_avatar_temporary_post

    Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because  the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from  which the client parses the JSON from.  &lt;p&gt;  Creating a temporary avatar is part of a 3-step process in uploading a new  avatar for an issue type: upload, crop, confirm. This endpoint allows you to use a multipart upload  instead of sending the image directly as the request body.  &lt;/p&gt;  &lt;p&gt;  You *must* use \&quot;avatar\&quot; as the name of the upload parameter:&lt;/p&gt;  &lt;p&gt;  &lt;pre&gt;  curl -c cookiejar.txt -X POST -u admin:admin -H \&quot;X-Atlassian-Token: no-check\&quot; \\    -F \&quot;avatar&#x3D;@mynewavatar.png;type&#x3D;image/png\&quot; \\    &#39;http://localhost:8090/jira/rest/api/2/issuetype/1/avatar/temporary&#39;  &lt;/pre&gt;

    :param id: the id of the issue type, which avatar is updated.
    :type id: str

    """
    return web.Response(status=200)


async def api2_issuetype_id_delete(request: web.Request, id, alternative_issue_type_id=None) -> web.Response:
    """api2_issuetype_id_delete

    Deletes the specified issue type. If the issue type has any associated issues, these issues will be migrated to  the alternative issue type specified in the parameter. You can determine the alternative issue types by calling  the &lt;b&gt;/rest/api/2/issuetype/{id}/alternatives&lt;/b&gt; resource.

    :param id: the id of the issue type to update.
    :type id: str
    :param alternative_issue_type_id: the id of an issue type to which issues associated with the removed issue type will be migrated.
    :type alternative_issue_type_id: str

    """
    return web.Response(status=200)


async def api2_issuetype_id_get(request: web.Request, id) -> web.Response:
    """api2_issuetype_id_get

    Returns a full representation of the issue type that has the given id.

    :param id: the id of the issue type to update.
    :type id: str

    """
    return web.Response(status=200)


async def api2_issuetype_issue_type_id_properties_property_key_delete(request: web.Request, issue_type_id, property_key) -> web.Response:
    """api2_issuetype_issue_type_id_properties_property_key_delete

    Removes the property from the issue type identified by the id. Ths user removing the property is required  to have permissions to edit the issue type.

    :param issue_type_id: the issue type from which the keys will be returned
    :type issue_type_id: str
    :param property_key: the key of the property to return
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_issuetype_issue_type_id_properties_property_key_get(request: web.Request, issue_type_id, property_key) -> web.Response:
    """api2_issuetype_issue_type_id_properties_property_key_get

    Returns the value of the property with a given key from the issue type identified by the id. The user who retrieves  the property is required to have permissions to view the issue type.

    :param issue_type_id: the issue type from which the keys will be returned
    :type issue_type_id: str
    :param property_key: the key of the property to return
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_issuetype_issue_type_id_properties_property_key_put(request: web.Request, issue_type_id, property_key) -> web.Response:
    """api2_issuetype_issue_type_id_properties_property_key_put

    Sets the value of the specified issue type&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against an issue type identified by the id. The user  who stores the data is required to have permissions to edit an issue type.  &lt;/p&gt;

    :param issue_type_id: the issue type from which the keys will be returned
    :type issue_type_id: str
    :param property_key: the key of the property to return
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_myself_get(request: web.Request, ) -> web.Response:
    """api2_myself_get

    Returns currently logged user. This resource cannot be accessed anonymously.


    """
    return web.Response(status=200)


async def api2_myself_put(request: web.Request, ) -> web.Response:
    """api2_myself_put

    Modify currently logged user. The \&quot;value\&quot; fields present will override the existing value.  Fields skipped in request will not be changed. Only email and display name can be change that way.  Requires user password.


    """
    return web.Response(status=200)


async def api2_notificationscheme_id_get(request: web.Request, id, expand=None) -> web.Response:
    """api2_notificationscheme_id_get

    Returns a full representation of the notification scheme for the given id. This resource will return a  notification scheme containing a list of events and recipient configured to receive notifications for these events. Consumer  should allow events without recipients to appear in response. User accessing  the data is required to have permissions to administer at least one project associated with the requested notification scheme.  &lt;p&gt;  Notification recipients can be:  &lt;ul&gt;  &lt;li&gt;current assignee - the value of the notificationType is CurrentAssignee&lt;/li&gt;  &lt;li&gt;issue reporter - the value of the notificationType is Reporter&lt;/li&gt;  &lt;li&gt;current user - the value of the notificationType is CurrentUser&lt;/li&gt;  &lt;li&gt;project lead - the value of the notificationType is ProjectLead&lt;/li&gt;  &lt;li&gt;component lead - the value of the notificationType is ComponentLead&lt;/li&gt;  &lt;li&gt;all watchers - the value of the notification type is AllWatchers&lt;/li&gt;  &lt;li&gt;configured user - the value of the notification type is User. Parameter will contain key of the user. Information about the user will be provided  if &lt;b&gt;user&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;li&gt;configured group - the value of the notification type is Group. Parameter will contain name of the group. Information about the group will be provided  if &lt;b&gt;group&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;li&gt;configured email address - the value of the notification type is EmailAddress, additionally information about the email will be provided.&lt;/li&gt;  &lt;li&gt;users or users in groups in the configured custom fields - the value of the notification type is UserCustomField or GroupCustomField. Parameter  will contain id of the custom field. Information about the field will be provided if &lt;b&gt;field&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;li&gt;configured project role - the value of the notification type is ProjectRole. Parameter will contain project role id. Information about the project role  will be provided if &lt;b&gt;projectRole&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;/ul&gt;  Please see the example for reference.  &lt;/p&gt;  The events can be JIRA system events or events configured by administrator. In case of the system events, data about theirs  ids, names and descriptions is provided. In case of custom events, the template event is included as well.

    :param id: an id of the notification scheme to retrieve
    :type id: int
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def api2_project_project_id_or_key_avatar_id_delete(request: web.Request, project_id_or_key, id) -> web.Response:
    """api2_project_project_id_or_key_avatar_id_delete

    Deletes avatar

    :param project_id_or_key: Project id or project key
    :type project_id_or_key: str
    :param id: database id for avatar
    :type id: int

    """
    return web.Response(status=200)


async def api2_project_project_id_or_key_avatar_post(request: web.Request, project_id_or_key) -> web.Response:
    """api2_project_project_id_or_key_avatar_post

    Converts temporary avatar into a real avatar

    :param project_id_or_key: 
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def api2_project_project_id_or_key_avatar_put(request: web.Request, project_id_or_key) -> web.Response:
    """api2_project_project_id_or_key_avatar_put

    

    :param project_id_or_key: 
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def api2_project_project_id_or_key_avatar_temporary_post(request: web.Request, project_id_or_key) -> web.Response:
    """api2_project_project_id_or_key_avatar_temporary_post

    Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because  the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from  which the client parses the JSON.

    :param project_id_or_key: Project id or project key
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def api2_project_project_id_or_key_avatars_get(request: web.Request, project_id_or_key) -> web.Response:
    """api2_project_project_id_or_key_avatars_get

    Returns all avatars which are visible for the currently logged in user.  The avatars are grouped into  system and custom.

    :param project_id_or_key: project id or project key
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def api2_project_project_id_or_key_get(request: web.Request, project_id_or_key, expand=None) -> web.Response:
    """api2_project_project_id_or_key_get

    Contains a full representation of a project in JSON format.  &lt;p&gt;  All project keys associated with the project will only be returned if &lt;code&gt;expand&#x3D;projectKeys&lt;/code&gt;.  &lt;p&gt;

    :param project_id_or_key: the project id or project key
    :type project_id_or_key: str
    :param expand: the parameters to expand
    :type expand: str

    """
    return web.Response(status=200)


async def api2_project_project_id_or_key_properties_get(request: web.Request, project_id_or_key) -> web.Response:
    """api2_project_project_id_or_key_properties_get

    Returns the keys of all properties for the project identified by the key or by the id.

    :param project_id_or_key: the project from which keys will be returned.
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def api2_project_project_id_or_key_properties_property_key_delete(request: web.Request, project_id_or_key, property_key) -> web.Response:
    """api2_project_project_id_or_key_properties_property_key_delete

    Removes the property from the project identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the project.

    :param project_id_or_key: the project from which keys will be returned.
    :type project_id_or_key: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_project_project_id_or_key_properties_property_key_get(request: web.Request, project_id_or_key, property_key) -> web.Response:
    """api2_project_project_id_or_key_properties_property_key_get

    Returns the value of the property with a given key from the project identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the project.

    :param project_id_or_key: the project from which keys will be returned.
    :type project_id_or_key: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_project_project_id_or_key_properties_property_key_put(request: web.Request, project_id_or_key, property_key) -> web.Response:
    """api2_project_project_id_or_key_properties_property_key_put

    Sets the value of the specified project&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the project identified by the key or by the id. The user  who stores the data is required to have permissions to administer the project.  &lt;/p&gt;

    :param project_id_or_key: the project from which keys will be returned.
    :type project_id_or_key: str
    :param property_key: the key of the property to return.
    :type property_key: str

    """
    return web.Response(status=200)


async def api2_project_project_id_or_key_role_get(request: web.Request, project_id_or_key) -> web.Response:
    """api2_project_project_id_or_key_role_get

    Returns all roles in the given project Id or key, with links to full details on each role.

    :param project_id_or_key: the project id or project key
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def api2_project_project_key_or_id_issuesecuritylevelscheme_get(request: web.Request, project_key_or_id) -> web.Response:
    """api2_project_project_key_or_id_issuesecuritylevelscheme_get

    Returns the issue security scheme for project.

    :param project_key_or_id: 
    :type project_key_or_id: str

    """
    return web.Response(status=200)


async def api2_project_project_key_or_id_notificationscheme_get(request: web.Request, project_key_or_id, expand=None) -> web.Response:
    """api2_project_project_key_or_id_notificationscheme_get

    Gets a notification scheme associated with the project.  Follow the documentation of /notificationscheme/{id} resource for all details about returned value.

    :param project_key_or_id: key or id of the project
    :type project_key_or_id: str
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def api2_projectvalidate_key_get(request: web.Request, key=None) -> web.Response:
    """api2_projectvalidate_key_get

    Validates a project key.

    :param key: the project key
    :type key: str

    """
    return web.Response(status=200)


async def api2_role_get(request: web.Request, ) -> web.Response:
    """api2_role_get

    Get all the ProjectRoles available in JIRA. Currently this list is global.


    """
    return web.Response(status=200)


async def api2_universal_avatar_type_type_owner_owning_object_id_avatar_id_delete(request: web.Request, id, type, owning_object_id) -> web.Response:
    """api2_universal_avatar_type_type_owner_owning_object_id_avatar_id_delete

    Deletes avatar

    :param id: database id for avatar
    :type id: int
    :param type: Project id or project key
    :type type: str
    :param owning_object_id: 
    :type owning_object_id: str

    """
    return web.Response(status=200)


async def api2_universal_avatar_type_type_owner_owning_object_id_avatar_post(request: web.Request, type, owning_object_id) -> web.Response:
    """api2_universal_avatar_type_type_owner_owning_object_id_avatar_post

    

    :param type: 
    :type type: str
    :param owning_object_id: 
    :type owning_object_id: str

    """
    return web.Response(status=200)


async def api2_universal_avatar_type_type_owner_owning_object_id_temp_post(request: web.Request, type, owning_object_id) -> web.Response:
    """api2_universal_avatar_type_type_owner_owning_object_id_temp_post

    

    :param type: 
    :type type: str
    :param owning_object_id: 
    :type owning_object_id: str

    """
    return web.Response(status=200)


async def api2_user_avatar_id_delete(request: web.Request, id, username=None) -> web.Response:
    """api2_user_avatar_id_delete

    Deletes avatar

    :param id: database id for avatar
    :type id: int
    :param username: username
    :type username: str

    """
    return web.Response(status=200)


async def api2_user_avatar_post(request: web.Request, username=None) -> web.Response:
    """api2_user_avatar_post

    Converts temporary avatar into a real avatar

    :param username: username
    :type username: str

    """
    return web.Response(status=200)


async def api2_user_avatar_put(request: web.Request, username=None) -> web.Response:
    """api2_user_avatar_put

    

    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def api2_user_avatar_temporary_post(request: web.Request, username=None) -> web.Response:
    """api2_user_avatar_temporary_post

    Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because  the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from  which the client parses the JSON from.  &lt;p&gt;  Creating a temporary avatar is part of a 3-step process in uploading a new  avatar for a user: upload, crop, confirm. This endpoint allows you to use a multipart upload  instead of sending the image directly as the request body.  &lt;/p&gt;  &lt;p&gt;  You *must* use \&quot;avatar\&quot; as the name of the upload parameter:&lt;/p&gt;  &lt;p/&gt;  &lt;pre&gt;  curl -c cookiejar.txt -X POST -u admin:admin -H \&quot;X-Atlassian-Token: no-check\&quot; \\    -F \&quot;avatar&#x3D;@mynewavatar.png;type&#x3D;image/png\&quot; \\    &#39;http://localhost:8090/jira/rest/api/2/user/avatar/temporary?username&#x3D;admin&#39;  &lt;/pre&gt;

    :param username: Username
    :type username: str

    """
    return web.Response(status=200)


async def api2_user_avatars_get(request: web.Request, username=None) -> web.Response:
    """api2_user_avatars_get

    Returns all avatars which are visible for the currently logged in user.

    :param username: username
    :type username: str

    """
    return web.Response(status=200)


async def api2_user_columns_delete(request: web.Request, username=None) -> web.Response:
    """api2_user_columns_delete

    Reset the default columns for the given user to the system default. Admin permission will be required to get  columns for a user other than the currently logged in user.

    :param username: username
    :type username: str

    """
    return web.Response(status=200)


async def api2_user_columns_get(request: web.Request, username=None) -> web.Response:
    """api2_user_columns_get

    Returns the default columns for the given user. Admin permission will be required to get columns for a user  other than the currently logged in user.

    :param username: username
    :type username: str

    """
    return web.Response(status=200)


async def api2_user_columns_put(request: web.Request, ) -> web.Response:
    """api2_user_columns_put

    Sets the default columns for the given user.  Admin permission will be required to get columns for a user  other than the currently logged in user.


    """
    return web.Response(status=200)


async def api2_user_get(request: web.Request, username=None, key=None) -> web.Response:
    """api2_user_get

    Returns a user. This resource cannot be accessed anonymously.

    :param username: the username
    :type username: str
    :param key: user key
    :type key: str

    """
    return web.Response(status=200)


async def api2_user_properties_get(request: web.Request, user_key=None, username=None) -> web.Response:
    """api2_user_properties_get

    Returns the keys of all properties for the user identified by the key or by the id.

    :param user_key: key of the user whose properties are to be returned
    :type user_key: str
    :param username: username of the user whose properties are to be returned
    :type username: str

    """
    return web.Response(status=200)


async def api2_user_properties_property_key_delete(request: web.Request, property_key, user_key=None, username=None) -> web.Response:
    """api2_user_properties_property_key_delete

    Removes the property from the user identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the user.

    :param property_key: 
    :type property_key: str
    :param user_key: key of the user whose property is to be removed
    :type user_key: str
    :param username: username of the user whose property is to be removed
    :type username: str

    """
    return web.Response(status=200)


async def api2_user_properties_property_key_get(request: web.Request, property_key, user_key=None, username=None) -> web.Response:
    """api2_user_properties_property_key_get

    Returns the value of the property with a given key from the user identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the user.

    :param property_key: 
    :type property_key: str
    :param user_key: key of the user whose property is to be returned
    :type user_key: str
    :param username: username of the user whose property is to be returned
    :type username: str

    """
    return web.Response(status=200)


async def api2_user_properties_property_key_put(request: web.Request, property_key, user_key=None, username=None) -> web.Response:
    """api2_user_properties_property_key_put

    Sets the value of the specified user&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the user identified by the key or by the id. The user  who stores the data is required to have permissions to administer the user.  &lt;/p&gt;

    :param property_key: 
    :type property_key: str
    :param user_key: key of the user whose property is to be set
    :type user_key: str
    :param username: username of the user whose property is to be set
    :type username: str

    """
    return web.Response(status=200)


async def api2_user_put(request: web.Request, username=None, key=None) -> web.Response:
    """api2_user_put

    Modify user. The \&quot;value\&quot; fields present will override the existing value.  Fields skipped in request will not be changed.

    :param username: the username
    :type username: str
    :param key: user key
    :type key: str

    """
    return web.Response(status=200)


async def api2_version_id_delete(request: web.Request, id, move_fix_issues_to=None, move_affected_issues_to=None) -> web.Response:
    """api2_version_id_delete

    Delete a project version.

    :param id: The version to delete
    :type id: str
    :param move_fix_issues_to: The version to set fixVersion to on issues where the deleted version is the fix version,                              If null then the fixVersion is removed.
    :type move_fix_issues_to: str
    :param move_affected_issues_to: The version to set affectedVersion to on issues where the deleted version is the affected version,                              If null then the affectedVersion is removed.
    :type move_affected_issues_to: str

    """
    return web.Response(status=200)


async def api2_version_id_remove_and_swap_post(request: web.Request, id) -> web.Response:
    """api2_version_id_remove_and_swap_post

    Delete a project version.

    :param id: The version to delete
    :type id: str

    """
    return web.Response(status=200)


async def api2_version_version_id_remotelink_global_id_post(request: web.Request, version_id, global_id) -> web.Response:
    """api2_version_version_id_remotelink_global_id_post

    Create a remote version link via POST.  The link&#39;s global ID will be taken from the  JSON payload if provided; otherwise, it will be generated.

    :param version_id: The version ID of the remote link
    :type version_id: str
    :param global_id: The global ID of the remote link
    :type global_id: str

    """
    return web.Response(status=200)


async def api2_version_version_id_remotelink_post(request: web.Request, version_id) -> web.Response:
    """api2_version_version_id_remotelink_post

    Create a remote version link via POST.  The link&#39;s global ID will be taken from the  JSON payload if provided; otherwise, it will be generated.

    :param version_id: The version for which to delete ALL existing remote version links
    :type version_id: str

    """
    return web.Response(status=200)


async def api2_workflow_api2_transitions_id_properties_delete(request: web.Request, id, key=None, workflow_name=None, workflow_mode=None) -> web.Response:
    """api2_workflow_api2_transitions_id_properties_delete

    Delete a property from the passed transition on the passed workflow. It is not an error to delete a property that  does not exist.

    :param id: the ID of the transition within the workflow.
    :type id: int
    :param key: the name of the property to add.
    :type key: str
    :param workflow_name: the name of the workflow to use.
    :type workflow_name: str
    :param workflow_mode: the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;.
    :type workflow_mode: str

    """
    return web.Response(status=200)


async def api2_workflowscheme_id_issuetype_issue_type_delete(request: web.Request, issue_type, id, update_draft_if_needed=None) -> web.Response:
    """api2_workflowscheme_id_issuetype_issue_type_delete

    Remove the specified issue type mapping from the scheme.

    :param issue_type: the issue type being set.
    :type issue_type: str
    :param id: the id of the scheme.
    :type id: int
    :param update_draft_if_needed: when true will create and return a draft when the workflow scheme cannot be edited                             (e.g. when it is being used by a project).
    :type update_draft_if_needed: bool

    """
    return web.Response(status=200)


async def api2_workflowscheme_id_issuetype_issue_type_get(request: web.Request, issue_type, id, return_draft_if_exists=None) -> web.Response:
    """api2_workflowscheme_id_issuetype_issue_type_get

    Returns the issue type mapping for the passed workflow scheme.

    :param issue_type: the issue type being set.
    :type issue_type: str
    :param id: the id of the scheme.
    :type id: int
    :param return_draft_if_exists: when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself.
    :type return_draft_if_exists: bool

    """
    return web.Response(status=200)


async def approve_upgrade(request: web.Request, ) -> web.Response:
    """approve_upgrade

    


    """
    return web.Response(status=200)


async def are_metrics_exposed(request: web.Request, ) -> web.Response:
    """are_metrics_exposed

    


    """
    return web.Response(status=200)


async def assign(request: web.Request, issue_id_or_key) -> web.Response:
    """assign

    Assigns an issue to a user.  You can use this resource to assign issues when the user submitting the request has the assign permission but not the  edit issue permission.  If the name is \&quot;-1\&quot; automatic assignee is used.  A null name will remove the assignee.

    :param issue_id_or_key: a String containing an issue key
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def assign_permission_scheme(request: web.Request, project_key_or_id, expand=None) -> web.Response:
    """assign_permission_scheme

    Assigns a permission scheme with a project.

    :param project_key_or_id: key or id of the project
    :type project_key_or_id: str
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def can_move_sub_task(request: web.Request, issue_id_or_key) -> web.Response:
    """can_move_sub_task

    

    :param issue_id_or_key: The parent issue&#39;s key or id
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def cancel_upgrade(request: web.Request, ) -> web.Response:
    """cancel_upgrade

    


    """
    return web.Response(status=200)


async def change_my_password(request: web.Request, ) -> web.Response:
    """change_my_password

    Modify caller password.


    """
    return web.Response(status=200)


async def change_user_password(request: web.Request, username=None, key=None) -> web.Response:
    """change_user_password

    Modify user password.

    :param username: the username
    :type username: str
    :param key: user key
    :type key: str

    """
    return web.Response(status=200)


async def create_component(request: web.Request, ) -> web.Response:
    """create_component

    Create a component via POST.


    """
    return web.Response(status=200)


async def create_custom_field(request: web.Request, ) -> web.Response:
    """create_custom_field

    Creates a custom field using a definition (object encapsulating custom field data)


    """
    return web.Response(status=200)


async def create_draft_for_parent(request: web.Request, id) -> web.Response:
    """create_draft_for_parent

    Create a draft for the passed scheme. The draft will be a copy of the state of the parent.

    :param id: the id of the parent scheme.
    :type id: int

    """
    return web.Response(status=200)


async def create_filter(request: web.Request, expand=None) -> web.Response:
    """create_filter

    Creates a new filter, and returns newly created filter.  Currently sets permissions just using the users default sharing permissions

    :param expand: the parameters to expand
    :type expand: str

    """
    return web.Response(status=200)


async def create_group(request: web.Request, ) -> web.Response:
    """create_group

    Creates a group by given group parameter  &lt;p&gt;  Returns REST representation for the requested group.


    """
    return web.Response(status=200)


async def create_issue(request: web.Request, ) -> web.Response:
    """create_issue

    Creates an issue or a sub-task from a JSON representation.  &lt;p/&gt;  The fields that can be set on create, in either the fields parameter or the update parameter can be determined  using the &lt;b&gt;/rest/api/2/issue/createmeta&lt;/b&gt; resource.  If a field is not configured to appear on the create screen, then it will not be in the createmeta, and a field  validation error will occur if it is submitted.  &lt;p/&gt;  Creating a sub-task is similar to creating a regular issue, with two important differences:  &lt;ul&gt;  &lt;li&gt;the &lt;code&gt;issueType&lt;/code&gt; field must correspond to a sub-task issue type (you can use  &lt;code&gt;/issue/createmeta&lt;/code&gt; to discover sub-task issue types), and&lt;/li&gt;  &lt;li&gt;you must provide a &lt;code&gt;parent&lt;/code&gt; field in the issue create request containing the id or key of the  parent issue.&lt;/li&gt;  &lt;/ul&gt;


    """
    return web.Response(status=200)


async def create_issue_link_type(request: web.Request, ) -> web.Response:
    """create_issue_link_type

    Create a new issue link type.


    """
    return web.Response(status=200)


async def create_issue_type(request: web.Request, ) -> web.Response:
    """create_issue_type

    Creates an issue type from a JSON representation and adds the issue newly created issue type to the default issue  type scheme.


    """
    return web.Response(status=200)


async def create_issues(request: web.Request, ) -> web.Response:
    """create_issues

    Creates issues or sub-tasks from a JSON representation.  &lt;p/&gt;  Creates many issues in one bulk operation.  &lt;p/&gt;  Creating a sub-task is similar to creating a regular issue. More details can be found in createIssue section:  {@link IssueResource#createIssue(IssueUpdateBean)}}


    """
    return web.Response(status=200)


async def create_or_update_remote_issue_link(request: web.Request, issue_id_or_key) -> web.Response:
    """create_or_update_remote_issue_link

    Creates or updates a remote issue link from a JSON representation. If a globalId is provided and a remote issue link  exists with that globalId, the remote issue link is updated. Otherwise, the remote issue link is created.

    :param issue_id_or_key: the issue to create the remote issue link for
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def create_permission_grant(request: web.Request, scheme_id, expand=None) -> web.Response:
    """create_permission_grant

    Creates a permission grant in a permission scheme.

    :param scheme_id: 
    :type scheme_id: int
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def create_permission_scheme(request: web.Request, expand=None) -> web.Response:
    """create_permission_scheme

    Create a new permission scheme.  This method can create schemes with a defined permission set, or without.

    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def create_project(request: web.Request, ) -> web.Response:
    """create_project

    Creates a new project.


    """
    return web.Response(status=200)


async def create_project_category(request: web.Request, ) -> web.Response:
    """create_project_category

    Create a project category via POST.


    """
    return web.Response(status=200)


async def create_project_role(request: web.Request, ) -> web.Response:
    """create_project_role

    Creates a new ProjectRole to be available in JIRA.  The created role does not have any default actors assigned.


    """
    return web.Response(status=200)


async def create_property(request: web.Request, id, key=None, workflow_name=None, workflow_mode=None) -> web.Response:
    """create_property

    Add a new property to a transition. Trying to add a property that already  exists will fail.

    :param id: the ID of the transition within the workflow.
    :type id: int
    :param key: the name of the property to add.
    :type key: str
    :param workflow_name: the name of the workflow to use.
    :type workflow_name: str
    :param workflow_mode: the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;.
    :type workflow_mode: str

    """
    return web.Response(status=200)


async def create_scheme(request: web.Request, ) -> web.Response:
    """create_scheme

    Create a new workflow scheme.  &lt;p/&gt;  The body contains a representation of the new scheme. Values not passed are assumed to be set to their defaults.


    """
    return web.Response(status=200)


async def create_user(request: web.Request, ) -> web.Response:
    """create_user

    Create user. By default created user will not be notified with email.  If password field is not set then password will be randomly generated.


    """
    return web.Response(status=200)


async def create_version(request: web.Request, ) -> web.Response:
    """create_version

    Create a version via POST.


    """
    return web.Response(status=200)


async def current_user(request: web.Request, ) -> web.Response:
    """current_user

    Returns information about the currently authenticated user&#39;s session. If the caller is not authenticated they  will get a 401 Unauthorized status code.


    """
    return web.Response(status=200)


async def delete_actor(request: web.Request, project_id_or_key, id, user=None, group=None) -> web.Response:
    """delete_actor

    Deletes actors (users or groups) from a project role.  &lt;p&gt;  &lt;ul&gt;  &lt;li&gt;Delete a user from the role: &lt;code&gt;/rest/api/2/project/{projectIdOrKey}/role/{roleId}?user&#x3D;{username}&lt;/code&gt;&lt;/li&gt;  &lt;li&gt;Delete a group from the role: &lt;code&gt;/rest/api/2/project/{projectIdOrKey}/role/{roleId}?group&#x3D;{groupname}&lt;/code&gt;&lt;/li&gt;  &lt;/ul&gt;

    :param project_id_or_key: the project id or project key
    :type project_id_or_key: str
    :param id: the project role id
    :type id: int
    :param user: the username to remove from the project role
    :type user: str
    :param group: the groupname to remove from the project role
    :type group: str

    """
    return web.Response(status=200)


async def delete_comment(request: web.Request, issue_id_or_key, id) -> web.Response:
    """delete_comment

    Deletes an existing comment .

    :param issue_id_or_key: of the issue the comment belongs to
    :type issue_id_or_key: str
    :param id: the ID of the comment to request
    :type id: str

    """
    return web.Response(status=200)


async def delete_default(request: web.Request, id, update_draft_if_needed=None) -> web.Response:
    """delete_default

    Remove the default workflow from the passed workflow scheme.

    :param id: the id of the scheme.
    :type id: int
    :param update_draft_if_needed: when true will create and return a draft when the workflow scheme cannot be edited                             (e.g. when it is being used by a project).
    :type update_draft_if_needed: bool

    """
    return web.Response(status=200)


async def delete_draft_by_id(request: web.Request, id) -> web.Response:
    """delete_draft_by_id

    Delete the passed draft workflow scheme.

    :param id: the id of the parent scheme.
    :type id: int

    """
    return web.Response(status=200)


async def delete_draft_default(request: web.Request, id) -> web.Response:
    """delete_draft_default

    Remove the default workflow from the passed draft workflow scheme.

    :param id: the id of the parent scheme.
    :type id: int

    """
    return web.Response(status=200)


async def delete_draft_issue_type(request: web.Request, issue_type, id) -> web.Response:
    """delete_draft_issue_type

    Remove the specified issue type mapping from the draft scheme.

    :param issue_type: the issue type being set.
    :type issue_type: str
    :param id: the id of the parent scheme.
    :type id: int

    """
    return web.Response(status=200)


async def delete_draft_workflow_mapping(request: web.Request, id, workflow_name=None) -> web.Response:
    """delete_draft_workflow_mapping

    Delete the passed workflow from the draft workflow scheme.

    :param id: the id of the parent scheme.
    :type id: int
    :param workflow_name: the name of the workflow to delete.
    :type workflow_name: str

    """
    return web.Response(status=200)


async def delete_filter(request: web.Request, id) -> web.Response:
    """delete_filter

    Delete a filter.

    :param id: the id of the filter being looked up
    :type id: int

    """
    return web.Response(status=200)


async def delete_issue(request: web.Request, issue_id_or_key, delete_subtasks=None) -> web.Response:
    """delete_issue

    Delete an issue.  &lt;p/&gt;  If the issue has subtasks you must set the parameter deleteSubtasks&#x3D;true to delete the issue.  You cannot delete an issue without its subtasks also being deleted.

    :param issue_id_or_key: the issue id or key to update (i.e. JRA-1330)
    :type issue_id_or_key: str
    :param delete_subtasks: a String of true or false indicating that any subtasks should also be deleted.  If the                        issue has no subtasks this parameter is ignored.  If the issue has subtasks and this parameter is missing or false,                        then the issue will not be deleted and an error will be returned.
    :type delete_subtasks: str

    """
    return web.Response(status=200)


async def delete_issue_link(request: web.Request, link_id) -> web.Response:
    """delete_issue_link

    Deletes an issue link with the specified id.  To be able to delete an issue link you must be able to view both issues and must have the link issue permission  for at least one of the issues.

    :param link_id: the issue link id.
    :type link_id: str

    """
    return web.Response(status=200)


async def delete_issue_link_type(request: web.Request, issue_link_type_id) -> web.Response:
    """delete_issue_link_type

    Delete the specified issue link type.

    :param issue_link_type_id: 
    :type issue_link_type_id: str

    """
    return web.Response(status=200)


async def delete_permission_scheme(request: web.Request, scheme_id) -> web.Response:
    """delete_permission_scheme

    Deletes a permission scheme identified by the given id.

    :param scheme_id: 
    :type scheme_id: int

    """
    return web.Response(status=200)


async def delete_permission_scheme_entity(request: web.Request, permission_id, scheme_id) -> web.Response:
    """delete_permission_scheme_entity

    Deletes a permission grant from a permission scheme.

    :param permission_id: 
    :type permission_id: int
    :param scheme_id: 
    :type scheme_id: int

    """
    return web.Response(status=200)


async def delete_project(request: web.Request, project_id_or_key) -> web.Response:
    """delete_project

    Deletes a project.

    :param project_id_or_key: the project id or project key
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def delete_project_role(request: web.Request, id, swap=None) -> web.Response:
    """delete_project_role

    Deletes a role. May return 403 in the future

    :param id: 
    :type id: int
    :param swap: if given, removes a role even if it is used in scheme by replacing the role with the given one
    :type swap: int

    """
    return web.Response(status=200)


async def delete_project_role_actors_from_role(request: web.Request, id, user=None, group=None) -> web.Response:
    """delete_project_role_actors_from_role

    Removes default actor from the given role.

    :param id: the role id to remove the actors from
    :type id: int
    :param user: if given, removes an actor from given role
    :type user: str
    :param group: if given, removes an actor from given role
    :type group: str

    """
    return web.Response(status=200)


async def delete_remote_issue_link_by_global_id(request: web.Request, issue_id_or_key, global_id=None) -> web.Response:
    """delete_remote_issue_link_by_global_id

    Delete the remote issue link with the given global id on the issue.

    :param issue_id_or_key: the issue to create the remote issue link for
    :type issue_id_or_key: str
    :param global_id: the global id of the remote issue link
    :type global_id: str

    """
    return web.Response(status=200)


async def delete_remote_issue_link_by_id(request: web.Request, link_id, issue_id_or_key) -> web.Response:
    """delete_remote_issue_link_by_id

    Delete the remote issue link with the given id on the issue.

    :param link_id: the id of the remote issue link
    :type link_id: str
    :param issue_id_or_key: the issue to create the remote issue link for
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def delete_remote_version_link(request: web.Request, version_id, global_id) -> web.Response:
    """delete_remote_version_link

    Delete a specific remote version link with the given version ID and global ID.

    :param version_id: The version ID of the remote link
    :type version_id: str
    :param global_id: The global ID of the remote link
    :type global_id: str

    """
    return web.Response(status=200)


async def delete_remote_version_links_by_version_id(request: web.Request, version_id) -> web.Response:
    """delete_remote_version_links_by_version_id

    Delete all remote version links for a given version ID.

    :param version_id: The version for which to delete ALL existing remote version links
    :type version_id: str

    """
    return web.Response(status=200)


async def delete_scheme(request: web.Request, id) -> web.Response:
    """delete_scheme

    Delete the passed workflow scheme.

    :param id: the id of the scheme.
    :type id: int

    """
    return web.Response(status=200)


async def delete_tab(request: web.Request, screen_id, tab_id) -> web.Response:
    """delete_tab

    Deletes tab to give screen

    :param screen_id: id of screen
    :type screen_id: int
    :param tab_id: id of tab
    :type tab_id: int

    """
    return web.Response(status=200)


async def delete_workflow_mapping(request: web.Request, id, workflow_name=None, update_draft_if_needed=None) -> web.Response:
    """delete_workflow_mapping

    Delete the passed workflow from the workflow scheme.

    :param id: the id of the scheme.
    :type id: int
    :param workflow_name: the name of the workflow to delete.
    :type workflow_name: str
    :param update_draft_if_needed: flag to indicate if a draft should be created if necessary to delete the workflow                             from the scheme.
    :type update_draft_if_needed: bool

    """
    return web.Response(status=200)


async def delete_worklog(request: web.Request, issue_id_or_key, id, adjust_estimate=None, new_estimate=None, increase_by=None) -> web.Response:
    """delete_worklog

    Deletes an existing worklog entry.

    :param issue_id_or_key: a string containing the issue id or key the worklog belongs to
    :type issue_id_or_key: str
    :param id: id of the worklog to be deleted
    :type id: str
    :param adjust_estimate: (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        &lt;ul&gt;                        &lt;li&gt;\&quot;new\&quot; - sets the estimate to a specific value&lt;/li&gt;                        &lt;li&gt;\&quot;leave\&quot;- leaves the estimate as is&lt;/li&gt;                        &lt;li&gt;\&quot;manual\&quot; - specify a specific amount to increase remaining estimate by&lt;/li&gt;                        &lt;li&gt;\&quot;auto\&quot;- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog&lt;/li&gt; &lt;/ul&gt;
    :type adjust_estimate: str
    :param new_estimate: (required when \&quot;new\&quot; is selected for adjustEstimate) the new value for the remaining estimate field. e.g. \&quot;2d\&quot;
    :type new_estimate: str
    :param increase_by: (required when \&quot;manual\&quot; is selected for adjustEstimate) the amount to increase the remaining estimate by e.g. \&quot;2d\&quot;
    :type increase_by: str

    """
    return web.Response(status=200)


async def do_transition(request: web.Request, issue_id_or_key) -> web.Response:
    """do_transition

    Perform a transition on an issue.  When performing the transition you can update or set other issue fields.  &lt;p/&gt;  The fields that can be set on transtion, in either the fields parameter or the update parameter can be determined  using the &lt;b&gt;/rest/api/2/issue/{issueIdOrKey}/transitions?expand&#x3D;transitions.fields&lt;/b&gt; resource.  If a field is not configured to appear on the transition screen, then it will not be in the transition metadata, and a field  validation error will occur if it is submitted.

    :param issue_id_or_key: the issue whose transitions you want to view
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def edit_filter(request: web.Request, id, expand=None) -> web.Response:
    """edit_filter

    Updates an existing filter, and returns its new value.

    :param id: the id of the filter being looked up
    :type id: int
    :param expand: the parameters to expand
    :type expand: str

    """
    return web.Response(status=200)


async def edit_issue(request: web.Request, issue_id_or_key, notify_users=None) -> web.Response:
    """edit_issue

    Edits an issue from a JSON representation.  &lt;p/&gt;  The issue can either be updated by setting explicit the field value(s)  or by using an operation to change the field value.  &lt;p/&gt;  The fields that can be updated, in either the fields parameter or the update parameter, can be determined  using the &lt;b&gt;/rest/api/2/issue/{issueIdOrKey}/editmeta&lt;/b&gt; resource.&lt;br&gt;  If a field is not configured to appear on the edit screen, then it will not be in the editmeta, and a field  validation error will occur if it is submitted.  &lt;p/&gt;  Specifying a \&quot;field_id\&quot;: field_value in the \&quot;fields\&quot; is a shorthand for a \&quot;set\&quot; operation in the \&quot;update\&quot; section.&lt;br&gt;  Field should appear either in \&quot;fields\&quot; or \&quot;update\&quot;, not in both.

    :param issue_id_or_key: the issue id or key to update (i.e. JRA-1330)
    :type issue_id_or_key: str
    :param notify_users: send the email with notification that the issue was updated to users that watch it.                     Admin or project admin permissions are required to disable the notification.
    :type notify_users: bool

    """
    return web.Response(status=200)


async def expand_for_humans(request: web.Request, id) -> web.Response:
    """expand_for_humans

    Tries to expand an attachment. Output is human-readable and subject to change.

    :param id: the id of the attachment to expand.
    :type id: str

    """
    return web.Response(status=200)


async def expand_for_machines(request: web.Request, id) -> web.Response:
    """expand_for_machines

    Tries to expand an attachment. Output is raw and should be backwards-compatible through the course of time.

    :param id: the id of the attachment to expand.
    :type id: str

    """
    return web.Response(status=200)


async def find_assignable_users(request: web.Request, username=None, project=None, issue_key=None, start_at=None, max_results=None, action_descriptor_id=None) -> web.Response:
    """find_assignable_users

    Returns a list of users that match the search string. This resource cannot be accessed anonymously.  Please note that this resource should be called with an issue key when a list of assignable users is retrieved  for editing.  For create only a project key should be supplied.  The list of assignable users may be incorrect  if it&#39;s called with the project key for editing.

    :param username: the username
    :type username: str
    :param project: the key of the project we are finding assignable users for
    :type project: str
    :param issue_key: the issue key for the issue being edited we need to find assignable users for.
    :type issue_key: str
    :param start_at: the index of the first user to return (0-based)
    :type start_at: int
    :param max_results: the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated.
    :type max_results: int
    :param action_descriptor_id: 
    :type action_descriptor_id: int

    """
    return web.Response(status=200)


async def find_bulk_assignable_users(request: web.Request, username=None, project_keys=None, start_at=None, max_results=None) -> web.Response:
    """find_bulk_assignable_users

    Returns a list of users that match the search string and can be assigned issues for all the given projects.  This resource cannot be accessed anonymously.

    :param username: the username
    :type username: str
    :param project_keys: the keys of the projects we are finding assignable users for, comma-separated
    :type project_keys: str
    :param start_at: the index of the first user to return (0-based)
    :type start_at: int
    :param max_results: the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                        If you specify a value that is higher than this number, your search results will be truncated.
    :type max_results: int

    """
    return web.Response(status=200)


async def find_groups(request: web.Request, query=None, exclude=None, max_results=None, user_name=None) -> web.Response:
    """find_groups

    Returns groups with substrings matching a given query. This is mainly for use with  the group picker, so the returned groups contain html to be used as picker suggestions.  The groups are also wrapped in a single response object that also contains a header for  use in the picker, specifically &lt;i&gt;Showing X of Y matching groups&lt;/i&gt;.  &lt;p&gt;  The number of groups returned is limited by the system property \&quot;jira.ajax.autocomplete.limit\&quot;  &lt;p&gt;  The groups will be unique and sorted.

    :param query: a String to match groups agains
    :type query: str
    :param exclude: 
    :type exclude: str
    :param max_results: 
    :type max_results: int
    :param user_name: 
    :type user_name: str

    """
    return web.Response(status=200)


async def find_users(request: web.Request, username=None, start_at=None, max_results=None, include_active=None, include_inactive=None) -> web.Response:
    """find_users

    Returns a list of users that match the search string. This resource cannot be accessed anonymously.

    :param username: A query string used to search username, name or e-mail address
    :type username: str
    :param start_at: the index of the first user to return (0-based)
    :type start_at: int
    :param max_results: the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                         If you specify a value that is higher than this number, your search results will be truncated.
    :type max_results: int
    :param include_active: If true, then active users are included in the results (default true)
    :type include_active: bool
    :param include_inactive: If true, then inactive users are included in the results (default false)
    :type include_inactive: bool

    """
    return web.Response(status=200)


async def find_users_and_groups(request: web.Request, query=None, max_results=None, show_avatar=None, field_id=None, project_id=None, issue_type_id=None) -> web.Response:
    """find_users_and_groups

    Returns a list of users and groups matching query with highlighting. This resource cannot be accessed  anonymously.

    :param query: A string used to search username, Name or e-mail address
    :type query: str
    :param max_results: the maximum number of users to return (defaults to 50). The maximum allowed value is 1000. If                     you specify a value that is higher than this number, your search results will be truncated.
    :type max_results: int
    :param show_avatar: 
    :type show_avatar: bool
    :param field_id: The custom field id, if this request comes from a custom field, such as a user picker. Optional.
    :type field_id: str
    :param project_id: The list of project ids to further restrict the search                     This parameter can occur multiple times to pass in multiple project ids.                     Comma separated value is not supported.                     This parameter is only used when fieldId is present.
    :type project_id: str
    :param issue_type_id: The list of issue type ids to further restrict the search.                     This parameter can occur multiple times to pass in multiple issue type ids.                     Comma separated value is not supported.                     Special values such as -1 (all standard issue types), -2 (all subtask issue types) are supported.                     This parameter is only used when fieldId is present.
    :type issue_type_id: str

    """
    return web.Response(status=200)


async def find_users_for_picker(request: web.Request, query=None, max_results=None, show_avatar=None, exclude=None) -> web.Response:
    """find_users_for_picker

    Returns a list of users matching query with highlighting. This resource cannot be accessed anonymously.

    :param query: A string used to search username, Name or e-mail address
    :type query: str
    :param max_results: the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated.
    :type max_results: int
    :param show_avatar: 
    :type show_avatar: bool
    :param exclude: 
    :type exclude: str

    """
    return web.Response(status=200)


async def find_users_with_all_permissions(request: web.Request, username=None, permissions=None, issue_key=None, project_key=None, start_at=None, max_results=None) -> web.Response:
    """find_users_with_all_permissions

    Returns a list of active users that match the search string and have all specified permissions for the project or issue.&lt;br&gt;  This resource can be accessed by users with ADMINISTER_PROJECT permission for the project or global ADMIN or SYSADMIN rights.

    :param username: the username filter, list includes all users if unspecified
    :type username: str
    :param permissions: comma separated list of permissions for project or issue returned users must have, see                     &lt;a href&#x3D;\&quot;https://developer.atlassian.com/static/javadoc/jira/6.0/reference/com/atlassian/jira/security/Permissions.Permission.html\&quot;&gt;Permissions&lt;/a&gt;                     JavaDoc for the list of all possible permissions.
    :type permissions: str
    :param issue_key: the issue key for the issue for which returned users have specified permissions.
    :type issue_key: str
    :param project_key: the optional project key to search for users with if no issueKey is supplied.
    :type project_key: str
    :param start_at: the index of the first user to return (0-based)
    :type start_at: int
    :param max_results: the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                     If you specify a value that is higher than this number, your search results will be truncated.
    :type max_results: int

    """
    return web.Response(status=200)


async def find_users_with_browse_permission(request: web.Request, username=None, issue_key=None, project_key=None, start_at=None, max_results=None) -> web.Response:
    """find_users_with_browse_permission

    Returns a list of active users that match the search string. This resource cannot be accessed anonymously   and requires the Browse Users global permission.  Given an issue key this resource will provide a list of users that match the search string and have  the browse issue permission for the issue provided.

    :param username: the username filter, no users returned if left blank
    :type username: str
    :param issue_key: the issue key for the issue being edited we need to find viewable users for.
    :type issue_key: str
    :param project_key: the optional project key to search for users with if no issueKey is supplied.
    :type project_key: str
    :param start_at: the index of the first user to return (0-based)
    :type start_at: int
    :param max_results: the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated.
    :type max_results: int

    """
    return web.Response(status=200)


async def fully_update_project_role(request: web.Request, id) -> web.Response:
    """fully_update_project_role

    Fully updates a roles. Both name and description must be given.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get(request: web.Request, key) -> web.Response:
    """get

    Returns the ApplicationRole with passed key if it exists.

    :param key: the key of the role to update.
    :type key: str

    """
    return web.Response(status=200)


async def get_accessible_project_type_by_key(request: web.Request, project_type_key) -> web.Response:
    """get_accessible_project_type_by_key

    Returns the project type with the given key, if it is accessible to the logged in user.  This takes into account whether the user is licensed on the Application that defines the project type.

    :param project_type_key: 
    :type project_type_key: str

    """
    return web.Response(status=200)


async def get_advanced_settings(request: web.Request, ) -> web.Response:
    """get_advanced_settings

    Returns the properties that are displayed on the \&quot;General Configuration &gt; Advanced Settings\&quot; page.


    """
    return web.Response(status=200)


async def get_all(request: web.Request, ) -> web.Response:
    """get_all

    Returns all ApplicationRoles in the system. Will also return an ETag header containing a version hash of the  collection of ApplicationRoles.


    """
    return web.Response(status=200)


async def get_all_fields(request: web.Request, screen_id, tab_id, project_key=None) -> web.Response:
    """get_all_fields

    Gets all fields for a given tab

    :param screen_id: id of screen
    :type screen_id: int
    :param tab_id: id of tab
    :type tab_id: int
    :param project_key: the key of the project; this parameter is optional
    :type project_key: str

    """
    return web.Response(status=200)


async def get_all_permissions(request: web.Request, ) -> web.Response:
    """get_all_permissions

    Returns all permissions that are present in the JIRA instance - Global, Project and the global ones added by plugins


    """
    return web.Response(status=200)


async def get_all_project_categories(request: web.Request, ) -> web.Response:
    """get_all_project_categories

    Returns all project categories


    """
    return web.Response(status=200)


async def get_all_project_types(request: web.Request, ) -> web.Response:
    """get_all_project_types

    Returns all the project types defined on the JIRA instance, not taking into account whether  the license to use those project types is valid or not.


    """
    return web.Response(status=200)


async def get_all_projects(request: web.Request, expand=None, recent=None) -> web.Response:
    """get_all_projects

    Returns all projects which are visible for the currently logged in user. If no user is logged in, it returns the  list of projects that are visible when using anonymous access.

    :param expand: the parameters to expand
    :type expand: str
    :param recent: if this parameter is set then only projects recently accessed by the current user (if not logged in then based on HTTP session) will be returned (maximum count limited to the specified number but no more than 20).
    :type recent: int

    """
    return web.Response(status=200)


async def get_all_statuses(request: web.Request, project_id_or_key) -> web.Response:
    """get_all_statuses

    Get all issue types with valid status values for a project

    :param project_id_or_key: Project id or project key
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def get_all_system_avatars(request: web.Request, type) -> web.Response:
    """get_all_system_avatars

    Returns all system avatars of the given type.

    :param type: the avatar type
    :type type: str

    """
    return web.Response(status=200)


async def get_all_tabs(request: web.Request, screen_id, project_key=None) -> web.Response:
    """get_all_tabs

    Returns a list of all tabs for the given screen

    :param screen_id: id of screen
    :type screen_id: int
    :param project_key: the key of the project; this parameter is optional
    :type project_key: str

    """
    return web.Response(status=200)


async def get_all_workflows(request: web.Request, workflow_name=None) -> web.Response:
    """get_all_workflows

    Returns all workflows.

    :param workflow_name: 
    :type workflow_name: str

    """
    return web.Response(status=200)


async def get_alternative_issue_types(request: web.Request, id) -> web.Response:
    """get_alternative_issue_types

    Returns a list of all alternative issue types for the given issue type id. The list will contain these issues types, to which  issues assigned to the given issue type can be migrated. The suitable alternatives are issue types which are assigned  to the same workflow, the same field configuration and the same screen scheme.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_assigned_permission_scheme(request: web.Request, project_key_or_id, expand=None) -> web.Response:
    """get_assigned_permission_scheme

    Gets a permission scheme assigned with a project.

    :param project_key_or_id: key or id of the project
    :type project_key_or_id: str
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def get_attachment(request: web.Request, id) -> web.Response:
    """get_attachment

    Returns the meta-data for an attachment, including the URI of the actual attached file.

    :param id: id of the attachment to remove
    :type id: str

    """
    return web.Response(status=200)


async def get_attachment_meta(request: web.Request, ) -> web.Response:
    """get_attachment_meta

    Returns the meta information for an attachments, specifically if they are enabled and the maximum upload size  allowed.


    """
    return web.Response(status=200)


async def get_auto_complete(request: web.Request, ) -> web.Response:
    """get_auto_complete

    Returns the auto complete data required for JQL searches.


    """
    return web.Response(status=200)


async def get_available_metrics(request: web.Request, ) -> web.Response:
    """get_available_metrics

    


    """
    return web.Response(status=200)


async def get_avatars(request: web.Request, type, owning_object_id) -> web.Response:
    """get_avatars

    

    :param type: 
    :type type: str
    :param owning_object_id: 
    :type owning_object_id: str

    """
    return web.Response(status=200)


async def get_by_id(request: web.Request, id, return_draft_if_exists=None) -> web.Response:
    """get_by_id

    Returns the requested workflow scheme to the caller.

    :param id: the id of the scheme.
    :type id: int
    :param return_draft_if_exists: when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself.
    :type return_draft_if_exists: bool

    """
    return web.Response(status=200)


async def get_comment(request: web.Request, issue_id_or_key, id, expand=None) -> web.Response:
    """get_comment

    Returns a single comment.

    :param issue_id_or_key: of the issue the comment belongs to
    :type issue_id_or_key: str
    :param id: the ID of the comment to request
    :type id: str
    :param expand: optional flags: renderedBody (provides body rendered in HTML)
    :type expand: str

    """
    return web.Response(status=200)


async def get_comments(request: web.Request, issue_id_or_key, start_at=None, max_results=None, order_by=None, expand=None) -> web.Response:
    """get_comments

    Returns all comments for an issue.  &lt;p&gt;  Results can be ordered by the \&quot;created\&quot; field which means the date a comment was added.  &lt;/p&gt;

    :param issue_id_or_key: a string containing the issue id or key the comment will be added to
    :type issue_id_or_key: str
    :param start_at: the page offset, if not specified then defaults to 0
    :type start_at: int
    :param max_results: how many results on the page should be included. Defaults to 50.
    :type max_results: int
    :param order_by: ordering of the results.
    :type order_by: str
    :param expand: optional flags: renderedBody (provides body rendered in HTML)
    :type expand: str

    """
    return web.Response(status=200)


async def get_component(request: web.Request, id) -> web.Response:
    """get_component

    Returns a project component.

    :param id: The component to delete.
    :type id: str

    """
    return web.Response(status=200)


async def get_component_related_issues(request: web.Request, id) -> web.Response:
    """get_component_related_issues

    Returns counts of issues related to this component.

    :param id: a String containing the component id
    :type id: str

    """
    return web.Response(status=200)


async def get_configuration(request: web.Request, ) -> web.Response:
    """get_configuration

    Returns the information if the optional features in JIRA are enabled or disabled. If the time tracking is enabled,  it also returns the detailed information about time tracking configuration.


    """
    return web.Response(status=200)


async def get_create_issue_meta(request: web.Request, project_ids=None, project_keys=None, issuetype_ids=None, issuetype_names=None) -> web.Response:
    """get_create_issue_meta

    Returns the meta data for creating issues. This includes the available projects, issue types and fields,  including field types and whether or not those fields are required.  Projects will not be returned if the user does not have permission to create issues in that project.  &lt;p/&gt;  The fields in the createmeta correspond to the fields in the create screen for the project/issuetype.  Fields not in the screen will not be in the createmeta.  &lt;p/&gt;  Fields will only be returned if &lt;code&gt;expand&#x3D;projects.issuetypes.fields&lt;/code&gt;.  &lt;p/&gt;  The results can be filtered by project and/or issue type, given by the query params.

    :param project_ids: combined with the projectKeys param, lists the projects with which to filter the results. If absent, all projects are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results.
    :type project_ids: str
    :param project_keys: combined with the projectIds param, lists the projects with which to filter the results. If null, all projects are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results.
    :type project_keys: str
    :param issuetype_ids: combinded with issuetypeNames, lists the issue types with which to filter the results. If null, all issue types are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying an issue type that does not exist is not an error.
    :type issuetype_ids: str
    :param issuetype_names: combinded with issuetypeIds, lists the issue types with which to filter the results. If null, all issue types are returned.                        This parameter can be specified multiple times, but is NOT interpreted as a comma-separated list.                        Specifiying an issue type that does not exist is not an error.
    :type issuetype_names: str

    """
    return web.Response(status=200)


async def get_custom_field_option(request: web.Request, id) -> web.Response:
    """get_custom_field_option

    Returns a full representation of the Custom Field Option that has the given id.

    :param id: a String containing an Custom Field Option id
    :type id: str

    """
    return web.Response(status=200)


async def get_dashboard(request: web.Request, id) -> web.Response:
    """get_dashboard

    Returns a single dashboard.

    :param id: the dashboard id
    :type id: str

    """
    return web.Response(status=200)


async def get_default(request: web.Request, id, return_draft_if_exists=None) -> web.Response:
    """get_default

    Return the default workflow from the passed workflow scheme.

    :param id: the id of the scheme.
    :type id: int
    :param return_draft_if_exists: when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself.
    :type return_draft_if_exists: bool

    """
    return web.Response(status=200)


async def get_default_share_scope(request: web.Request, ) -> web.Response:
    """get_default_share_scope

    Returns the default share scope of the logged-in user.


    """
    return web.Response(status=200)


async def get_draft_by_id(request: web.Request, id) -> web.Response:
    """get_draft_by_id

    Returns the requested draft workflow scheme to the caller.

    :param id: the id of the parent scheme.
    :type id: int

    """
    return web.Response(status=200)


async def get_draft_default(request: web.Request, id) -> web.Response:
    """get_draft_default

    Return the default workflow from the passed draft workflow scheme to the caller.

    :param id: the id of the parent scheme.
    :type id: int

    """
    return web.Response(status=200)


async def get_draft_issue_type(request: web.Request, issue_type, id) -> web.Response:
    """get_draft_issue_type

    Returns the issue type mapping for the passed draft workflow scheme.

    :param issue_type: the issue type being set.
    :type issue_type: str
    :param id: the id of the parent scheme.
    :type id: int

    """
    return web.Response(status=200)


async def get_draft_workflow(request: web.Request, id, workflow_name=None) -> web.Response:
    """get_draft_workflow

    Returns the draft workflow mappings or requested mapping to the caller.

    :param id: the id of the parent scheme.
    :type id: int
    :param workflow_name: the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name.
    :type workflow_name: str

    """
    return web.Response(status=200)


async def get_edit_issue_meta(request: web.Request, issue_id_or_key) -> web.Response:
    """get_edit_issue_meta

    Returns the meta data for editing an issue.  &lt;p/&gt;  The fields in the editmeta correspond to the fields in the edit screen for the issue.  Fields not in the screen will not be in the editmeta.

    :param issue_id_or_key: the issue whose edit meta data you want to view
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def get_favourite_filters(request: web.Request, expand=None, enable_shared_users=None) -> web.Response:
    """get_favourite_filters

    Returns the favourite filters of the logged-in user.

    :param expand: the parameters to expand
    :type expand: str
    :param enable_shared_users: enable calculating shared users collection
    :type enable_shared_users: bool

    """
    return web.Response(status=200)


async def get_field_auto_complete_for_query_string(request: web.Request, field_name=None, field_value=None, predicate_name=None, predicate_value=None) -> web.Response:
    """get_field_auto_complete_for_query_string

    Returns auto complete suggestions for JQL search.

    :param field_name: the field name for which the suggestions are generated.
    :type field_name: str
    :param field_value: the portion of the field value that has already been provided by the user.
    :type field_value: str
    :param predicate_name: the predicate for which the suggestions are generated. Suggestions are generated only for: \&quot;by\&quot;, \&quot;from\&quot; and \&quot;to\&quot;.
    :type predicate_name: str
    :param predicate_value: the portion of the predicate value that has already been provided by the user.
    :type predicate_value: str

    """
    return web.Response(status=200)


async def get_fields(request: web.Request, ) -> web.Response:
    """get_fields

    Returns a list of all fields, both System and Custom


    """
    return web.Response(status=200)


async def get_fields_to_add(request: web.Request, screen_id) -> web.Response:
    """get_fields_to_add

    Gets available fields for screen. i.e ones that haven&#39;t already been added.

    :param screen_id: id of screen
    :type screen_id: int

    """
    return web.Response(status=200)


async def get_filter(request: web.Request, id, expand=None, enable_shared_users=None) -> web.Response:
    """get_filter

    Returns a filter given an id

    :param id: the id of the filter being looked up
    :type id: int
    :param expand: the parameters to expand
    :type expand: str
    :param enable_shared_users: enable calculating shared users collection
    :type enable_shared_users: bool

    """
    return web.Response(status=200)


async def get_group(request: web.Request, groupname=None, expand=None) -> web.Response:
    """get_group

    Returns REST representation for the requested group. Allows to get list of active users belonging to the  specified group and its subgroups if \&quot;users\&quot; expand option is provided. You can page through users list by using  indexes in expand param. For example to get users from index 10 to index 15 use \&quot;users[10:15]\&quot; expand value. This  will return 6 users (if there are at least 16 users in this group). Indexes are 0-based and inclusive.  &lt;p&gt;  This resource is deprecated, please use group/member API instead.

    :param groupname: A name of requested group.
    :type groupname: str
    :param expand: List of fields to expand. Currently only available expand is \&quot;users\&quot;.
    :type expand: str

    """
    return web.Response(status=200)


async def get_ids_of_worklogs_deleted_since(request: web.Request, since=None) -> web.Response:
    """get_ids_of_worklogs_deleted_since

    Returns worklogs id and delete time of worklogs that was deleted since given time.  The returns set of worklogs is limited to 1000 elements.  This API will not return worklogs deleted during last minute.

    :param since: a date time in unix timestamp format since when deleted worklogs will be returned.
    :type since: int

    """
    return web.Response(status=200)


async def get_ids_of_worklogs_modified_since(request: web.Request, since=None) -> web.Response:
    """get_ids_of_worklogs_modified_since

    Returns worklogs id and update time of worklogs that was updated since given time.  The returns set of worklogs is limited to 1000 elements.  This API will not return worklogs updated during last minute.

    :param since: a date time in unix timestamp format since when updated worklogs will be returned.
    :type since: int

    """
    return web.Response(status=200)


async def get_index_summary(request: web.Request, ) -> web.Response:
    """get_index_summary

    Summarizes index condition of current node.  &lt;p/&gt;  Returned data consists of:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;nodeId&lt;/code&gt; - Node identifier.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;reportTime&lt;/code&gt; - Time of this report creation.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;issueIndex&lt;/code&gt; - Summary of issue index status.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;replicationQueues&lt;/code&gt; - Map of index replication queues, where  keys represent nodes from which replication operations came from.&lt;/li&gt;  &lt;/ul&gt;  &lt;p/&gt;  &lt;code&gt;issueIndex&lt;/code&gt; can contain:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;indexReadable&lt;/code&gt; - If &lt;code&gt;false&lt;/code&gt; the end point failed to read data from issue index  (check JIRA logs for detailed stack trace), otherwise &lt;code&gt;true&lt;/code&gt;.  When &lt;code&gt;false&lt;/code&gt; other fields of &lt;code&gt;issueIndex&lt;/code&gt; can be not visible.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;countInDatabase&lt;/code&gt; - Count of issues found in database.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;countInIndex&lt;/code&gt; - Count of issues found while querying index.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastUpdatedInDatabase&lt;/code&gt; - Time of last update of issue found in database.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastUpdatedInIndex&lt;/code&gt; - Time of last update of issue found while querying index.&lt;/li&gt;  &lt;/ul&gt;  &lt;p/&gt;  &lt;code&gt;replicationQueues&lt;/code&gt;&#39;s map values can contain:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;lastConsumedOperation&lt;/code&gt; - Last executed index replication operation by current node from sending node&#39;s queue.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastConsumedOperation.id&lt;/code&gt; - Identifier of the operation.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastConsumedOperation.replicationTime&lt;/code&gt; - Time when the operation was sent to other nodes.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastOperationInQueue&lt;/code&gt; - Last index replication operation in sending node&#39;s queue.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastOperationInQueue.id&lt;/code&gt; - Identifier of the operation.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastOperationInQueue.replicationTime&lt;/code&gt; - Time when the operation was sent to other nodes.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;queueSize&lt;/code&gt; - Number of operations in queue from sending node to current node.&lt;/li&gt;  &lt;/ul&gt;


    """
    return web.Response(status=200)


async def get_issue(request: web.Request, issue_id_or_key, fields=None, expand=None, properties=None) -> web.Response:
    """get_issue

    Returns a full representation of the issue for the given issue key.  &lt;p&gt;  An issue JSON consists of the issue key, a collection of fields,  a link to the workflow transition sub-resource, and (optionally) the HTML rendered values of any fields that support it  (e.g. if wiki syntax is enabled for the description or comments).  &lt;p&gt;  The &lt;code&gt;fields&lt;/code&gt; param (which can be specified multiple times) gives a comma-separated list of fields  to include in the response. This can be used to retrieve a subset of fields.  A particular field can be excluded by prefixing it with a minus.  &lt;p&gt;  By default, all (&lt;code&gt;*all&lt;/code&gt;) fields are returned in this get-issue resource. Note: the default is different  when doing a jql search -- the default there is just navigable fields (&lt;code&gt;*navigable&lt;/code&gt;).  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;*all&lt;/code&gt; - include all fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*navigable&lt;/code&gt; - include just navigable fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;summary,comment&lt;/code&gt; - include just the summary and comments&lt;/li&gt;  &lt;li&gt;&lt;code&gt;-comment&lt;/code&gt; - include everything except comments (the default is &lt;code&gt;*all&lt;/code&gt; for get-issue)&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*all,-comment&lt;/code&gt; - include everything except comments&lt;/li&gt;  &lt;/ul&gt;  &lt;p&gt;  The {@code properties} param is similar to {@code fields} and specifies a comma-separated list of issue  properties to include. Unlike {@code fields}, properties are not included by default. To include them all  send {@code ?properties&#x3D;*all}. You can also include only specified properties or exclude some properties  with a minus (-) sign.  &lt;p&gt;  &lt;ul&gt;  &lt;li&gt;{@code *all} - include all properties&lt;/li&gt;  &lt;li&gt;{@code *all, -prop1} - include all properties except {@code prop1} &lt;/li&gt;  &lt;li&gt;{@code prop1, prop1} - include {@code prop1} and {@code prop2} properties &lt;/li&gt;  &lt;/ul&gt;  &lt;/p&gt;  &lt;p/&gt;  JIRA will attempt to identify the issue by the &lt;code&gt;issueIdOrKey&lt;/code&gt; path parameter. This can be an issue id,  or an issue key. If the issue cannot be found via an exact match, JIRA will also look for the issue in a case-insensitive way, or  by looking to see if the issue was moved. In either of these cases, the request will proceed as normal (a 302 or other redirect  will &lt;b&gt;not&lt;/b&gt; be returned). The issue key contained in the response will indicate the current value of issue&#39;s key.  &lt;p/&gt;  The &lt;code&gt;expand&lt;/code&gt; param is used to include, hidden by default, parts of response. This can be used to include:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;renderedFields&lt;/code&gt; - field values in HTML format&lt;/li&gt;  &lt;li&gt;&lt;code&gt;names&lt;/code&gt; - display name of each field&lt;/li&gt;  &lt;li&gt;&lt;code&gt;schema&lt;/code&gt; - schema for each field which describes a type of the field&lt;/li&gt;  &lt;li&gt;&lt;code&gt;transitions&lt;/code&gt; - all possible transitions for the given issue&lt;/li&gt;  &lt;li&gt;&lt;code&gt;operations&lt;/code&gt; - all possibles operations which may be applied on issue&lt;/li&gt;  &lt;li&gt;&lt;code&gt;editmeta&lt;/code&gt; - information about how each field may be edited. It contains field&#39;s schema as well.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;changelog&lt;/code&gt; - history of all changes of the given issue&lt;/li&gt;  &lt;li&gt;&lt;code&gt;versionedRepresentations&lt;/code&gt; -  REST representations of all fields. Some field may contain more recent versions. RESET representations are numbered.  The greatest number always represents the most recent version. It is recommended that the most recent version is used.  version for these fields which provide a more recent REST representation.  After including &lt;code&gt;versionedRepresentations&lt;/code&gt; \&quot;fields\&quot; field become hidden.&lt;/li&gt;  &lt;/ul&gt;

    :param issue_id_or_key: the issue id or key to update (i.e. JRA-1330)
    :type issue_id_or_key: str
    :param fields: the list of fields to return for the issue. By default, all fields are returned.
    :type fields: str
    :param expand: 
    :type expand: str
    :param properties: the list of properties to return for the issue. By default no properties are returned.
    :type properties: str

    """
    return web.Response(status=200)


async def get_issue_all_types(request: web.Request, ) -> web.Response:
    """get_issue_all_types

    Returns a list of all issue types visible to the user


    """
    return web.Response(status=200)


async def get_issue_link(request: web.Request, link_id) -> web.Response:
    """get_issue_link

    Returns an issue link with the specified id.

    :param link_id: the issue link id.
    :type link_id: str

    """
    return web.Response(status=200)


async def get_issue_link_type(request: web.Request, issue_link_type_id) -> web.Response:
    """get_issue_link_type

    Returns for a given issue link type id all information about this issue link type.

    :param issue_link_type_id: 
    :type issue_link_type_id: str

    """
    return web.Response(status=200)


async def get_issue_link_types(request: web.Request, ) -> web.Response:
    """get_issue_link_types

    Returns a list of available issue link types, if issue linking is enabled.  Each issue link type has an id, a name and a label for the outward and inward link relationship.


    """
    return web.Response(status=200)


async def get_issue_navigator_default_columns(request: web.Request, ) -> web.Response:
    """get_issue_navigator_default_columns

    Returns the default system columns for issue navigator. Admin permission will be required.


    """
    return web.Response(status=200)


async def get_issue_picker_resource(request: web.Request, query=None, current_jql=None, current_issue_key=None, current_project_id=None, show_sub_tasks=None, show_sub_task_parent=None) -> web.Response:
    """get_issue_picker_resource

    Returns suggested issues which match the auto-completion query for the user which executes this request. This REST  method will check the user&#39;s history and the user&#39;s browsing context and select this issues, which match the query.

    :param query: the query.
    :type query: str
    :param current_jql: the JQL in context of which the request is executed. Only issues which match this JQL query will be included in results.
    :type current_jql: str
    :param current_issue_key: the key of the issue in context of which the request is executed. The issue which is in context will not be included in the auto-completion result, even if it matches the query.
    :type current_issue_key: str
    :param current_project_id: the id of the project in context of which the request is executed. Suggested issues will be only from this project.
    :type current_project_id: str
    :param show_sub_tasks: if set to false, subtasks will not be included in the list.
    :type show_sub_tasks: bool
    :param show_sub_task_parent: if set to false and request is executed in context of a subtask, the parent issue will not be included in the auto-completion result, even if it matches the query.
    :type show_sub_task_parent: bool

    """
    return web.Response(status=200)


async def get_issue_security_schemes(request: web.Request, ) -> web.Response:
    """get_issue_security_schemes

    Returns all issue security schemes that are defined.


    """
    return web.Response(status=200)


async def get_issue_watchers(request: web.Request, issue_id_or_key) -> web.Response:
    """get_issue_watchers

    Returns the list of watchers for the issue with the given key.

    :param issue_id_or_key: a String containing an issue key.
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def get_issue_worklog(request: web.Request, issue_id_or_key) -> web.Response:
    """get_issue_worklog

    Returns all work logs for an issue. &lt;br/&gt;  &lt;strong&gt;Note:&lt;/strong&gt; Work logs won&#39;t be returned if the Log work field is hidden for the project.

    :param issue_id_or_key: a string containing the issue id or key the worklog will be added to
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def get_issuesecuritylevel(request: web.Request, id) -> web.Response:
    """get_issuesecuritylevel

    Returns a full representation of the security level that has the given id.

    :param id: a String containing an issue security level id
    :type id: str

    """
    return web.Response(status=200)


async def get_notification_schemes(request: web.Request, start_at=None, max_results=None, expand=None) -> web.Response:
    """get_notification_schemes

    Returns a &lt;a href&#x3D;\&quot;#pagination\&quot;&gt;paginated&lt;/a&gt; list of notification schemes. In order to access notification scheme, the calling user is  required to have permissions to administer at least one project associated with the requested notification scheme. Each scheme contains  a list of events and recipient configured to receive notifications for these events. Consumer should allow events without recipients to appear in response.  The list is ordered by the scheme&#39;s name.  Follow the documentation of /notificationscheme/{id} resource for all details about returned value.

    :param start_at: the index of the first notification scheme to return (0 based).
    :type start_at: int
    :param max_results: the maximum number of notification schemes to return (max 50).
    :type max_results: int
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def get_password_policy(request: web.Request, has_old_password=None) -> web.Response:
    """get_password_policy

    Returns the list of requirements for the current password policy. For example, \&quot;The password must have at least 10 characters.\&quot;,  \&quot;The password must not be similar to the user&#39;s name or email address.\&quot;, etc.

    :param has_old_password: whether or not the user will be required to enter their current password.  Use                        {@code false} (the default) if this is a new user or if an administrator is forcibly changing                        another user&#39;s password.
    :type has_old_password: bool

    """
    return web.Response(status=200)


async def get_permission_scheme(request: web.Request, scheme_id, expand=None) -> web.Response:
    """get_permission_scheme

    Returns a permission scheme identified by the given id.

    :param scheme_id: 
    :type scheme_id: int
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def get_permission_scheme_grant(request: web.Request, permission_id, scheme_id, expand=None) -> web.Response:
    """get_permission_scheme_grant

    Returns a permission grant identified by the given id.

    :param permission_id: 
    :type permission_id: int
    :param scheme_id: 
    :type scheme_id: int
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def get_permission_scheme_grants(request: web.Request, scheme_id, expand=None) -> web.Response:
    """get_permission_scheme_grants

    Returns all permission grants of the given permission scheme.

    :param scheme_id: 
    :type scheme_id: int
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def get_permission_schemes(request: web.Request, expand=None) -> web.Response:
    """get_permission_schemes

    Returns a list of all permission schemes.  &lt;p&gt;  By default only shortened beans are returned. If you want to include permissions of all the schemes,  then specify the &lt;b&gt;permissions&lt;/b&gt; expand parameter. Permissions will be included also if you specify  any other expand parameter.  &lt;/p&gt;

    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def get_permissions(request: web.Request, project_key=None, project_id=None, issue_key=None, issue_id=None) -> web.Response:
    """get_permissions

    Returns all permissions in the system and whether the currently logged in user has them. You can optionally provide a specific context to get permissions for  (projectKey OR projectId OR issueKey OR issueId)  &lt;ul&gt;  &lt;li&gt; When no context supplied the project related permissions will return true if the user has that permission in ANY project &lt;/li&gt;  &lt;li&gt; If a project context is provided, project related permissions will return true if the user has the permissions in the specified project.  For permissions that are determined using issue data (e.g Current Assignee), true will be returned if the user meets the permission criteria in ANY issue in that project &lt;/li&gt;  &lt;li&gt; If an issue context is provided, it will return whether or not the user has each permission in that specific issue&lt;/li&gt;  &lt;/ul&gt;  &lt;p&gt;  NB: The above means that for issue-level permissions (EDIT_ISSUE for example), hasPermission may be true when no context is provided, or when a project context is provided,  &lt;b&gt;but&lt;/b&gt; may be false for any given (or all) issues. This would occur (for example) if Reporters were given the EDIT_ISSUE permission. This is because  any user could be a reporter, except in the context of a concrete issue, where the reporter is known.  &lt;/p&gt;  &lt;p&gt;  Global permissions will still be returned for all scopes.  &lt;/p&gt;  &lt;p&gt;  Prior to version 6.4 this service returned project permissions with keys corresponding to com.atlassian.jira.security.Permissions.Permission constants.  Since 6.4 those keys are considered deprecated and this service returns system project permission keys corresponding to constants defined in com.atlassian.jira.permission.ProjectPermissions.  Permissions with legacy keys are still also returned for backwards compatibility, they are marked with an attribute deprecatedKey&#x3D;true.  The attribute is missing for project permissions with the current keys.  &lt;/p&gt;

    :param project_key: - key of project to scope returned permissions for.
    :type project_key: str
    :param project_id: - id of project to scope returned permissions for.
    :type project_id: str
    :param issue_key: - key of the issue to scope returned permissions for.
    :type issue_key: str
    :param issue_id: - id of the issue to scope returned permissions for.
    :type issue_id: str

    """
    return web.Response(status=200)


async def get_preference(request: web.Request, key=None) -> web.Response:
    """get_preference

    Returns preference of the currently logged in user. Preference key must be provided as input parameter (key). The  value is returned exactly as it is. If key parameter is not provided or wrong - status code 404. If value is  found  - status code 200.

    :param key: - key of the preference to be returned.
    :type key: str

    """
    return web.Response(status=200)


async def get_priorities(request: web.Request, ) -> web.Response:
    """get_priorities

    Returns a list of all issue priorities.


    """
    return web.Response(status=200)


async def get_priority(request: web.Request, id) -> web.Response:
    """get_priority

    Returns an issue priority.

    :param id: a String containing the priority id
    :type id: str

    """
    return web.Response(status=200)


async def get_progress(request: web.Request, request_id) -> web.Response:
    """get_progress

    Retrieves the progress of a single reindex request.

    :param request_id: the reindex request ID.
    :type request_id: int

    """
    return web.Response(status=200)


async def get_progress_bulk(request: web.Request, request_id=None) -> web.Response:
    """get_progress_bulk

    Retrieves the progress of a multiple reindex requests.  Only reindex requests that actually exist will be returned  in the results.

    :param request_id: the reindex request IDs.
    :type request_id: str

    """
    return web.Response(status=200)


async def get_project_category_by_id(request: web.Request, id) -> web.Response:
    """get_project_category_by_id

    Contains a representation of a project category in JSON format.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_project_components(request: web.Request, project_id_or_key) -> web.Response:
    """get_project_components

    Contains a full representation of a the specified project&#39;s components.

    :param project_id_or_key: the project id or project key
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def get_project_role(request: web.Request, project_id_or_key, id) -> web.Response:
    """get_project_role

    Returns the details for a given project role in a project.

    :param project_id_or_key: the project id or project key
    :type project_id_or_key: str
    :param id: the project role id
    :type id: int

    """
    return web.Response(status=200)


async def get_project_role_actors_for_role(request: web.Request, id) -> web.Response:
    """get_project_role_actors_for_role

    Gets default actors for the given role.

    :param id: the role id to remove the actors from
    :type id: int

    """
    return web.Response(status=200)


async def get_project_roles_by_id(request: web.Request, id) -> web.Response:
    """get_project_roles_by_id

    Get a specific ProjectRole available in JIRA.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_project_type_by_key(request: web.Request, project_type_key) -> web.Response:
    """get_project_type_by_key

    Returns the project type with the given key.

    :param project_type_key: 
    :type project_type_key: str

    """
    return web.Response(status=200)


async def get_project_versions(request: web.Request, project_id_or_key, expand=None) -> web.Response:
    """get_project_versions

    Contains a full representation of a the specified project&#39;s versions.

    :param project_id_or_key: the project id or project key
    :type project_id_or_key: str
    :param expand: the parameters to expand
    :type expand: str

    """
    return web.Response(status=200)


async def get_project_versions_paginated(request: web.Request, project_id_or_key, start_at=None, max_results=None, order_by=None, expand=None) -> web.Response:
    """get_project_versions_paginated

    Returns all versions for the specified project. Results are &lt;a href&#x3D;\&quot;#pagination\&quot;&gt;paginated&lt;/a&gt;.  &lt;p&gt;  Results can be ordered by the following fields:  &lt;ul&gt;  &lt;li&gt;sequence&lt;/li&gt;  &lt;li&gt;name&lt;/li&gt;  &lt;li&gt;startDate&lt;/li&gt;  &lt;li&gt;releaseDate&lt;/li&gt;  &lt;/ul&gt;  &lt;/p&gt;

    :param project_id_or_key: the project id or project key
    :type project_id_or_key: str
    :param start_at: the page offset, if not specified then defaults to 0
    :type start_at: int
    :param max_results: how many results on the page should be included. Defaults to 50.
    :type max_results: int
    :param order_by: ordering of the results.
    :type order_by: str
    :param expand: the parameters to expand
    :type expand: str

    """
    return web.Response(status=200)


async def get_properties(request: web.Request, id, include_reserved_keys=None, key=None, workflow_name=None, workflow_mode=None) -> web.Response:
    """get_properties

    Return the property or properties associated with a transition.

    :param id: the ID of the transition within the workflow.
    :type id: int
    :param include_reserved_keys: some keys under the \&quot;jira.\&quot; prefix are editable, some are not. Set this to true                             in order to include the non-editable keys in the response.
    :type include_reserved_keys: bool
    :param key: the name of the property key to query. Can be left off the query to return all properties.
    :type key: str
    :param workflow_name: the name of the workflow to use.
    :type workflow_name: str
    :param workflow_mode: the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;.
    :type workflow_mode: str

    """
    return web.Response(status=200)


async def get_property_keys(request: web.Request, issue_type_id) -> web.Response:
    """get_property_keys

    Returns the keys of all properties for the issue type identified by the id.

    :param issue_type_id: the issue type from which the keys will be returned
    :type issue_type_id: str

    """
    return web.Response(status=200)


async def get_records(request: web.Request, offset=None, limit=None, filter=None, _from=None, to=None, project_ids=None, user_ids=None) -> web.Response:
    """get_records

    Returns auditing records filtered using provided parameters

    :param offset: - the number of record from which search starts
    :type offset: int
    :param limit: - maximum number of returned results (if is limit is &lt;&#x3D; 0 or &gt; 1000, it will be set do default value: 1000)
    :type limit: int
    :param filter: - text query; each record that will be returned must contain the provided text in one of its fields
    :type filter: str
    :param _from: - timestamp in past; &#39;from&#39; must be less or equal &#39;to&#39;, otherwise the result set will be empty                only records that where created in the same moment or after the &#39;from&#39; timestamp will be provided in response
    :type _from: str
    :param to: - timestamp in past; &#39;from&#39; must be less or equal &#39;to&#39;, otherwise the result set will be empty                only records that where created in the same moment or earlier than the &#39;to&#39; timestamp will be provided in response
    :type to: str
    :param project_ids: - list of project ids to look for
    :type project_ids: str
    :param user_ids: - list of user ids to look for
    :type user_ids: str

    """
    return web.Response(status=200)


async def get_reindex_info(request: web.Request, task_id=None) -> web.Response:
    """get_reindex_info

    Returns information on the system reindexes.  If a reindex is currently taking place then information about this reindex is returned.  If there is no active index task, then returns information about the latest reindex task run, otherwise returns a 404  indicating that no reindex has taken place.

    :param task_id: the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and                returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no                reindexing task with that id then a 404 is returned.
    :type task_id: int

    """
    return web.Response(status=200)


async def get_reindex_progress(request: web.Request, task_id=None) -> web.Response:
    """get_reindex_progress

    Returns information on the system reindexes.  If a reindex is currently taking place then information about this reindex is returned.  If there is no active index task, then returns information about the latest reindex task run, otherwise returns a 404  indicating that no reindex has taken place.

    :param task_id: the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and                returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no                reindexing task with that id then a 404 is returned.
    :type task_id: int

    """
    return web.Response(status=200)


async def get_remote_issue_link_by_id(request: web.Request, link_id, issue_id_or_key) -> web.Response:
    """get_remote_issue_link_by_id

    Get the remote issue link with the given id on the issue.

    :param link_id: the id of the remote issue link
    :type link_id: str
    :param issue_id_or_key: the issue to create the remote issue link for
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def get_remote_issue_links(request: web.Request, issue_id_or_key, global_id=None) -> web.Response:
    """get_remote_issue_links

    A REST sub-resource representing the remote issue links on the issue.

    :param issue_id_or_key: the issue to create the remote issue link for
    :type issue_id_or_key: str
    :param global_id: The id of the remote issue link to be returned.  If null (not provided) all remote links for the                      issue are returned.                      &lt;p&gt;For a fullexplanation of Issue Link fields please refer to                      &lt;a href&#x3D;\&quot;https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links\&quot;&gt;https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links&lt;/a&gt;&lt;/p&gt;
    :type global_id: str

    """
    return web.Response(status=200)


async def get_remote_version_link(request: web.Request, version_id, global_id) -> web.Response:
    """get_remote_version_link

    A REST sub-resource representing a remote version link

    :param version_id: The version ID of the remote link
    :type version_id: str
    :param global_id: The global ID of the remote link
    :type global_id: str

    """
    return web.Response(status=200)


async def get_remote_version_links(request: web.Request, global_id=None) -> web.Response:
    """get_remote_version_links

    Returns the remote version links for a given global ID.

    :param global_id: the global ID of the remote resource that is linked to the versions
    :type global_id: str

    """
    return web.Response(status=200)


async def get_remote_version_links_by_version_id(request: web.Request, version_id) -> web.Response:
    """get_remote_version_links_by_version_id

    Returns the remote version links associated with the given version ID.

    :param version_id: The version for which to delete ALL existing remote version links
    :type version_id: str

    """
    return web.Response(status=200)


async def get_resolution(request: web.Request, id) -> web.Response:
    """get_resolution

    Returns a resolution.

    :param id: a String containing the resolution id
    :type id: str

    """
    return web.Response(status=200)


async def get_resolutions(request: web.Request, ) -> web.Response:
    """get_resolutions

    Returns a list of all resolutions.


    """
    return web.Response(status=200)


async def get_scheme_attribute(request: web.Request, permission_scheme_id, attribute_key) -> web.Response:
    """get_scheme_attribute

    

    :param permission_scheme_id: permission scheme id
    :type permission_scheme_id: int
    :param attribute_key: permission scheme attribute key
    :type attribute_key: str

    """
    return web.Response(status=200)


async def get_security_levels_for_project(request: web.Request, project_key_or_id) -> web.Response:
    """get_security_levels_for_project

    Returns all security levels for the project that the current logged in user has access to.  If the user does not have the Set Issue Security permission, the list will be empty.

    :param project_key_or_id: - key or id of project to list the security levels for
    :type project_key_or_id: str

    """
    return web.Response(status=200)


async def get_server_info(request: web.Request, do_health_check=None) -> web.Response:
    """get_server_info

    Returns general information about the current JIRA server.

    :param do_health_check: 
    :type do_health_check: bool

    """
    return web.Response(status=200)


async def get_share_permission(request: web.Request, permission_id, id) -> web.Response:
    """get_share_permission

    Returns a single share permission of the given filter.

    :param permission_id: 
    :type permission_id: int
    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_share_permissions(request: web.Request, id) -> web.Response:
    """get_share_permissions

    Returns all share permissions of the given filter.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_state(request: web.Request, ) -> web.Response:
    """get_state

    


    """
    return web.Response(status=200)


async def get_status(request: web.Request, id_or_name) -> web.Response:
    """get_status

    Returns a full representation of the Status having the given id or name.

    :param id_or_name: a numeric Status id or a status name
    :type id_or_name: str

    """
    return web.Response(status=200)


async def get_status_categories(request: web.Request, ) -> web.Response:
    """get_status_categories

    Returns a list of all status categories


    """
    return web.Response(status=200)


async def get_status_category(request: web.Request, id_or_key) -> web.Response:
    """get_status_category

    Returns a full representation of the StatusCategory having the given id or key

    :param id_or_key: a numeric StatusCategory id or a status category key
    :type id_or_key: str

    """
    return web.Response(status=200)


async def get_statuses(request: web.Request, ) -> web.Response:
    """get_statuses

    Returns a list of all statuses


    """
    return web.Response(status=200)


async def get_sub_tasks(request: web.Request, issue_id_or_key) -> web.Response:
    """get_sub_tasks

    Returns an issue&#39;s subtask list

    :param issue_id_or_key: The parent issue&#39;s key or id
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def get_transitions(request: web.Request, issue_id_or_key, transition_id=None) -> web.Response:
    """get_transitions

    Get a list of the transitions possible for this issue by the current user, along with fields that are required and their types.  &lt;p/&gt;  Fields will only be returned if &lt;code&gt;expand&#x3D;transitions.fields&lt;/code&gt;.  &lt;p/&gt;  The fields in the metadata correspond to the fields in the transition screen for that transition.  Fields not in the screen will not be in the metadata.

    :param issue_id_or_key: the issue whose transitions you want to view
    :type issue_id_or_key: str
    :param transition_id: 
    :type transition_id: str

    """
    return web.Response(status=200)


async def get_upgrade_result(request: web.Request, ) -> web.Response:
    """get_upgrade_result

    Returns the result of the last upgrade task.   Returns {@link javax.ws.rs.core.Response#seeOther(java.net.URI)} if still running.


    """
    return web.Response(status=200)


async def get_users_from_group(request: web.Request, groupname=None, include_inactive_users=None, start_at=None, max_results=None) -> web.Response:
    """get_users_from_group

    This resource returns a &lt;a href&#x3D;\&quot;#pagination\&quot;&gt;paginated&lt;/a&gt; list of users who are members of the specified group and its subgroups.  Users in the page are ordered by user names. User of this resource is required to have sysadmin or admin permissions.

    :param groupname: a name of the group for which members will be returned.
    :type groupname: str
    :param include_inactive_users: inactive users will be included in the response if set to true.
    :type include_inactive_users: bool
    :param start_at: the index of the first user in group to return (0 based).
    :type start_at: int
    :param max_results: the maximum number of users to return (max 50).
    :type max_results: int

    """
    return web.Response(status=200)


async def get_version(request: web.Request, id, expand=None) -> web.Response:
    """get_version

    Returns a project version.

    :param id: The version to delete
    :type id: str
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def get_version_related_issues(request: web.Request, id) -> web.Response:
    """get_version_related_issues

    Returns a bean containing the number of fixed in and affected issues for the given version.

    :param id: a String containing the version id
    :type id: str

    """
    return web.Response(status=200)


async def get_version_unresolved_issues(request: web.Request, id) -> web.Response:
    """get_version_unresolved_issues

    Returns the number of unresolved issues for the given version

    :param id: a String containing the version id
    :type id: str

    """
    return web.Response(status=200)


async def get_votes(request: web.Request, issue_id_or_key) -> web.Response:
    """get_votes

    A REST sub-resource representing the voters on the issue.

    :param issue_id_or_key: the issue to view voting information for
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def get_workflow(request: web.Request, id, workflow_name=None, return_draft_if_exists=None) -> web.Response:
    """get_workflow

    Returns the workflow mappings or requested mapping to the caller for the passed scheme.

    :param id: the id of the scheme.
    :type id: int
    :param workflow_name: the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name.
    :type workflow_name: str
    :param return_draft_if_exists: when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself.
    :type return_draft_if_exists: bool

    """
    return web.Response(status=200)


async def get_worklog(request: web.Request, issue_id_or_key, id) -> web.Response:
    """get_worklog

    Returns a specific worklog. &lt;br/&gt;  &lt;strong&gt;Note:&lt;/strong&gt; The work log won&#39;t be returned if the Log work field is hidden for the project.

    :param issue_id_or_key: a string containing the issue id or key the worklog belongs to
    :type issue_id_or_key: str
    :param id: id of the worklog to be deleted
    :type id: str

    """
    return web.Response(status=200)


async def get_worklogs_for_ids(request: web.Request, ) -> web.Response:
    """get_worklogs_for_ids

    Returns worklogs for given worklog ids. Only worklogs to which the calling user has permissions, will be included in the result.  The returns set of worklogs is limited to 1000 elements.


    """
    return web.Response(status=200)


async def link_issues(request: web.Request, ) -> web.Response:
    """link_issues

    Creates an issue link between two issues.  The user requires the link issue permission for the issue which will be linked to another issue.  The specified link type in the request is used to create the link and will create a link from the first issue  to the second issue using the outward description. It also create a link from the second issue to the first issue using the  inward description of the issue link type.  It will add the supplied comment to the first issue. The comment can have a restriction who can view it.  If group is specified, only users of this group can view this comment, if roleLevel is specified only users who have the specified role can view this comment.  The user who creates the issue link needs to belong to the specified group or have the specified role.


    """
    return web.Response(status=200)


async def list(request: web.Request, filter=None, start_at=None, max_results=None) -> web.Response:
    """list

    Returns a list of all dashboards, optionally filtering them.

    :param filter: an optional filter that is applied to the list of dashboards. Valid values include                         &lt;code&gt;\&quot;favourite\&quot;&lt;/code&gt; for returning only favourite dashboards, and &lt;code&gt;\&quot;my\&quot;&lt;/code&gt; for returning                         dashboards that are owned by the calling user.
    :type filter: str
    :param start_at: the index of the first dashboard to return (0-based). must be 0 or a multiple of                         &lt;code&gt;maxResults&lt;/code&gt;
    :type start_at: int
    :param max_results: a hint as to the the maximum number of dashboards to return in each call. Note that the                         JIRA server reserves the right to impose a &lt;code&gt;maxResults&lt;/code&gt; limit that is lower than the value that a                         client provides, dues to lack or resources or any other condition. When this happens, your results will be                         truncated. Callers should always check the returned &lt;code&gt;maxResults&lt;/code&gt; to determine the value that is                         effectively being used.
    :type max_results: int

    """
    return web.Response(status=200)


async def login(request: web.Request, ) -> web.Response:
    """login

    Creates a new session for a user in JIRA. Once a session has been successfully created it can be used to access  any of JIRA&#39;s remote APIs and also the web UI by passing the appropriate HTTP Cookie header.  &lt;p&gt;  Note that it is generally preferrable to use HTTP BASIC authentication with the REST API. However, this resource  may be used to mimic the behaviour of JIRA&#39;s log-in page (e.g. to display log-in errors to a user).


    """
    return web.Response(status=200)


async def logout(request: web.Request, ) -> web.Response:
    """logout

    Logs the current user out of JIRA, destroying the existing session, if any.


    """
    return web.Response(status=200)


async def merge(request: web.Request, move_issues_to, id) -> web.Response:
    """merge

    Merge versions

    :param move_issues_to: The version to set fixVersion to on issues where the deleted version is the fix version,                      If null then the fixVersion is removed.
    :type move_issues_to: str
    :param id: The version that will be merged to version {@code moveIssuesTo} and removed
    :type id: str

    """
    return web.Response(status=200)


async def move_field(request: web.Request, screen_id, tab_id, id) -> web.Response:
    """move_field

    Moves field on the given tab

    :param screen_id: id of screen
    :type screen_id: int
    :param tab_id: id of tab
    :type tab_id: int
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def move_sub_tasks(request: web.Request, issue_id_or_key) -> web.Response:
    """move_sub_tasks

    Reorders an issue&#39;s subtasks by moving the subtask at index \&quot;from\&quot;  to index \&quot;to\&quot;.

    :param issue_id_or_key: The parent issue&#39;s key or id
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def move_tab(request: web.Request, screen_id, tab_id, pos) -> web.Response:
    """move_tab

    Moves tab position

    :param screen_id: id of screen
    :type screen_id: int
    :param tab_id: id of tab
    :type tab_id: int
    :param pos: position of tab
    :type pos: int

    """
    return web.Response(status=200)


async def move_version(request: web.Request, id) -> web.Response:
    """move_version

    Modify a version&#39;s sequence within a project.  &lt;p/&gt;  The move version bean has 2 alternative field value pairs:  &lt;dl&gt;  &lt;dt&gt;position&lt;/dt&gt;&lt;dd&gt;An absolute position, which may have a value of &#39;First&#39;, &#39;Last&#39;, &#39;Earlier&#39; or &#39;Later&#39;&lt;/dd&gt;  &lt;dt&gt;after&lt;/dt&gt;&lt;dd&gt;A version to place this version after.  The value should be the self link of another version&lt;/dd&gt;  &lt;/dl&gt;

    :param id: a String containing the version id
    :type id: str

    """
    return web.Response(status=200)


async def notify(request: web.Request, issue_id_or_key) -> web.Response:
    """notify

    Sends a notification (email) to the list or recipients defined in the request.

    :param issue_id_or_key: a string containing the issue id or key the comment will be added to
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def partial_update_project_role(request: web.Request, id) -> web.Response:
    """partial_update_project_role

    Partially updates a roles name or description.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def policy_check_create_user(request: web.Request, ) -> web.Response:
    """policy_check_create_user

    Returns a list of statements explaining why the password policy would disallow a proposed password for a new user.  &lt;p&gt;  You can use this method to test the password policy validation. This could be done prior to an action   where a new user and related password are created, using methods like the ones in   &lt;a href&#x3D;\&quot;https://docs.atlassian.com/jira/latest/com/atlassian/jira/bc/user/UserService.html\&quot;&gt;UserService&lt;/a&gt;.        For example, you could use this to validate a password in a create user form in the user interface, as the user enters it.&lt;br/&gt;  The username and new password must be not empty to perform the validation.&lt;br/&gt;  Note, this method will help you validate against the policy only. It won&#39;t check any other validations that might be performed   when creating a new user, e.g. checking whether a user with the same name already exists.  &lt;/p&gt;


    """
    return web.Response(status=200)


async def policy_check_update_user(request: web.Request, ) -> web.Response:
    """policy_check_update_user

    Returns a list of statements explaining why the password policy would disallow a proposed new password for a user with an existing password.  &lt;p&gt;  You can use this method to test the password policy validation. This could be done prior to an action where the password   is actually updated, using methods like &lt;a href&#x3D;\&quot;https://docs.atlassian.com/jira/latest/com/atlassian/jira/web/action/user/ChangePassword.html\&quot;&gt;ChangePassword&lt;/a&gt;        or &lt;a href&#x3D;\&quot;https://docs.atlassian.com/jira/latest/com/atlassian/jira/web/action/user/ResetPassword.html\&quot;&gt;ResetPassword&lt;/a&gt;.   For example, you could use this to validate a password in a change password form in the user interface, as the user enters it.&lt;br/&gt;  The user must exist and the username and new password must be not empty, to perform the validation.&lt;br/&gt;  Note, this method will help you validate against the policy only. It won&#39;t check any other validations that might be performed   when submitting a password change/reset request, e.g. verifying whether the old password is valid.  &lt;/p&gt;


    """
    return web.Response(status=200)


async def process_requests(request: web.Request, ) -> web.Response:
    """process_requests

    Executes any pending reindex requests.  Returns a JSON array containing the IDs of the reindex requests  that are being processed.  Execution is asynchronous - progress of the returned tasks can be monitored through  other REST calls.


    """
    return web.Response(status=200)


async def put(request: web.Request, key, if_match=None) -> web.Response:
    """put

    Updates the ApplicationRole with the passed data. Only the groups and default groups setting of the  role may be updated. Requests to change the key or the name of the role will be silently ignored.  &lt;p&gt;  Optional: If versionHash is passed through the If-Match header the request will be rejected if not the  same as server

    :param key: the key of the role to update.
    :type key: str
    :param if_match: the hash of the version to update. Optional Param
    :type if_match: str

    """
    return web.Response(status=200)


async def put_bulk(request: web.Request, if_match=None) -> web.Response:
    """put_bulk

    Updates the ApplicationRoles with the passed data if the version hash is the same as the server.  Only the groups and default groups setting of the role may be updated. Requests to change the key  or the name of the role will be silently ignored. It is acceptable to pass only the roles that are updated  as roles that are present in the server but not in data to update with, will not be deleted.

    :param if_match: 
    :type if_match: str

    """
    return web.Response(status=200)


async def reindex(request: web.Request, type=None, index_comments=None, index_change_history=None, index_worklogs=None) -> web.Response:
    """reindex

    Kicks off a reindex.  Need Admin permissions to perform this reindex.

    :param type: Case insensitive String indicating type of reindex.  If omitted, then defaults to BACKGROUND_PREFERRED.
    :type type: str
    :param index_comments: Indicates that comments should also be reindexed. Not relevant for foreground reindex, where comments are always reindexed.
    :type index_comments: bool
    :param index_change_history: Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed.
    :type index_change_history: bool
    :param index_worklogs: Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed.
    :type index_worklogs: bool

    """
    return web.Response(status=200)


async def reindex_issues(request: web.Request, issue_id=None, index_comments=None, index_change_history=None, index_worklogs=None) -> web.Response:
    """reindex_issues

    Reindexes one or more individual issues.  Indexing is performed synchronously - the call returns when indexing of  the issues has completed or a failure occurs.  &lt;p&gt;  Use either explicitly specified issue IDs or a JQL query to select issues to reindex.

    :param issue_id: the IDs or keys of one or more issues to reindex.
    :type issue_id: str
    :param index_comments: Indicates that comments should also be reindexed.
    :type index_comments: bool
    :param index_change_history: Indicates that changeHistory should also be reindexed.
    :type index_change_history: bool
    :param index_worklogs: Indicates that changeHistory should also be reindexed.
    :type index_worklogs: bool

    """
    return web.Response(status=200)


async def release(request: web.Request, ) -> web.Response:
    """release

    This method invalidates the any current WebSudo session.


    """
    return web.Response(status=200)


async def remove_attachment(request: web.Request, id) -> web.Response:
    """remove_attachment

    Remove an attachment from an issue.

    :param id: id of the attachment to remove
    :type id: str

    """
    return web.Response(status=200)


async def remove_field(request: web.Request, screen_id, tab_id, id) -> web.Response:
    """remove_field

    Removes field from given tab

    :param screen_id: id of screen
    :type screen_id: int
    :param tab_id: id of tab
    :type tab_id: int
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def remove_group(request: web.Request, groupname=None, swap_group=None) -> web.Response:
    """remove_group

    Deletes a group by given group parameter.  &lt;p&gt;  Returns no content

    :param groupname: (mandatory) The name of the group to delete.
    :type groupname: str
    :param swap_group: If you delete a group and content is restricted to that group, the content will be hidden from all users.   To prevent this, use this parameter to specify a different group to transfer the restrictions (comments and worklogs only) to.
    :type swap_group: str

    """
    return web.Response(status=200)


async def remove_preference(request: web.Request, key=None) -> web.Response:
    """remove_preference

    Removes preference of the currently logged in user. Preference key must be provided as input parameters (key). If  key parameter is not provided or wrong - status code 404. If preference is unset - status code 204.

    :param key: - key of the preference to be removed.
    :type key: str

    """
    return web.Response(status=200)


async def remove_project_category(request: web.Request, id) -> web.Response:
    """remove_project_category

    Delete a project category.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def remove_user(request: web.Request, username=None, key=None) -> web.Response:
    """remove_user

    Removes user.

    :param username: the username
    :type username: str
    :param key: user key
    :type key: str

    """
    return web.Response(status=200)


async def remove_user_from_application(request: web.Request, username=None, application_key=None) -> web.Response:
    """remove_user_from_application

    Remove user from given application. Admin permission will be required to perform this operation.

    :param username: username
    :type username: str
    :param application_key: application key
    :type application_key: str

    """
    return web.Response(status=200)


async def remove_user_from_group(request: web.Request, groupname=None, username=None) -> web.Response:
    """remove_user_from_group

    Removes given user from a group.  &lt;p&gt;  Returns no content

    :param groupname: A name of requested group.
    :type groupname: str
    :param username: User to remove from a group
    :type username: str

    """
    return web.Response(status=200)


async def remove_vote(request: web.Request, issue_id_or_key) -> web.Response:
    """remove_vote

    Remove your vote from an issue. (i.e. \&quot;unvote\&quot;)

    :param issue_id_or_key: the issue to view voting information for
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def remove_watcher(request: web.Request, issue_id_or_key, username=None) -> web.Response:
    """remove_watcher

    Removes a user from an issue&#39;s watcher list.

    :param issue_id_or_key: a String containing an issue key.
    :type issue_id_or_key: str
    :param username: a String containing the name of the user to remove from the watcher list. Must not be null.
    :type username: str

    """
    return web.Response(status=200)


async def rename_tab(request: web.Request, screen_id, tab_id) -> web.Response:
    """rename_tab

    Renames tab on given screen

    :param screen_id: id of screen
    :type screen_id: int
    :param tab_id: id of tab
    :type tab_id: int

    """
    return web.Response(status=200)


async def run_upgrades_now(request: web.Request, ) -> web.Response:
    """run_upgrades_now

    Runs any pending delayed upgrade tasks.  Need Admin permissions to do this.


    """
    return web.Response(status=200)


async def search(request: web.Request, jql=None, start_at=None, max_results=None, validate_query=None, fields=None, expand=None) -> web.Response:
    """search

    Searches for issues using JQL.  &lt;p&gt;  &lt;b&gt;Sorting&lt;/b&gt;  the &lt;code&gt;jql&lt;/code&gt; parameter is a full &lt;a href&#x3D;\&quot;http://confluence.atlassian.com/display/JIRA/Advanced+Searching\&quot;&gt;JQL&lt;/a&gt;  expression, and includes an &lt;code&gt;ORDER BY&lt;/code&gt; clause.  &lt;/p&gt;  &lt;p&gt;  The &lt;code&gt;fields&lt;/code&gt; param (which can be specified multiple times) gives a comma-separated list of fields  to include in the response. This can be used to retrieve a subset of fields.  A particular field can be excluded by prefixing it with a minus.  &lt;p&gt;  By default, only navigable (&lt;code&gt;*navigable&lt;/code&gt;) fields are returned in this search resource. Note: the default is different  in the get-issue resource -- the default there all fields (&lt;code&gt;*all&lt;/code&gt;).  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;*all&lt;/code&gt; - include all fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*navigable&lt;/code&gt; - include just navigable fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;summary,comment&lt;/code&gt; - include just the summary and comments&lt;/li&gt;  &lt;li&gt;&lt;code&gt;-description&lt;/code&gt; - include navigable fields except the description (the default is &lt;code&gt;*navigable&lt;/code&gt; for search)&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*all,-comment&lt;/code&gt; - include everything except comments&lt;/li&gt;  &lt;/ul&gt;  &lt;p&gt;  &lt;/p&gt;  &lt;p&gt;&lt;b&gt;GET vs POST:&lt;/b&gt;  If the JQL query is too large to be encoded as a query param you should instead  POST to this resource.  &lt;/p&gt;  &lt;p&gt;  &lt;b&gt;Expanding Issues in the Search Result:&lt;/b&gt;  It is possible to expand the issues returned by directly specifying the expansion on the expand parameter passed  in to this resources.  &lt;/p&gt;  &lt;p&gt;  For instance, to expand the &amp;quot;changelog&amp;quot; for all the issues on the search result, it is neccesary to  specify &amp;quot;changelog&amp;quot; as one of the values to expand.  &lt;/p&gt;

    :param jql: a JQL query string
    :type jql: str
    :param start_at: the index of the first issue to return (0-based)
    :type start_at: int
    :param max_results: the maximum number of issues to return (defaults to 50). The maximum allowable value is                       dictated by the JIRA property &#39;jira.search.views.default.max&#39;. If you specify a value that is higher than this                       number, your search results will be truncated.
    :type max_results: int
    :param validate_query: whether to validate the JQL query
    :type validate_query: bool
    :param fields: the list of fields to return for each issue. By default, all navigable fields are returned.
    :type fields: str
    :param expand: A comma-separated list of the parameters to expand.
    :type expand: str

    """
    return web.Response(status=200)


async def search_using_search_request(request: web.Request, ) -> web.Response:
    """search_using_search_request

    Performs a search using JQL.


    """
    return web.Response(status=200)


async def set_actors(request: web.Request, project_id_or_key, id) -> web.Response:
    """set_actors

    Updates a project role to include the specified actors (users or groups).

    :param project_id_or_key: the project id or project key
    :type project_id_or_key: str
    :param id: the project role id
    :type id: int

    """
    return web.Response(status=200)


async def set_base_url(request: web.Request, ) -> web.Response:
    """set_base_url

    Sets the base URL that is configured for this JIRA instance.


    """
    return web.Response(status=200)


async def set_default_share_scope(request: web.Request, ) -> web.Response:
    """set_default_share_scope

    Sets the default share scope of the logged-in user. Available values are GLOBAL and PRIVATE.


    """
    return web.Response(status=200)


async def set_draft_issue_type(request: web.Request, issue_type, id) -> web.Response:
    """set_draft_issue_type

    Set the issue type mapping for the passed draft scheme.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that  the draft should be created/updated when the actual scheme cannot be edited.

    :param issue_type: the issue type being set.
    :type issue_type: str
    :param id: the id of the parent scheme.
    :type id: int

    """
    return web.Response(status=200)


async def set_issue_navigator_default_columns(request: web.Request, ) -> web.Response:
    """set_issue_navigator_default_columns

    Sets the default system columns for issue navigator. Admin permission will be required.


    """
    return web.Response(status=200)


async def set_issue_type(request: web.Request, issue_type, id) -> web.Response:
    """set_issue_type

    Set the issue type mapping for the passed scheme.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that  the draft should be created/updated when the actual scheme cannot be edited.

    :param issue_type: the issue type being set.
    :type issue_type: str
    :param id: the id of the scheme.
    :type id: int

    """
    return web.Response(status=200)


async def set_preference(request: web.Request, key=None) -> web.Response:
    """set_preference

    Sets preference of the currently logged in user. Preference key must be provided as input parameters (key). Value  must be provided as post body. If key or value parameter is not provided - status code 404. If preference is set  - status code 204.

    :param key: - key of the preference to be set.
    :type key: str

    """
    return web.Response(status=200)


async def set_property_via_restful_table(request: web.Request, id) -> web.Response:
    """set_property_via_restful_table

    Modify an application property via PUT. The \&quot;value\&quot; field present in the PUT will override the existing value.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def set_ready_to_upgrade(request: web.Request, ) -> web.Response:
    """set_ready_to_upgrade

    


    """
    return web.Response(status=200)


async def set_scheme_attribute(request: web.Request, permission_scheme_id, key) -> web.Response:
    """set_scheme_attribute

    Updates or inserts the attribute for a permission scheme specified by permission scheme id.  The attribute consists of the key and the value. The value will be converted to Boolean using Boolean#valueOf.

    :param permission_scheme_id: permission scheme id
    :type permission_scheme_id: int
    :param key: permission scheme attribute key
    :type key: str

    """
    return web.Response(status=200)


async def start(request: web.Request, ) -> web.Response:
    """start

    


    """
    return web.Response(status=200)


async def stop(request: web.Request, ) -> web.Response:
    """stop

    


    """
    return web.Response(status=200)


async def store_temporary_avatar(request: web.Request, type, filename=None, size=None) -> web.Response:
    """store_temporary_avatar

    Creates temporary avatar

    :param type: the avatar type
    :type type: str
    :param filename: name of file being uploaded
    :type filename: str
    :param size: size of file
    :type size: int

    """
    return web.Response(status=200)


async def update(request: web.Request, id) -> web.Response:
    """update

    Update the passed workflow scheme.  &lt;p/&gt;  The body of the request is a representation of the workflow scheme. Values not passed are assumed to indicate  no change for that field.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that the draft  should be created and/or updated when the actual scheme cannot be edited (e.g. when the scheme is being used by  a project). Values not appearing the body will not be touched.

    :param id: the id of the scheme.
    :type id: int

    """
    return web.Response(status=200)


async def update_comment(request: web.Request, issue_id_or_key, id, expand=None) -> web.Response:
    """update_comment

    Updates an existing comment using its JSON representation.

    :param issue_id_or_key: of the issue the comment belongs to
    :type issue_id_or_key: str
    :param id: the ID of the comment to request
    :type id: str
    :param expand: optional flags: renderedBody (provides body rendered in HTML)
    :type expand: str

    """
    return web.Response(status=200)


async def update_component(request: web.Request, id) -> web.Response:
    """update_component

    Modify a component via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field  is not present, it is silently ignored.  &lt;p&gt;  If leadUserName is an empty string (\&quot;\&quot;) the component lead will be removed.

    :param id: The component to delete.
    :type id: str

    """
    return web.Response(status=200)


async def update_default(request: web.Request, id) -> web.Response:
    """update_default

    Set the default workflow for the passed workflow scheme.  &lt;p/&gt;  The passed representation can have its  updateDraftIfNeeded flag set to true to indicate that the draft should be created/updated when the actual scheme  cannot be edited.

    :param id: the id of the scheme.
    :type id: int

    """
    return web.Response(status=200)


async def update_draft(request: web.Request, id) -> web.Response:
    """update_draft

    Update a draft workflow scheme. The draft will created if necessary.  &lt;p/&gt;  The body is a representation of the workflow scheme. Values not passed are assumed to indicate no change for that field.

    :param id: the id of the parent scheme.
    :type id: int

    """
    return web.Response(status=200)


async def update_draft_default(request: web.Request, id) -> web.Response:
    """update_draft_default

    Set the default workflow for the passed draft workflow scheme.

    :param id: the id of the parent scheme.
    :type id: int

    """
    return web.Response(status=200)


async def update_draft_workflow_mapping(request: web.Request, id, workflow_name=None) -> web.Response:
    """update_draft_workflow_mapping

    Update the draft scheme to include the passed mapping.  &lt;p/&gt;  The body is a representation of the workflow mapping.  Values not passed are assumed to indicate no change for that field.

    :param id: the id of the parent scheme.
    :type id: int
    :param workflow_name: the name of the workflow mapping to update.
    :type workflow_name: str

    """
    return web.Response(status=200)


async def update_issue_link_type(request: web.Request, issue_link_type_id) -> web.Response:
    """update_issue_link_type

    Update the specified issue link type.

    :param issue_link_type_id: 
    :type issue_link_type_id: str

    """
    return web.Response(status=200)


async def update_issue_type(request: web.Request, id) -> web.Response:
    """update_issue_type

    Updates the specified issue type from a JSON representation.

    :param id: the id of the issue type to update.
    :type id: str

    """
    return web.Response(status=200)


async def update_permission_scheme(request: web.Request, scheme_id, expand=None) -> web.Response:
    """update_permission_scheme

    Updates a permission scheme.  &lt;p&gt;  If the permissions list is present then it will be set in the permission scheme, which basically means it will overwrite any permission grants that  existed in the permission scheme. Sending an empty list will remove all permission grants from the permission scheme.  &lt;/p&gt;  &lt;p&gt;  To update just the name and description, do not send permissions list at all.  &lt;/p&gt;  &lt;p&gt;  To add or remove a single permission grant instead of updating the whole list at once use the &lt;b&gt;{schemeId}/permission/&lt;/b&gt; resource.  &lt;/p&gt;

    :param scheme_id: 
    :type scheme_id: int
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)


async def update_project(request: web.Request, project_id_or_key, expand=None) -> web.Response:
    """update_project

    Updates a project.  &lt;p&gt;  Only non null values sent in JSON will be updated in the project.&lt;/p&gt;  &lt;p&gt;  Values available for the assigneeType field are: \&quot;PROJECT_LEAD\&quot; and \&quot;UNASSIGNED\&quot;.&lt;/p&gt;

    :param project_id_or_key: the project id or project key
    :type project_id_or_key: str
    :param expand: the parameters to expand in returned project
    :type expand: str

    """
    return web.Response(status=200)


async def update_project_category(request: web.Request, id) -> web.Response:
    """update_project_category

    Modify a project category via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field  is not present, it is silently ignored.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def update_project_type(request: web.Request, project_id_or_key, new_project_type_key) -> web.Response:
    """update_project_type

    Updates the type of a project.

    :param project_id_or_key: identity of the project to update
    :type project_id_or_key: str
    :param new_project_type_key: The key of the new project type
    :type new_project_type_key: str

    """
    return web.Response(status=200)


async def update_property(request: web.Request, id, key=None, workflow_name=None, workflow_mode=None) -> web.Response:
    """update_property

    Update/add new property to a transition. Trying to update a property that does  not exist will result in a new property being added.

    :param id: the ID of the transition within the workflow.
    :type id: int
    :param key: the name of the property to add.
    :type key: str
    :param workflow_name: the name of the workflow to use.
    :type workflow_name: str
    :param workflow_mode: the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;.
    :type workflow_mode: str

    """
    return web.Response(status=200)


async def update_remote_issue_link(request: web.Request, link_id, issue_id_or_key) -> web.Response:
    """update_remote_issue_link

    Updates a remote issue link from a JSON representation. Any fields not provided are set to null.

    :param link_id: the id of the remote issue link
    :type link_id: str
    :param issue_id_or_key: the issue to create the remote issue link for
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def update_version(request: web.Request, id) -> web.Response:
    """update_version

    Modify a version via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field  is not present, it is silently ignored.

    :param id: The version to delete
    :type id: str

    """
    return web.Response(status=200)


async def update_workflow_mapping(request: web.Request, id, workflow_name=None) -> web.Response:
    """update_workflow_mapping

    Update the scheme to include the passed mapping.  &lt;p/&gt;  The body is a representation of the workflow mapping.  Values not passed are assumed to indicate no change for that field.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that the draft  should be created/updated when the actual scheme cannot be edited.

    :param id: the id of the scheme.
    :type id: int
    :param workflow_name: the name of the workflow mapping to update.
    :type workflow_name: str

    """
    return web.Response(status=200)


async def update_worklog(request: web.Request, issue_id_or_key, id, adjust_estimate=None, new_estimate=None) -> web.Response:
    """update_worklog

    Updates an existing worklog entry.  &lt;p&gt;Note that:&lt;/p&gt;   &lt;ul&gt;       &lt;li&gt;Fields possible for editing are: comment, visibility, started, timeSpent and timeSpentSeconds.&lt;/li&gt;       &lt;li&gt;Either timeSpent or timeSpentSeconds can be set.&lt;/li&gt;       &lt;li&gt;Fields which are not set will not be updated.&lt;/li&gt;       &lt;li&gt;For a request to be valid, it has to have at least one field change.&lt;/li&gt;   &lt;/ul&gt;

    :param issue_id_or_key: a string containing the issue id or key the worklog belongs to
    :type issue_id_or_key: str
    :param id: id of the worklog to be deleted
    :type id: str
    :param adjust_estimate: (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        &lt;ul&gt;                        &lt;li&gt;\&quot;new\&quot; - sets the estimate to a specific value&lt;/li&gt;                        &lt;li&gt;\&quot;leave\&quot;- leaves the estimate as is&lt;/li&gt;                        &lt;li&gt;\&quot;auto\&quot;- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog&lt;/li&gt; &lt;/ul&gt;
    :type adjust_estimate: str
    :param new_estimate: (required when \&quot;new\&quot; is selected for adjustEstimate) the new value for the remaining estimate field.
    :type new_estimate: str

    """
    return web.Response(status=200)


async def validate(request: web.Request, ) -> web.Response:
    """validate

    


    """
    return web.Response(status=200)
