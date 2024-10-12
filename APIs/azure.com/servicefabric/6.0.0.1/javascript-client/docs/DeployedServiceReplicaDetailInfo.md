# ServiceFabricClientApis.DeployedServiceReplicaDetailInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentServiceOperation** | [**ServiceOperationName**](ServiceOperationName.md) |  | [optional] 
**currentServiceOperationStartTimeUtc** | **Date** | The start time of the current service operation in UTC format. | [optional] 
**partitionId** | **String** | An internal ID used by Service Fabric to uniquely identify a partition. This is a randomly generated GUID when the service was created. The partition id is unique and does not change for the lifetime of the service. If the same service was deleted and recreated the ids of its partitions would be different. | [optional] 
**reportedLoad** | [**[LoadMetricReportInfo]**](LoadMetricReportInfo.md) | List of load reported by replica. | [optional] 
**serviceKind** | [**ServiceKind**](ServiceKind.md) |  | 
**serviceName** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. | [optional] 


