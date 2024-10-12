

# VMwareCbtDiskInput

VMwareCbt disk input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskId** | **String** | The disk Id. |  |
|**diskType** | [**DiskTypeEnum**](#DiskTypeEnum) | The disk type. |  [optional] |
|**isOSDisk** | **String** | A value indicating whether the disk is the OS disk. |  |
|**logStorageAccountId** | **String** | The log storage account ARM Id. |  |
|**logStorageAccountSasSecretName** | **String** | The key vault secret name of the log storage account. |  |



## Enum: DiskTypeEnum

| Name | Value |
|---- | -----|
| STANDARD_LRS | &quot;Standard_LRS&quot; |
| PREMIUM_LRS | &quot;Premium_LRS&quot; |
| STANDARD_SSD_LRS | &quot;StandardSSD_LRS&quot; |



