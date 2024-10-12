# Inspector2.CreateFilterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Defines the action that is to be applied to the findings that match the filter. | 
**description** | **String** | A description of the filter. | [optional] 
**filterCriteria** | [**CreateFilterRequestFilterCriteria**](CreateFilterRequestFilterCriteria.md) |  | 
**name** | **String** | The name of the filter. Minimum length of 3. Maximum length of 64. Valid characters include alphanumeric characters, dot (.), underscore (_), and dash (-). Spaces are not allowed. | 
**reason** | **String** | The reason for creating the filter. | [optional] 
**tags** | **{String: String}** | A list of tags for the filter. | [optional] 



## Enum: ActionEnum


* `NONE` (value: `"NONE"`)

* `SUPPRESS` (value: `"SUPPRESS"`)




