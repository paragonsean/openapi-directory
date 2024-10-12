

# VMwareCbtEnableMigrationInput

VMwareCbt specific enable migration input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataMoverRunAsAccountId** | **String** | The data mover RunAs account Id. |  |
|**disksToInclude** | [**List&lt;VMwareCbtDiskInput&gt;**](VMwareCbtDiskInput.md) | The disks to include list. |  |
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | License type. |  [optional] |
|**performAutoResync** | **String** | A value indicating whether auto resync is to be done. |  [optional] |
|**snapshotRunAsAccountId** | **String** | The snapshot RunAs account Id. |  |
|**targetAvailabilitySetId** | **String** | The target availability set ARM Id. |  [optional] |
|**targetBootDiagnosticsStorageAccountId** | **String** | The target boot diagnostics storage account ARM Id. |  [optional] |
|**targetNetworkId** | **String** | The target network ARM Id. |  |
|**targetResourceGroupId** | **String** | The target resource group ARM Id. |  |
|**targetSubnetName** | **String** | The target subnet name. |  [optional] |
|**targetVmName** | **String** | The target VM name. |  [optional] |
|**targetVmSize** | **String** | The target VM size. |  [optional] |
|**vmwareMachineId** | **String** | The ARM Id of the VM discovered in VMware. |  |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| NO_LICENSE_TYPE | &quot;NoLicenseType&quot; |
| WINDOWS_SERVER | &quot;WindowsServer&quot; |



