# ServiceFabricClientApis.SelectedPartition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitionId** | **String** | An internal ID used by Service Fabric to uniquely identify a partition. This is a randomly generated GUID when the service was created. The partition id is unique and does not change for the lifetime of the service. If the same service was deleted and recreated the ids of its partitions would be different. | [optional] 
**serviceName** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. | [optional] 


