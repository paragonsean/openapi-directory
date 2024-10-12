

# ApiV1AdminAccountsIdActionPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reportId** | **String** | ID of an associated report that caused this action to be taken |  [optional] |
|**sendEmailNotification** | **Boolean** | Whether an email should be sent to the user with the above information. |  [optional] |
|**text** | **String** | Additional text for clarification of why this action was taken |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of action to be taken. Enumerable oneOf: none disable silence suspend |  [optional] |
|**warningPresetId** | **String** | ID of a preset warning |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| DISABLE | &quot;disable&quot; |
| SILENCE | &quot;silence&quot; |
| SUSPEND | &quot;suspend&quot; |



