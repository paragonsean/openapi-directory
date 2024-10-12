

# TableServiceProperties

Table service properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**settings** | [**Object**](Object.md) | Settings of storage services. |  [optional] |
|**healthStatus** | [**HealthStatusEnum**](#HealthStatusEnum) | Current health status. |  [optional] [readonly] |
|**version** | **String** | Storage service version. |  [optional] |



## Enum: HealthStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| HEALTHY | &quot;Healthy&quot; |
| WARNING | &quot;Warning&quot; |
| CRITICAL | &quot;Critical&quot; |



