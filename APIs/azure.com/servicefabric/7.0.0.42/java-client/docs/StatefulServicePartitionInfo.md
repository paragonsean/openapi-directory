

# StatefulServicePartitionInfo

Information about a partition of a stateful Service Fabric service..

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastQuorumLossDuration** | **String** | The duration for which this partition was in quorum loss. If the partition is currently in quorum loss, it returns the duration since it has been in that state. This field is using ISO8601 format for specifying the duration. |  [optional] |
|**minReplicaSetSize** | **Long** | The minimum replica set size as a number. |  [optional] |
|**primaryEpoch** | [**Epoch**](Epoch.md) |  |  [optional] |
|**targetReplicaSetSize** | **Long** | The target replica set size as a number. |  [optional] |



