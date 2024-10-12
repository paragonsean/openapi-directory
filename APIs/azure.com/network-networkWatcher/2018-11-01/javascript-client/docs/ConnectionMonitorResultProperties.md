# NetworkManagementClient.ConnectionMonitorResultProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitoringStatus** | **String** | The monitoring status of the connection monitor. | [optional] 
**provisioningState** | **String** | The provisioning state of the connection monitor. | [optional] 
**startTime** | **Date** | The date and time when the connection monitor was started. | [optional] 
**autoStart** | **Boolean** | Determines if the connection monitor will start automatically once created. | [optional] [default to true]
**destination** | [**ConnectionMonitorDestination**](ConnectionMonitorDestination.md) |  | 
**monitoringIntervalInSeconds** | **Number** | Monitoring interval in seconds. | [optional] 
**source** | [**ConnectionMonitorSource**](ConnectionMonitorSource.md) |  | 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




