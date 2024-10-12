

# RoleAssignmentsCreate400Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** | A human-readable explanation specific to this occurrence of the problem. |  [optional] |
|**instance** | **String** | A URI reference that identifies the specific occurrence of the problem.  It may or may not yield further information if dereferenced. |  [optional] |
|**status** | **Object** |  |  [optional] |
|**title** | **Object** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VALIDATION_ERROR_HTML | &quot;https://errors.ix-api.net/v2/validation-error.html&quot; |
| UNABLE_TO_FULFILL_HTML | &quot;https://errors.ix-api.net/v2/unable-to-fulfill.html&quot; |



