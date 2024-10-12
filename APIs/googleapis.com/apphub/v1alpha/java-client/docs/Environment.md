

# Environment

Environment of the Application, Service, or Workload

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**environment** | **String** | Optional. Environment name. Can contain only lowercase letters, numeric characters, underscores, and dashes. Can have a maximum length of 63 characters. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Environment Type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| PRODUCTION | &quot;PRODUCTION&quot; |
| STAGING | &quot;STAGING&quot; |
| TEST | &quot;TEST&quot; |
| DEVELOPMENT | &quot;DEVELOPMENT&quot; |



