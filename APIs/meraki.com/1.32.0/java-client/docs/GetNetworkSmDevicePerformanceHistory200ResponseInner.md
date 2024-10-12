

# GetNetworkSmDevicePerformanceHistory200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cpuPercentUsed** | **Float** | The percentage of CPU used as a decimal format. |  [optional] |
|**diskUsage** | [**GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsage**](GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsage.md) |  |  [optional] |
|**memActive** | **Integer** | The active RAM on the device. |  [optional] |
|**memFree** | **Integer** | Memory that is not yet in use by the system. |  [optional] |
|**memInactive** | **Integer** | The inactive RAM on the device. |  [optional] |
|**memWired** | **Integer** | Memory used for core OS functions on the device. |  [optional] |
|**networkReceived** | **Integer** | Network bandwith received. |  [optional] |
|**networkSent** | **Integer** | Network bandwith transmitted. |  [optional] |
|**swapUsed** | **Integer** | The amount of space being used on the startup disk to swap unused files to and from RAM. |  [optional] |
|**ts** | **String** | The time at which the performance was measured. |  [optional] |



