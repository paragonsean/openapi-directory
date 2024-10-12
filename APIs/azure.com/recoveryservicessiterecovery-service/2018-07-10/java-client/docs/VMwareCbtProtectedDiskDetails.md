

# VMwareCbtProtectedDiskDetails

VMwareCbt protected disk details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacityInBytes** | **Long** | The disk capacity in bytes. |  [optional] [readonly] |
|**diskId** | **String** | The disk id. |  [optional] [readonly] |
|**diskName** | **String** | The disk name. |  [optional] [readonly] |
|**diskPath** | **String** | The disk path. |  [optional] [readonly] |
|**diskType** | [**DiskTypeEnum**](#DiskTypeEnum) | The disk type. |  [optional] |
|**isOSDisk** | **String** | A value indicating whether the disk is the OS disk. |  [optional] [readonly] |
|**logStorageAccountId** | **String** | The log storage account ARM Id. |  [optional] [readonly] |
|**logStorageAccountSasSecretName** | **String** | The key vault secret name of the log storage account. |  [optional] [readonly] |
|**seedManagedDiskId** | **String** | The ARM Id of the seed managed disk. |  [optional] [readonly] |
|**targetManagedDiskId** | **String** | The ARM Id of the target managed disk. |  [optional] [readonly] |



## Enum: DiskTypeEnum

| Name | Value |
|---- | -----|
| STANDARD_LRS | &quot;Standard_LRS&quot; |
| PREMIUM_LRS | &quot;Premium_LRS&quot; |
| STANDARD_SSD_LRS | &quot;StandardSSD_LRS&quot; |



