# SqlManagementClient.JobStepAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **String** | The source of the action to execute. | [optional] [default to &#39;Inline&#39;]
**type** | **String** | Type of action being executed by the job step. | [optional] [default to &#39;TSql&#39;]
**value** | **String** | The action value, for example the text of the T-SQL script to execute. | 



## Enum: SourceEnum


* `Inline` (value: `"Inline"`)





## Enum: TypeEnum


* `TSql` (value: `"TSql"`)




