# Inspector2.UpdateFilterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Specifies the action that is to be applied to the findings that match the filter. | [optional] 
**description** | **String** | A description of the filter. | [optional] 
**filterArn** | **String** | The Amazon Resource Number (ARN) of the filter to update. | 
**filterCriteria** | [**CreateFilterRequestFilterCriteria**](CreateFilterRequestFilterCriteria.md) |  | [optional] 
**name** | **String** | The name of the filter. | [optional] 
**reason** | **String** | The reason the filter was updated. | [optional] 



## Enum: ActionEnum


* `NONE` (value: `"NONE"`)

* `SUPPRESS` (value: `"SUPPRESS"`)




