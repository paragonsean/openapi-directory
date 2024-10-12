

# ContactGroup

A contact group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientData** | [**List&lt;GroupClientData&gt;**](GroupClientData.md) | The group&#39;s client data. |  [optional] |
|**etag** | **String** | The [HTTP entity tag](https://en.wikipedia.org/wiki/HTTP_ETag) of the resource. Used for web cache validation. |  [optional] |
|**formattedName** | **String** | Output only. The name translated and formatted in the viewer&#39;s account locale or the &#x60;Accept-Language&#x60; HTTP header locale for system groups names. Group names set by the owner are the same as name. |  [optional] [readonly] |
|**groupType** | [**GroupTypeEnum**](#GroupTypeEnum) | Output only. The contact group type. |  [optional] [readonly] |
|**memberCount** | **Integer** | Output only. The total number of contacts in the group irrespective of max members in specified in the request. |  [optional] [readonly] |
|**memberResourceNames** | **List&lt;String&gt;** | Output only. The list of contact person resource names that are members of the contact group. The field is only populated for GET requests and will only return as many members as &#x60;maxMembers&#x60; in the get request. |  [optional] [readonly] |
|**metadata** | [**ContactGroupMetadata**](ContactGroupMetadata.md) |  |  [optional] |
|**name** | **String** | The contact group name set by the group owner or a system provided name for system groups. For [&#x60;contactGroups.create&#x60;](/people/api/rest/v1/contactGroups/create) or [&#x60;contactGroups.update&#x60;](/people/api/rest/v1/contactGroups/update) the name must be unique to the users contact groups. Attempting to create a group with a duplicate name will return a HTTP 409 error. |  [optional] |
|**resourceName** | **String** | The resource name for the contact group, assigned by the server. An ASCII string, in the form of &#x60;contactGroups/{contact_group_id}&#x60;. |  [optional] |



## Enum: GroupTypeEnum

| Name | Value |
|---- | -----|
| GROUP_TYPE_UNSPECIFIED | &quot;GROUP_TYPE_UNSPECIFIED&quot; |
| USER_CONTACT_GROUP | &quot;USER_CONTACT_GROUP&quot; |
| SYSTEM_CONTACT_GROUP | &quot;SYSTEM_CONTACT_GROUP&quot; |



