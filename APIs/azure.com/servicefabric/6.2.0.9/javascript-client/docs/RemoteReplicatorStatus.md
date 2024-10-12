# ServiceFabricClientApis.RemoteReplicatorStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isInBuild** | **Boolean** | A value that indicates whether the secondary replica is in the process of being built. | [optional] 
**lastAcknowledgementProcessedTimeUtc** | **Date** | The last timestamp (in UTC) when an acknowledgement from the secondary replicator was processed on the primary. UTC 0 represents an invalid value, indicating that no acknowledgement messages were ever processed. | [optional] 
**lastAppliedCopySequenceNumber** | **String** | The highest copy operation sequence number that the secondary has applied to its state. A value of -1 implies that the secondary has applied all copy operations and the copy process is complete. | [optional] 
**lastAppliedReplicationSequenceNumber** | **String** | The highest replication operation sequence number that the secondary has applied to its state. | [optional] 
**lastReceivedCopySequenceNumber** | **String** | The highest copy operation sequence number that the secondary has received from the primary. A value of -1 implies that the secondary has received all copy operations. | [optional] 
**lastReceivedReplicationSequenceNumber** | **String** | The highest replication operation sequence number that the secondary has received from the primary. | [optional] 
**remoteReplicatorAcknowledgementStatus** | [**RemoteReplicatorAcknowledgementStatus**](RemoteReplicatorAcknowledgementStatus.md) |  | [optional] 
**replicaId** | **String** | Id of a stateful service replica. ReplicaId is used by Service Fabric to uniquely identify a replica of a partition. It is unique within a partition and does not change for the lifetime of the replica. If a replica gets dropped and another replica gets created on the same node for the same partition, it will get a different value for the id. Sometimes the id of a stateless service instance is also referred as a replica id. | [optional] 


