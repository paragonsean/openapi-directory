# TheJiraCloudPlatformRestApi.Visibility

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **String** | The ID of the group or the name of the role that visibility of this item is restricted to. | [optional] 
**type** | **String** | Whether visibility of this item is restricted to a group or role. | [optional] 
**value** | **String** | The name of the group or role that visibility of this item is restricted to. Please note that the name of a group is mutable, to reliably identify a group use &#x60;identifier&#x60;. | [optional] 



## Enum: TypeEnum


* `group` (value: `"group"`)

* `role` (value: `"role"`)




