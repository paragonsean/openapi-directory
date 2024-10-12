

# AclRule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | ETag of the resource. |  [optional] |
|**id** | **String** | Identifier of the Access Control List (ACL) rule. See Sharing calendars. |  [optional] |
|**kind** | **String** | Type of the resource (\&quot;calendar#aclRule\&quot;). |  [optional] |
|**role** | **String** | The role assigned to the scope. Possible values are:   - \&quot;none\&quot; - Provides no access.  - \&quot;freeBusyReader\&quot; - Provides read access to free/busy information.  - \&quot;reader\&quot; - Provides read access to the calendar. Private events will appear to users with reader access, but event details will be hidden.  - \&quot;writer\&quot; - Provides read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible.  - \&quot;owner\&quot; - Provides ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs. |  [optional] |
|**scope** | [**AclRuleScope**](AclRuleScope.md) |  |  [optional] |



