

# AlertProperties

Properties of alert

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertType** | **String** | Type of the alert |  |
|**appearedAtSourceTime** | **OffsetDateTime** | UTC time at which the alert appeared on the source |  |
|**appearedAtTime** | **OffsetDateTime** | UTC time at which the alert appeared |  |
|**clearedAtSourceTime** | **OffsetDateTime** | UTC time at which the alert was cleared on the source |  [optional] |
|**clearedAtTime** | **OffsetDateTime** | UTC time at which the alert got cleared |  [optional] |
|**detailedInformation** | **Map&lt;String, String&gt;** | Other information about the alert |  [optional] |
|**errorDetails** | [**AlertErrorDetails**](AlertErrorDetails.md) |  |  [optional] |
|**recommendation** | **String** | Recommendation for acting on the alert |  [optional] |
|**resolutionReason** | **String** | Reason for resolving the alert |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | Device or Resource alert |  |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of the alert |  |
|**source** | [**AlertSource**](AlertSource.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of the alert |  |
|**title** | **String** | Title of the alert |  |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| RESOURCE | &quot;Resource&quot; |
| DEVICE | &quot;Device&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| INFORMATIONAL | &quot;Informational&quot; |
| WARNING | &quot;Warning&quot; |
| CRITICAL | &quot;Critical&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| CLEARED | &quot;Cleared&quot; |



