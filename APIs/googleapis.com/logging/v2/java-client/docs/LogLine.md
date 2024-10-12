

# LogLine

Application log line emitted while processing a request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**logMessage** | **String** | App-provided log message. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of this log entry. |  [optional] |
|**sourceLocation** | [**SourceLocation**](SourceLocation.md) |  |  [optional] |
|**time** | **String** | Approximate time when this log entry was made. |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| DEBUG | &quot;DEBUG&quot; |
| INFO | &quot;INFO&quot; |
| NOTICE | &quot;NOTICE&quot; |
| WARNING | &quot;WARNING&quot; |
| ERROR | &quot;ERROR&quot; |
| CRITICAL | &quot;CRITICAL&quot; |
| ALERT | &quot;ALERT&quot; |
| EMERGENCY | &quot;EMERGENCY&quot; |



