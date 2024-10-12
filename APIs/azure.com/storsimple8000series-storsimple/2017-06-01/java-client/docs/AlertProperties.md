

# AlertProperties

The properties of alert

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertType** | **String** | The type of the alert |  |
|**appearedAtSourceTime** | **OffsetDateTime** | The source time at which the alert was raised |  |
|**appearedAtTime** | **OffsetDateTime** | The UTC time at which the alert was raised |  |
|**clearedAtSourceTime** | **OffsetDateTime** | The source time at which the alert was cleared |  [optional] |
|**clearedAtTime** | **OffsetDateTime** | The UTC time at which the alert was cleared |  [optional] |
|**detailedInformation** | **Map&lt;String, String&gt;** | More details about the alert |  [optional] |
|**errorDetails** | [**AlertErrorDetails**](AlertErrorDetails.md) |  |  [optional] |
|**recommendation** | **String** | The recommended action for the issue raised in the alert |  [optional] |
|**resolutionReason** | **String** | The reason for resolving the alert |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | The scope of the alert |  |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The severity of the alert |  |
|**source** | [**AlertSource**](AlertSource.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the alert |  |
|**title** | **String** | The title of the alert |  |



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



