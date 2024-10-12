

# AlertProperties

Properties of alert.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertType** | **String** | Alert type. |  [optional] [readonly] |
|**appearedAtDateTime** | **OffsetDateTime** | UTC time when the alert appeared. |  [optional] [readonly] |
|**detailedInformation** | **Map&lt;String, String&gt;** | Alert details. |  [optional] [readonly] |
|**errorDetails** | [**AlertErrorDetails**](AlertErrorDetails.md) |  |  [optional] |
|**recommendation** | **String** | Alert recommendation. |  [optional] [readonly] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of the alert. |  [optional] [readonly] |
|**title** | **String** | Alert title. |  [optional] [readonly] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| INFORMATIONAL | &quot;Informational&quot; |
| WARNING | &quot;Warning&quot; |
| CRITICAL | &quot;Critical&quot; |



