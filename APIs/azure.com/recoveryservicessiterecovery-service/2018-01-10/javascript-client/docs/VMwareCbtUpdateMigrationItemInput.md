# SiteRecoveryManagementClient.VMwareCbtUpdateMigrationItemInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**licenseType** | **String** | The license type. | [optional] 
**performAutoResync** | **String** | A value indicating whether auto resync is to be done. | [optional] 
**targetAvailabilitySetId** | **String** | The target availability set ARM Id. | [optional] 
**targetBootDiagnosticsStorageAccountId** | **String** | The target boot diagnostics storage account ARM Id. | [optional] 
**targetNetworkId** | **String** | The target network ARM Id. | [optional] 
**targetResourceGroupId** | **String** | The target resource group ARM Id. | [optional] 
**targetVmName** | **String** | The target VM name. | [optional] 
**targetVmSize** | **String** | The target VM size. | [optional] 
**vmNics** | [**[VMwareCbtNicInput]**](VMwareCbtNicInput.md) | The list of NIC details. | [optional] 



## Enum: LicenseTypeEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `NoLicenseType` (value: `"NoLicenseType"`)

* `WindowsServer` (value: `"WindowsServer"`)




