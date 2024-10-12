# NetworkAdminManagementClient.VirtualNetworkConfigurationState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostErrors** | [**[VirtualNetworkConfigurationStatus]**](VirtualNetworkConfigurationStatus.md) | List of NIC errors associated with the resource. | [optional] 
**lastUpdatedTime** | **Date** | Last updated time for the running state. | [optional] [readonly] 
**status** | **String** | The virtual network status. | [optional] [readonly] 
**virtualNetworkInterfaceErrors** | [**[VirtualNetworkConfigurationStatus]**](VirtualNetworkConfigurationStatus.md) | List of NIC errors associated with the resource. | [optional] 



## Enum: StatusEnum


* `Failure` (value: `"Failure"`)

* `Warning` (value: `"Warning"`)

* `Success` (value: `"Success"`)

* `Uninitialized` (value: `"Uninitialized"`)

* `InProgress` (value: `"InProgress"`)

* `Unknown` (value: `"Unknown"`)




