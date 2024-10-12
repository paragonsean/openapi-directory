# TheJiraCloudPlatformRestApi.ProjectFeature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **String** | The key of the feature. | [optional] 
**imageUri** | **String** | URI for the image representing the feature. | [optional] 
**localisedDescription** | **String** | Localized display description for the feature. | [optional] 
**localisedName** | **String** | Localized display name for the feature. | [optional] 
**prerequisites** | **[String]** | List of keys of the features required to enable the feature. | [optional] 
**projectId** | **Number** | The ID of the project. | [optional] 
**state** | **String** | The state of the feature. When updating the state of a feature, only ENABLED and DISABLED are supported. Responses can contain all values | [optional] 
**toggleLocked** | **Boolean** | Whether the state of the feature can be updated. | [optional] 



## Enum: StateEnum


* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)

* `COMING_SOON` (value: `"COMING_SOON"`)




