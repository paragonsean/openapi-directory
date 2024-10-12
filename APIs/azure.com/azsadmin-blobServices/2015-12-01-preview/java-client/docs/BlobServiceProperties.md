

# BlobServiceProperties

Blob service properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**settings** | [**BlobServiceSettings**](BlobServiceSettings.md) |  |  [optional] |
|**healthStatus** | [**HealthStatusEnum**](#HealthStatusEnum) | Current health status. |  [optional] [readonly] |
|**version** | **String** | Storage service version. |  [optional] |



## Enum: HealthStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| HEALTHY | &quot;Healthy&quot; |
| WARNING | &quot;Warning&quot; |
| CRITICAL | &quot;Critical&quot; |



