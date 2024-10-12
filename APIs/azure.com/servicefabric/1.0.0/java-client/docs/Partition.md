

# Partition

The partition

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentConfigurationEpoch** | [**PartitionCurrentConfigurationEpoch**](PartitionCurrentConfigurationEpoch.md) |  |  [optional] |
|**healthState** | **HealthState** |  |  [optional] |
|**instanceCount** | **Integer** |  |  [optional] |
|**minReplicaSetSize** | **Integer** |  |  [optional] |
|**partitionInformation** | [**PartitionInformation**](PartitionInformation.md) |  |  [optional] |
|**partitionStatus** | [**PartitionStatusEnum**](#PartitionStatusEnum) |  |  [optional] |
|**serviceKind** | **ServiceKind** |  |  [optional] |
|**targetReplicaSetSize** | **Integer** |  |  [optional] |



## Enum: PartitionStatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| READY | &quot;Ready&quot; |
| NOT_READY | &quot;NotReady&quot; |
| IN_QUORUM_LOSS | &quot;InQuorumLoss&quot; |
| RECONFIGURING | &quot;Reconfiguring&quot; |
| DELETING | &quot;Deleting&quot; |



