

# DiagnosticsConfiguration

Diagnostics settings for an Azure ML web service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiry** | **OffsetDateTime** | Specifies the date and time when the logging will cease. If null, diagnostic collection is not time limited. |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) | Specifies the verbosity of the diagnostic output. Valid values are: None - disables tracing; Error - collects only error (stderr) traces; All - collects all traces (stdout and stderr). |  |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| ERROR | &quot;Error&quot; |
| ALL | &quot;All&quot; |



