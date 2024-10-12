# ServiceFabricClientApis.ReplicatorQueueStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committedSequenceNumber** | **String** | On a primary replicator, this is semantically the highest sequence number of the operation for which a write quorum of the secondary replicas have sent an acknowledgement. On a secondary replicator, this is semantically the highest sequence number of the in-order operation received from the primary. | [optional] 
**completedSequenceNumber** | **String** | On a primary replicator, this is semantically the highest sequence number of the operation for which all the secondary replicas have sent an acknowledgement. On a secondary replicator, this is semantically the highest sequence number that has been applied to the persistent state. | [optional] 
**firstSequenceNumber** | **String** | On a primary replicator, this is semantically the sequence number of the operation for which all the secondary replicas have sent an acknowledgement. On a secondary replicator, this is the smallest sequence number of the operation that is present in the queue. | [optional] 
**lastSequenceNumber** | **String** | Represents the latest sequence number of the operation that is available in the queue. | [optional] 
**queueMemorySize** | **String** | Represents the virtual memory consumed by the queue in bytes. | [optional] 
**queueUtilizationPercentage** | **Number** | Represents the utilization of the queue. A value of 0 indicates that the queue is empty and a value of 100 indicates the queue is full. | [optional] 


