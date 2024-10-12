# ServiceFabricClientApis.ServiceCreatedEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationName** | **String** | Application name. | 
**applicationTypeName** | **String** | Application type name. | 
**isStateful** | **Boolean** | Indicates if Service is stateful. | 
**minReplicaSetSize** | **Number** | Minimum size of replicas set. | 
**partitionCount** | **Number** | Number of partitions. | 
**partitionId** | **String** | An internal ID used by Service Fabric to uniquely identify a partition. This is a randomly generated GUID when the service was created. The partition ID is unique and does not change for the lifetime of the service. If the same service was deleted and recreated the IDs of its partitions would be different. | 
**serviceInstance** | **Number** | Id of Service instance. | 
**servicePackageVersion** | **String** | Version of Service package. | 
**serviceTypeName** | **String** | Service type name. | 
**targetReplicaSetSize** | **Number** | Size of target replicas set. | 


