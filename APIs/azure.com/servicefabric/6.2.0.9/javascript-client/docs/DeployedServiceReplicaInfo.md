# ServiceFabricClientApis.DeployedServiceReplicaInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The last address returned by the replica in Open or ChangeRole. | [optional] 
**codePackageName** | **String** | The name of the code package defined in the service manifest. | [optional] 
**hostProcessId** | **String** | Host process ID of the process that is hosting the replica. This will be zero if the replica is down. In hyper-v containers this host process ID will be from different kernel. | [optional] 
**partitionId** | **String** | An internal ID used by Service Fabric to uniquely identify a partition. This is a randomly generated GUID when the service was created. The partition ID is unique and does not change for the lifetime of the service. If the same service was deleted and recreated the IDs of its partitions would be different. | [optional] 
**replicaStatus** | [**ReplicaStatus**](ReplicaStatus.md) |  | [optional] 
**serviceKind** | [**ServiceKind**](ServiceKind.md) |  | 
**serviceManifestName** | **String** | The name of the service manifest. | [optional] 
**serviceName** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. | [optional] 
**servicePackageActivationId** | **String** | The ActivationId of a deployed service package. If ServicePackageActivationMode specified at the time of creating the service is &#39;SharedProcess&#39; (or if it is not specified, in which case it defaults to &#39;SharedProcess&#39;), then value of ServicePackageActivationId is always an empty string. | [optional] 
**serviceTypeName** | **String** | Name of the service type as specified in the service manifest. | [optional] 


