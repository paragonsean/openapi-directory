

# VirtualNetworkConfigurationState

The virtual network configuration state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostErrors** | [**List&lt;VirtualNetworkConfigurationStatus&gt;**](VirtualNetworkConfigurationStatus.md) | List of NIC errors associated with the resource. |  [optional] |
|**lastUpdatedTime** | **OffsetDateTime** | Last updated time for the running state. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The virtual network status. |  [optional] [readonly] |
|**virtualNetworkInterfaceErrors** | [**List&lt;VirtualNetworkConfigurationStatus&gt;**](VirtualNetworkConfigurationStatus.md) | List of NIC errors associated with the resource. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| FAILURE | &quot;Failure&quot; |
| WARNING | &quot;Warning&quot; |
| SUCCESS | &quot;Success&quot; |
| UNINITIALIZED | &quot;Uninitialized&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| UNKNOWN | &quot;Unknown&quot; |



