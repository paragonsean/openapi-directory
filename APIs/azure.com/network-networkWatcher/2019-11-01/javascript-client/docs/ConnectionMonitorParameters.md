# NetworkManagementClient.ConnectionMonitorParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoStart** | **Boolean** | Determines if the connection monitor will start automatically once created. | [optional] [default to true]
**destination** | [**ConnectionMonitorDestination**](ConnectionMonitorDestination.md) |  | [optional] 
**endpoints** | [**[ConnectionMonitorEndpoint]**](ConnectionMonitorEndpoint.md) | List of connection monitor endpoints. | [optional] 
**monitoringIntervalInSeconds** | **Number** | Monitoring interval in seconds. | [optional] 
**notes** | **String** | Optional notes to be associated with the connection monitor. | [optional] 
**outputs** | [**[ConnectionMonitorOutput]**](ConnectionMonitorOutput.md) | List of connection monitor outputs. | [optional] 
**source** | [**ConnectionMonitorSource**](ConnectionMonitorSource.md) |  | [optional] 
**testConfigurations** | [**[ConnectionMonitorTestConfiguration]**](ConnectionMonitorTestConfiguration.md) | List of connection monitor test configurations. | [optional] 
**testGroups** | [**[ConnectionMonitorTestGroup]**](ConnectionMonitorTestGroup.md) | List of connection monitor test groups. | [optional] 


