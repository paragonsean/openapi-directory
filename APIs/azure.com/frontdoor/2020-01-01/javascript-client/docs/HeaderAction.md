# FrontDoorManagementClient.HeaderAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headerActionType** | **String** | Which type of manipulation to apply to the header. | 
**headerName** | **String** | The name of the header this action will apply to. | 
**value** | **String** | The value to update the given header name with. This value is not used if the actionType is Delete. | [optional] 



## Enum: HeaderActionTypeEnum


* `Append` (value: `"Append"`)

* `Delete` (value: `"Delete"`)

* `Overwrite` (value: `"Overwrite"`)




