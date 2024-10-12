# SiteRecoveryManagementClient.HyperVReplicaAzurePolicyInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationConsistentSnapshotFrequencyInHours** | **Number** | The interval (in hours) at which Hyper-V Replica should create an application consistent snapshot within the VM. | [optional] 
**onlineReplicationStartTime** | **String** | The scheduled start time for the initial replication. If this parameter is Null, the initial replication starts immediately. | [optional] 
**recoveryPointHistoryDuration** | **Number** | The duration (in hours) to which point the recovery history needs to be maintained. | [optional] 
**replicationInterval** | **Number** | The replication interval. | [optional] 
**storageAccounts** | **[String]** | The list of storage accounts to which the VMs in the primary cloud can replicate to. | [optional] 


