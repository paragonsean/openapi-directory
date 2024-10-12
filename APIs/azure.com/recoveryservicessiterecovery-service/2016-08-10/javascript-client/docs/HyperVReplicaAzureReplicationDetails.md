# SiteRecoveryManagementClient.HyperVReplicaAzureReplicationDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureVMDiskDetails** | [**[AzureVmDiskDetails]**](AzureVmDiskDetails.md) | Azure VM Disk details. | [optional] 
**enableRDPOnTargetOption** | **String** | The selected option to enable RDP\\SSH on target vm after failover. String value of {SrsDataContract.EnableRDPOnTargetOption} enum. | [optional] 
**encryption** | **String** | The encryption info. | [optional] 
**initialReplicationDetails** | [**InitialReplicationDetails**](InitialReplicationDetails.md) |  | [optional] 
**lastReplicatedTime** | **Date** | The Last replication time. | [optional] 
**licenseType** | **String** | License Type of the VM to be used. | [optional] 
**oSDetails** | [**OSDetails**](OSDetails.md) |  | [optional] 
**recoveryAvailabilitySetId** | **String** | The recovery availability set Id. | [optional] 
**recoveryAzureLogStorageAccountId** | **String** | The ARM id of the log storage account used for replication. This will be set to null if no log storage account was provided during enable protection. | [optional] 
**recoveryAzureResourceGroupId** | **String** | The target resource group Id. | [optional] 
**recoveryAzureStorageAccount** | **String** | The recovery Azure storage account. | [optional] 
**recoveryAzureVMName** | **String** | Recovery Azure given name. | [optional] 
**recoveryAzureVMSize** | **String** | The Recovery Azure VM size. | [optional] 
**selectedRecoveryAzureNetworkId** | **String** | The selected recovery azure network Id. | [optional] 
**sourceVmCPUCount** | **Number** | The CPU count of the VM on the primary side. | [optional] 
**sourceVmRAMSizeInMB** | **Number** | The RAM size of the VM on the primary side. | [optional] 
**useManagedDisks** | **String** | A value indicating whether managed disks should be used during failover. | [optional] 
**vmId** | **String** | The virtual machine Id. | [optional] 
**vmNics** | [**[VMNicDetails]**](VMNicDetails.md) | The PE Network details. | [optional] 
**vmProtectionState** | **String** | The protection state for the vm. | [optional] 
**vmProtectionStateDescription** | **String** | The protection state description for the vm. | [optional] 


