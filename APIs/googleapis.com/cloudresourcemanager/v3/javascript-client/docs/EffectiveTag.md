# CloudResourceManagerApi.EffectiveTag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inherited** | **Boolean** | Indicates the inheritance status of a tag value attached to the given resource. If the tag value is inherited from one of the resource&#39;s ancestors, inherited will be true. If false, then the tag value is directly attached to the resource, inherited will be false. | [optional] 
**namespacedTagKey** | **String** | The namespaced name of the TagKey. Can be in the form &#x60;{organization_id}/{tag_key_short_name}&#x60; or &#x60;{project_id}/{tag_key_short_name}&#x60; or &#x60;{project_number}/{tag_key_short_name}&#x60;. | [optional] 
**namespacedTagValue** | **String** | The namespaced name of the TagValue. Can be in the form &#x60;{organization_id}/{tag_key_short_name}/{tag_value_short_name}&#x60; or &#x60;{project_id}/{tag_key_short_name}/{tag_value_short_name}&#x60; or &#x60;{project_number}/{tag_key_short_name}/{tag_value_short_name}&#x60;. | [optional] 
**tagKey** | **String** | The name of the TagKey, in the format &#x60;tagKeys/{id}&#x60;, such as &#x60;tagKeys/123&#x60;. | [optional] 
**tagKeyParentName** | **String** | The parent name of the tag key. Must be in the format &#x60;organizations/{organization_id}&#x60; or &#x60;projects/{project_number}&#x60; | [optional] 
**tagValue** | **String** | Resource name for TagValue in the format &#x60;tagValues/456&#x60;. | [optional] 


