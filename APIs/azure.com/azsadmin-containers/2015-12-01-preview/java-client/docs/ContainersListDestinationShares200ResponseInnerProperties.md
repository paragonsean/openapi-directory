

# ContainersListDestinationShares200ResponseInnerProperties

Storage share properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**freeCapacity** | **Long** | The free space of the storage share in bytes. |  [optional] [readonly] |
|**healthStatus** | [**HealthStatusEnum**](#HealthStatusEnum) | Current health status. |  [optional] [readonly] |
|**shareName** | **String** | The name of the storage share. |  [optional] [readonly] |
|**totalCapacity** | **Long** | The total capacity of the storage share in bytes. |  [optional] [readonly] |
|**uncPath** | **String** | The UNC path to the storage share. |  [optional] [readonly] |
|**usedCapacity** | **Long** | The used capacity of the storage share in bytes. |  [optional] [readonly] |



## Enum: HealthStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| HEALTHY | &quot;Healthy&quot; |
| WARNING | &quot;Warning&quot; |
| CRITICAL | &quot;Critical&quot; |



