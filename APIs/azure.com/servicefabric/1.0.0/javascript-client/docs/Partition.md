# ServiceFabricClient.Partition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentConfigurationEpoch** | [**PartitionCurrentConfigurationEpoch**](PartitionCurrentConfigurationEpoch.md) |  | [optional] 
**healthState** | [**HealthState**](HealthState.md) |  | [optional] 
**instanceCount** | **Number** |  | [optional] 
**minReplicaSetSize** | **Number** |  | [optional] 
**partitionInformation** | [**PartitionInformation**](PartitionInformation.md) |  | [optional] 
**partitionStatus** | **String** |  | [optional] 
**serviceKind** | [**ServiceKind**](ServiceKind.md) |  | [optional] 
**targetReplicaSetSize** | **Number** |  | [optional] 



## Enum: PartitionStatusEnum


* `Invalid` (value: `"Invalid"`)

* `Ready` (value: `"Ready"`)

* `NotReady` (value: `"NotReady"`)

* `InQuorumLoss` (value: `"InQuorumLoss"`)

* `Reconfiguring` (value: `"Reconfiguring"`)

* `Deleting` (value: `"Deleting"`)




