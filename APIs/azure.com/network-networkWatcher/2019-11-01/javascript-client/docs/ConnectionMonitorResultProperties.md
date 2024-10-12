# NetworkManagementClient.ConnectionMonitorResultProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionMonitorType** | **String** | Type of connection monitor. | [optional] [readonly] 
**monitoringStatus** | **String** | The monitoring status of the connection monitor. | [optional] [readonly] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**startTime** | **Date** | The date and time when the connection monitor was started. | [optional] [readonly] 
**autoStart** | **Boolean** | Determines if the connection monitor will start automatically once created. | [optional] [default to true]
**destination** | [**ConnectionMonitorDestination**](ConnectionMonitorDestination.md) |  | [optional] 
**endpoints** | [**[ConnectionMonitorEndpoint]**](ConnectionMonitorEndpoint.md) | List of connection monitor endpoints. | [optional] 
**monitoringIntervalInSeconds** | **Number** | Monitoring interval in seconds. | [optional] 
**notes** | **String** | Optional notes to be associated with the connection monitor. | [optional] 
**outputs** | [**[ConnectionMonitorOutput]**](ConnectionMonitorOutput.md) | List of connection monitor outputs. | [optional] 
**source** | [**ConnectionMonitorSource**](ConnectionMonitorSource.md) |  | [optional] 
**testConfigurations** | [**[ConnectionMonitorTestConfiguration]**](ConnectionMonitorTestConfiguration.md) | List of connection monitor test configurations. | [optional] 
**testGroups** | [**[ConnectionMonitorTestGroup]**](ConnectionMonitorTestGroup.md) | List of connection monitor test groups. | [optional] 



## Enum: ConnectionMonitorTypeEnum


* `MultiEndpoint` (value: `"MultiEndpoint"`)

* `SingleSourceDestination` (value: `"SingleSourceDestination"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




