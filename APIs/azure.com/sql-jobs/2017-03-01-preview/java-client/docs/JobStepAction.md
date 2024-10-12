

# JobStepAction

The action to be executed by a job step.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**source** | [**SourceEnum**](#SourceEnum) | The source of the action to execute. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of action being executed by the job step. |  [optional] |
|**value** | **String** | The action value, for example the text of the T-SQL script to execute. |  |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| INLINE | &quot;Inline&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| T_SQL | &quot;TSql&quot; |



