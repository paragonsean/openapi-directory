

# GoogleCloudFunctionsV2alphaStateMessage

Informational messages about the state of the Cloud Function or Operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | The message. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of the state message. |  [optional] |
|**type** | **String** | One-word CamelCase type of the state message. |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEVERITY_UNSPECIFIED | &quot;SEVERITY_UNSPECIFIED&quot; |
| ERROR | &quot;ERROR&quot; |
| WARNING | &quot;WARNING&quot; |
| INFO | &quot;INFO&quot; |



