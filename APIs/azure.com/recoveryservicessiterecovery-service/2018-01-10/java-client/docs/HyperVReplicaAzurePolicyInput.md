

# HyperVReplicaAzurePolicyInput

Hyper-V Replica Azure specific input for creating a protection profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationConsistentSnapshotFrequencyInHours** | **Integer** | The interval (in hours) at which Hyper-V Replica should create an application consistent snapshot within the VM. |  [optional] |
|**onlineReplicationStartTime** | **String** | The scheduled start time for the initial replication. If this parameter is Null, the initial replication starts immediately. |  [optional] |
|**recoveryPointHistoryDuration** | **Integer** | The duration (in hours) to which point the recovery history needs to be maintained. |  [optional] |
|**replicationInterval** | **Integer** | The replication interval. |  [optional] |
|**storageAccounts** | **List&lt;String&gt;** | The list of storage accounts to which the VMs in the primary cloud can replicate to. |  [optional] |



