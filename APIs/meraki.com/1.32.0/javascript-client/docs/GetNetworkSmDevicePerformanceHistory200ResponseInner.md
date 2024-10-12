# MerakiDashboardApi.GetNetworkSmDevicePerformanceHistory200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpuPercentUsed** | **Number** | The percentage of CPU used as a decimal format. | [optional] 
**diskUsage** | [**GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsage**](GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsage.md) |  | [optional] 
**memActive** | **Number** | The active RAM on the device. | [optional] 
**memFree** | **Number** | Memory that is not yet in use by the system. | [optional] 
**memInactive** | **Number** | The inactive RAM on the device. | [optional] 
**memWired** | **Number** | Memory used for core OS functions on the device. | [optional] 
**networkReceived** | **Number** | Network bandwith received. | [optional] 
**networkSent** | **Number** | Network bandwith transmitted. | [optional] 
**swapUsed** | **Number** | The amount of space being used on the startup disk to swap unused files to and from RAM. | [optional] 
**ts** | **String** | The time at which the performance was measured. | [optional] 


