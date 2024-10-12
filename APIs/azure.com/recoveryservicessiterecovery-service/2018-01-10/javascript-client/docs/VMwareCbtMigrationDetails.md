# SiteRecoveryManagementClient.VMwareCbtMigrationDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataMoverRunAsAccountId** | **String** | The data mover RunAs account Id. | [optional] [readonly] 
**initialSeedingProgressPercentage** | **Number** | The initial seeding progress percentage. | [optional] [readonly] 
**lastRecoveryPointId** | **String** | The last recovery point Id. | [optional] [readonly] 
**lastRecoveryPointReceived** | **Date** | The last recovery point received time. | [optional] [readonly] 
**licenseType** | **String** | License Type of the VM to be used. | [optional] 
**migrationProgressPercentage** | **Number** | The migration progress percentage. | [optional] [readonly] 
**migrationRecoveryPointId** | **String** | The recovery point Id to which the VM was migrated. | [optional] [readonly] 
**osType** | **String** | The type of the OS on the VM. | [optional] [readonly] 
**performAutoResync** | **String** | A value indicating whether auto resync is to be done. | [optional] 
**protectedDisks** | [**[VMwareCbtProtectedDiskDetails]**](VMwareCbtProtectedDiskDetails.md) | The list of protected disks. | [optional] 
**resyncProgressPercentage** | **Number** | The resync progress percentage. | [optional] [readonly] 
**resyncState** | **String** | The resync state. | [optional] [readonly] 
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



## Enum: ResyncStateEnum


* `None` (value: `"None"`)

* `PreparedForResynchronization` (value: `"PreparedForResynchronization"`)

* `StartedResynchronization` (value: `"StartedResynchronization"`)




