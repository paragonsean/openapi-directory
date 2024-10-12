

# AlertFilter

Filters that can be specified on the alert

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appearedOnTime** | **OffsetDateTime** | UTC time on which the alert appeared |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of the alert |  [optional] |
|**sourceName** | **String** | Source name of the alert |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Source of the alert |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the alert |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| INFORMATIONAL | &quot;Informational&quot; |
| WARNING | &quot;Warning&quot; |
| CRITICAL | &quot;Critical&quot; |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| RESOURCE | &quot;Resource&quot; |
| DEVICE | &quot;Device&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| CLEARED | &quot;Cleared&quot; |



