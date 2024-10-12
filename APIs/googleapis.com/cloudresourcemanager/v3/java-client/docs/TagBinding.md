

# TagBinding

A TagBinding represents a connection between a TagValue and a cloud resource Once a TagBinding is created, the TagValue is applied to all the descendants of the Google Cloud resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Output only. The name of the TagBinding. This is a String of the form: &#x60;tagBindings/{full-resource-name}/{tag-value-name}&#x60; (e.g. &#x60;tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F123/tagValues/456&#x60;). |  [optional] [readonly] |
|**parent** | **String** | The full resource name of the resource the TagValue is bound to. E.g. &#x60;//cloudresourcemanager.googleapis.com/projects/123&#x60; |  [optional] |
|**tagValue** | **String** | The TagValue of the TagBinding. Must be of the form &#x60;tagValues/456&#x60;. |  [optional] |
|**tagValueNamespacedName** | **String** | The namespaced name for the TagValue of the TagBinding. Must be in the format &#x60;{parent_id}/{tag_key_short_name}/{short_name}&#x60;. For methods that support TagValue namespaced name, only one of tag_value_namespaced_name or tag_value may be filled. Requests with both fields will be rejected. |  [optional] |



