

# HyperVReplicaAzureUpdateReplicationProtectedItemInput

HyperV replica Azure input to update replication protected item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskIdToDiskEncryptionMap** | **Map&lt;String, String&gt;** | The dictionary of disk resource Id to disk encryption set ARM Id. |  [optional] |
|**recoveryAzureV1ResourceGroupId** | **String** | The recovery Azure resource group Id for classic deployment. |  [optional] |
|**recoveryAzureV2ResourceGroupId** | **String** | The recovery Azure resource group Id for resource manager deployment. |  [optional] |
|**useManagedDisks** | **String** | A value indicating whether managed disks should be used during failover. |  [optional] |



