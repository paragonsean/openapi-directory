

# VMwareCbtUpdateMigrationItemInput

VMwareCbt specific update migration item input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | The license type. |  [optional] |
|**performAutoResync** | **String** | A value indicating whether auto resync is to be done. |  [optional] |
|**targetAvailabilitySetId** | **String** | The target availability set ARM Id. |  [optional] |
|**targetBootDiagnosticsStorageAccountId** | **String** | The target boot diagnostics storage account ARM Id. |  [optional] |
|**targetNetworkId** | **String** | The target network ARM Id. |  [optional] |
|**targetResourceGroupId** | **String** | The target resource group ARM Id. |  [optional] |
|**targetVmName** | **String** | The target VM name. |  [optional] |
|**targetVmSize** | **String** | The target VM size. |  [optional] |
|**vmNics** | [**List&lt;VMwareCbtNicInput&gt;**](VMwareCbtNicInput.md) | The list of NIC details. |  [optional] |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| NO_LICENSE_TYPE | &quot;NoLicenseType&quot; |
| WINDOWS_SERVER | &quot;WindowsServer&quot; |



