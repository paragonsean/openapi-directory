# SiteRecoveryManagementClient.HyperVReplicaAzurePolicyDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeStorageAccountId** | **String** | The active storage account Id. | [optional] 
**applicationConsistentSnapshotFrequencyInHours** | **Number** | The interval (in hours) at which Hyper-V Replica should create an application consistent snapshot within the VM. | [optional] 
**encryption** | **String** | A value indicating whether encryption is enabled for virtual machines in this cloud. | [optional] 
**onlineReplicationStartTime** | **String** | The scheduled start time for the initial replication. If this parameter is Null, the initial replication starts immediately. | [optional] 
**recoveryPointHistoryDurationInHours** | **Number** | The duration (in hours) to which point the recovery history needs to be maintained. | [optional] 
**replicationInterval** | **Number** | The replication interval. | [optional] 


