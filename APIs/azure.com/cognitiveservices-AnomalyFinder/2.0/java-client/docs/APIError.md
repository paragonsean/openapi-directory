

# APIError

Error information returned by the API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | The error code. |  [optional] |
|**message** | **String** | A message explaining the error reported by the service. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| INVALID_CUSTOM_INTERVAL | &quot;InvalidCustomInterval&quot; |
| BAD_ARGUMENT | &quot;BadArgument&quot; |
| INVALID_GRANULARITY | &quot;InvalidGranularity&quot; |
| INVALID_PERIOD | &quot;InvalidPeriod&quot; |
| INVALID_MODEL_ARGUMENT | &quot;InvalidModelArgument&quot; |
| INVALID_SERIES | &quot;InvalidSeries&quot; |



