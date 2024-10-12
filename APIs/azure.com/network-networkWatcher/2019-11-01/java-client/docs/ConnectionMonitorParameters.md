

# ConnectionMonitorParameters

Parameters that define the operation to create a connection monitor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoStart** | **Boolean** | Determines if the connection monitor will start automatically once created. |  [optional] |
|**destination** | [**ConnectionMonitorDestination**](ConnectionMonitorDestination.md) |  |  [optional] |
|**endpoints** | [**List&lt;ConnectionMonitorEndpoint&gt;**](ConnectionMonitorEndpoint.md) | List of connection monitor endpoints. |  [optional] |
|**monitoringIntervalInSeconds** | **Integer** | Monitoring interval in seconds. |  [optional] |
|**notes** | **String** | Optional notes to be associated with the connection monitor. |  [optional] |
|**outputs** | [**List&lt;ConnectionMonitorOutput&gt;**](ConnectionMonitorOutput.md) | List of connection monitor outputs. |  [optional] |
|**source** | [**ConnectionMonitorSource**](ConnectionMonitorSource.md) |  |  [optional] |
|**testConfigurations** | [**List&lt;ConnectionMonitorTestConfiguration&gt;**](ConnectionMonitorTestConfiguration.md) | List of connection monitor test configurations. |  [optional] |
|**testGroups** | [**List&lt;ConnectionMonitorTestGroup&gt;**](ConnectionMonitorTestGroup.md) | List of connection monitor test groups. |  [optional] |



