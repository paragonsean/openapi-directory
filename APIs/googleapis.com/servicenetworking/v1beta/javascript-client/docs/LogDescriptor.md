# ServiceNetworkingApi.LogDescriptor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A human-readable description of this log. This information appears in the documentation and can contain details. | [optional] 
**displayName** | **String** | The human-readable name for this log. This information appears on the user interface and should be concise. | [optional] 
**labels** | [**[LabelDescriptor]**](LabelDescriptor.md) | The set of labels that are available to describe a specific log entry. Runtime requests that contain labels not specified here are considered invalid. | [optional] 
**name** | **String** | The name of the log. It must be less than 512 characters long and can include the following characters: upper- and lower-case alphanumeric characters [A-Za-z0-9], and punctuation characters including slash, underscore, hyphen, period [/_-.]. | [optional] 


