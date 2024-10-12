# CloudMonitoringApi.MetricsScope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when this Metrics Scope was created. | [optional] [readonly] 
**monitoredProjects** | [**[MonitoredProject]**](MonitoredProject.md) | Output only. The list of projects monitored by this Metrics Scope. | [optional] [readonly] 
**name** | **String** | Immutable. The resource name of the Monitoring Metrics Scope. On input, the resource name can be specified with the scoping project ID or number. On output, the resource name is specified with the scoping project number. Example: locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER} | [optional] 
**updateTime** | **String** | Output only. The time when this Metrics Scope record was last updated. | [optional] [readonly] 


