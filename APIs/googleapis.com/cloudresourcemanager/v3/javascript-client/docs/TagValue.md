# CloudResourceManagerApi.TagValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Creation time. | [optional] [readonly] 
**description** | **String** | Optional. User-assigned description of the TagValue. Must not exceed 256 characters. Read-write. | [optional] 
**etag** | **String** | Optional. Entity tag which users can pass to prevent race conditions. This field is always set in server responses. See UpdateTagValueRequest for details. | [optional] 
**name** | **String** | Immutable. Resource name for TagValue in the format &#x60;tagValues/456&#x60;. | [optional] 
**namespacedName** | **String** | Output only. The namespaced name of the TagValue. Can be in the form &#x60;{organization_id}/{tag_key_short_name}/{tag_value_short_name}&#x60; or &#x60;{project_id}/{tag_key_short_name}/{tag_value_short_name}&#x60; or &#x60;{project_number}/{tag_key_short_name}/{tag_value_short_name}&#x60;. | [optional] [readonly] 
**parent** | **String** | Immutable. The resource name of the new TagValue&#39;s parent TagKey. Must be of the form &#x60;tagKeys/{tag_key_id}&#x60;. | [optional] 
**shortName** | **String** | Required. Immutable. User-assigned short name for TagValue. The short name should be unique for TagValues within the same parent TagKey. The short name must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. | [optional] 
**updateTime** | **String** | Output only. Update time. | [optional] [readonly] 


