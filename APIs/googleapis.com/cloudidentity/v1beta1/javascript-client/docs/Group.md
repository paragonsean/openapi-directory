# CloudIdentityApi.Group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalGroupKeys** | [**[EntityKey]**](EntityKey.md) | Output only. Additional group keys associated with the Group. | [optional] [readonly] 
**createTime** | **String** | Output only. The time when the &#x60;Group&#x60; was created. | [optional] [readonly] 
**description** | **String** | An extended description to help users determine the purpose of a &#x60;Group&#x60;. Must not be longer than 4,096 characters. | [optional] 
**displayName** | **String** | The display name of the &#x60;Group&#x60;. | [optional] 
**dynamicGroupMetadata** | [**DynamicGroupMetadata**](DynamicGroupMetadata.md) |  | [optional] 
**groupKey** | [**EntityKey**](EntityKey.md) |  | [optional] 
**labels** | **{String: String}** | Required. One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value. Google Groups are the default type of group and have a label with a key of &#x60;cloudidentity.googleapis.com/groups.discussion_forum&#x60; and an empty value. Existing Google Groups can have an additional label with a key of &#x60;cloudidentity.googleapis.com/groups.security&#x60; and an empty value added to them. **This is an immutable change and the security label cannot be removed once added.** Dynamic groups have a label with a key of &#x60;cloudidentity.googleapis.com/groups.dynamic&#x60;. Identity-mapped groups for Cloud Search have a label with a key of &#x60;system/groups/external&#x60; and an empty value. | [optional] 
**name** | **String** | Output only. The [resource name](https://cloud.google.com/apis/design/resource_names) of the &#x60;Group&#x60;. Shall be of the form &#x60;groups/{group_id}&#x60;. | [optional] [readonly] 
**parent** | **String** | Required. Immutable. The resource name of the entity under which this &#x60;Group&#x60; resides in the Cloud Identity resource hierarchy. Must be of the form &#x60;identitysources/{identity_source}&#x60; for external [identity-mapped groups](https://support.google.com/a/answer/9039510) or &#x60;customers/{customer_id}&#x60; for Google Groups. The &#x60;customer_id&#x60; must begin with \&quot;C\&quot; (for example, &#39;C046psxkn&#39;). [Find your customer ID.] (https://support.google.com/cloudidentity/answer/10070793) | [optional] 
**posixGroups** | [**[PosixGroup]**](PosixGroup.md) | Optional. The POSIX groups associated with the &#x60;Group&#x60;. | [optional] 
**updateTime** | **String** | Output only. The time when the &#x60;Group&#x60; was last updated. | [optional] [readonly] 


