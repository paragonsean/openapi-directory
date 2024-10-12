

# ConnectionMonitorResultProperties

Describes the properties of a connection monitor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionMonitorType** | [**ConnectionMonitorTypeEnum**](#ConnectionMonitorTypeEnum) | Type of connection monitor. |  [optional] [readonly] |
|**monitoringStatus** | **String** | The monitoring status of the connection monitor. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | The date and time when the connection monitor was started. |  [optional] [readonly] |
|**autoStart** | **Boolean** | Determines if the connection monitor will start automatically once created. |  [optional] |
|**destination** | [**ConnectionMonitorDestination**](ConnectionMonitorDestination.md) |  |  [optional] |
|**endpoints** | [**List&lt;ConnectionMonitorEndpoint&gt;**](ConnectionMonitorEndpoint.md) | List of connection monitor endpoints. |  [optional] |
|**monitoringIntervalInSeconds** | **Integer** | Monitoring interval in seconds. |  [optional] |
|**notes** | **String** | Optional notes to be associated with the connection monitor. |  [optional] |
|**outputs** | [**List&lt;ConnectionMonitorOutput&gt;**](ConnectionMonitorOutput.md) | List of connection monitor outputs. |  [optional] |
|**source** | [**ConnectionMonitorSource**](ConnectionMonitorSource.md) |  |  [optional] |
|**testConfigurations** | [**List&lt;ConnectionMonitorTestConfiguration&gt;**](ConnectionMonitorTestConfiguration.md) | List of connection monitor test configurations. |  [optional] |
|**testGroups** | [**List&lt;ConnectionMonitorTestGroup&gt;**](ConnectionMonitorTestGroup.md) | List of connection monitor test groups. |  [optional] |



## Enum: ConnectionMonitorTypeEnum

| Name | Value |
|---- | -----|
| MULTI_ENDPOINT | &quot;MultiEndpoint&quot; |
| SINGLE_SOURCE_DESTINATION | &quot;SingleSourceDestination&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



