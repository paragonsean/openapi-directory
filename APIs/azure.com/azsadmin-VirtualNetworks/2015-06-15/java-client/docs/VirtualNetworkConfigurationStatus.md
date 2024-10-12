

# VirtualNetworkConfigurationStatus

Virtual network configuration status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastUpdatedTime** | **OffsetDateTime** | Last updated time for the configuration status. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The virtual network configuration status. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| FAILURE | &quot;Failure&quot; |
| WARNING | &quot;Warning&quot; |
| SUCCESS | &quot;Success&quot; |
| UNINITIALIZED | &quot;Uninitialized&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| UNKNOWN | &quot;Unknown&quot; |



