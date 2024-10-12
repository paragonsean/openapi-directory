# ServiceFabricClientApis.StatefulServicePartitionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentConfigurationEpoch** | [**Epoch**](Epoch.md) |  | [optional] 
**lastQuorumLossDuration** | **String** | The duration for which this partition was in quorum loss. If the partition is currently in quorum loss, it returns the duration since it has been in that state. This field is using ISO8601 format for specifying the duration. | [optional] 
**minReplicaSetSize** | **Number** | The minimum replica set size as a number. | [optional] 
**targetReplicaSetSize** | **Number** | The target replica set size as a number. | [optional] 


