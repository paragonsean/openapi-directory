

# HyperVReplicaAzureReplicationDetails

Hyper V Replica Azure provider specific settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureVmDiskDetails** | [**List&lt;AzureVmDiskDetails&gt;**](AzureVmDiskDetails.md) | Azure VM Disk details. |  [optional] |
|**enableRdpOnTargetOption** | **String** | The selected option to enable RDP\\SSH on target vm after failover. String value of {SrsDataContract.EnableRDPOnTargetOption} enum. |  [optional] |
|**encryption** | **String** | The encryption info. |  [optional] |
|**initialReplicationDetails** | [**InitialReplicationDetails**](InitialReplicationDetails.md) |  |  [optional] |
|**lastReplicatedTime** | **OffsetDateTime** | The Last replication time. |  [optional] |
|**lastRpoCalculatedTime** | **OffsetDateTime** | The last RPO calculated time. |  [optional] |
|**licenseType** | **String** | License Type of the VM to be used. |  [optional] |
|**oSDetails** | [**OSDetails**](OSDetails.md) |  |  [optional] |
|**recoveryAvailabilitySetId** | **String** | The recovery availability set Id. |  [optional] |
|**recoveryAzureLogStorageAccountId** | **String** | The ARM id of the log storage account used for replication. This will be set to null if no log storage account was provided during enable protection. |  [optional] |
|**recoveryAzureResourceGroupId** | **String** | The target resource group Id. |  [optional] |
|**recoveryAzureStorageAccount** | **String** | The recovery Azure storage account. |  [optional] |
|**recoveryAzureVMSize** | **String** | The Recovery Azure VM size. |  [optional] |
|**recoveryAzureVmName** | **String** | Recovery Azure given name. |  [optional] |
|**rpoInSeconds** | **Long** | Last RPO value. |  [optional] |
|**selectedRecoveryAzureNetworkId** | **String** | The selected recovery azure network Id. |  [optional] |
|**selectedSourceNicId** | **String** | The selected source nic Id which will be used as the primary nic during failover. |  [optional] |
|**sourceVmCpuCount** | **Integer** | The CPU count of the VM on the primary side. |  [optional] |
|**sourceVmRamSizeInMB** | **Integer** | The RAM size of the VM on the primary side. |  [optional] |
|**useManagedDisks** | **String** | A value indicating whether managed disks should be used during failover. |  [optional] |
|**vmId** | **String** | The virtual machine Id. |  [optional] |
|**vmNics** | [**List&lt;VMNicDetails&gt;**](VMNicDetails.md) | The PE Network details. |  [optional] |
|**vmProtectionState** | **String** | The protection state for the vm. |  [optional] |
|**vmProtectionStateDescription** | **String** | The protection state description for the vm. |  [optional] |



