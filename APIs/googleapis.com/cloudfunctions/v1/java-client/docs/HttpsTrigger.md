

# HttpsTrigger

Describes HttpsTrigger, could be used to connect web hooks to function.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**securityLevel** | [**SecurityLevelEnum**](#SecurityLevelEnum) | The security level for the function. |  [optional] |
|**url** | **String** | Output only. The deployed url for the function. |  [optional] [readonly] |



## Enum: SecurityLevelEnum

| Name | Value |
|---- | -----|
| SECURITY_LEVEL_UNSPECIFIED | &quot;SECURITY_LEVEL_UNSPECIFIED&quot; |
| SECURE_ALWAYS | &quot;SECURE_ALWAYS&quot; |
| SECURE_OPTIONAL | &quot;SECURE_OPTIONAL&quot; |



