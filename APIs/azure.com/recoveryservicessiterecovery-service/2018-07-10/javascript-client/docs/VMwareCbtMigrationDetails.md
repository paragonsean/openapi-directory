# SiteRecoveryManagementClient.VMwareCbtMigrationDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataMoverRunAsAccountId** | **String** | The data mover RunAs account Id. | [optional] [readonly] 
**lastRecoveryPointReceived** | **Date** | The last recovery point received time. | [optional] [readonly] 
**licenseType** | **String** | License Type of the VM to be used. | [optional] 
**migrationRecoveryPointId** | **String** | The recovery point Id to which the VM was migrated. | [optional] [readonly] 
**osType** | **String** | The type of the OS on the VM. | [optional] [readonly] 
**protectedDisks** | [**[VMwareCbtProtectedDiskDetails]**](VMwareCbtProtectedDiskDetails.md) | The list of protected disks. | [optional] 
**snapshotRunAsAccountId** | **String** | The snapshot RunAs account Id. | [optional] [readonly] 
**targetAvailabilitySetId** | **String** | The target availability set Id. | [optional] 
**targetBootDiagnosticsStorageAccountId** | **String** | The target boot diagnostics storage account ARM Id. | [optional] 
**targetLocation** | **String** | The target location. | [optional] [readonly] 
**targetNetworkId** | **String** | The target network Id. | [optional] 
**targetResourceGroupId** | **String** | The target resource group Id. | [optional] 
**targetVmName** | **String** | Target VM name. | [optional] 
**targetVmSize** | **String** | The target VM size. | [optional] 
**vmNics** | [**[VMwareCbtNicDetails]**](VMwareCbtNicDetails.md) | The network details. | [optional] 
**vmwareMachineId** | **String** | The ARM Id of the VM discovered in VMware. | [optional] [readonly] 


