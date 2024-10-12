# SiteRecoveryManagementClient.VMwareCbtEnableMigrationInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataMoverRunAsAccountId** | **String** | The data mover RunAs account Id. | 
**disksToInclude** | [**[VMwareCbtDiskInput]**](VMwareCbtDiskInput.md) | The disks to include list. | 
**licenseType** | **String** | License type. | [optional] 
**snapshotRunAsAccountId** | **String** | The snapshot RunAs account Id. | 
**targetAvailabilitySetId** | **String** | The target availability set ARM Id. | [optional] 
**targetBootDiagnosticsStorageAccountId** | **String** | The target boot diagnostics storage account ARM Id. | [optional] 
**targetNetworkId** | **String** | The target network ARM Id. | 
**targetResourceGroupId** | **String** | The target resource group ARM Id. | 
**targetSubnetName** | **String** | The target subnet name. | [optional] 
**targetVmName** | **String** | The target VM name. | [optional] 
**targetVmSize** | **String** | The target VM size. | [optional] 
**vmwareMachineId** | **String** | The ARM Id of the VM discovered in VMware. | 



## Enum: LicenseTypeEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `NoLicenseType` (value: `"NoLicenseType"`)

* `WindowsServer` (value: `"WindowsServer"`)




