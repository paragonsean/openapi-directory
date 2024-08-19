

# ConnectionMonitorResultProperties

Describes the properties of a connection monitor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**monitoringStatus** | **String** | The monitoring status of the connection monitor. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | The date and time when the connection monitor was started. |  [optional] |
|**autoStart** | **Boolean** | Determines if the connection monitor will start automatically once created. |  [optional] |
|**destination** | [**ConnectionMonitorDestination**](ConnectionMonitorDestination.md) |  |  |
|**monitoringIntervalInSeconds** | **Integer** | Monitoring interval in seconds. |  [optional] |
|**source** | [**ConnectionMonitorSource**](ConnectionMonitorSource.md) |  |  |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



