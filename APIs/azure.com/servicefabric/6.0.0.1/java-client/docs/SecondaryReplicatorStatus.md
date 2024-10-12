

# SecondaryReplicatorStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copyQueueStatus** | [**ReplicatorQueueStatus**](ReplicatorQueueStatus.md) |  |  [optional] |
|**isInBuild** | **Boolean** | Value that indicates whether the replica is currently being built. |  [optional] |
|**lastAcknowledgementSentTimeUtc** | **OffsetDateTime** | The last time-stamp (UTC) at which an acknowledgment was sent to the primary replicator. UTC 0 represents an invalid value, indicating that an acknowledgment message was never sent.  |  [optional] |
|**lastCopyOperationReceivedTimeUtc** | **OffsetDateTime** | The last time-stamp (UTC) at which a copy operation was received from the primary. UTC 0 represents an invalid value, indicating that a copy operation message was never received.  |  [optional] |
|**lastReplicationOperationReceivedTimeUtc** | **OffsetDateTime** | The last time-stamp (UTC) at which a replication operation was received from the primary. UTC 0 represents an invalid value, indicating that a replication operation message was never received.  |  [optional] |
|**replicationQueueStatus** | [**ReplicatorQueueStatus**](ReplicatorQueueStatus.md) |  |  [optional] |



