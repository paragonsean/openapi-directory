# ServiceFabricClientApis.RemoteReplicatorAcknowledgementDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**averageApplyDuration** | **String** | Represents the average duration it takes for the remote replicator to apply an operation. This usually entails writing the operation to disk. | [optional] 
**averageReceiveDuration** | **String** | Represents the average duration it takes for the remote replicator to receive an operation. | [optional] 
**notReceivedCount** | **String** | Represents the number of operations not yet received by a remote replicator. | [optional] 
**receivedAndNotAppliedCount** | **String** | Represents the number of operations received and not yet applied by a remote replicator. | [optional] 


