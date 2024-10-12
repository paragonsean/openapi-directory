

# LabProperties

Properties of a lab.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactsStorageAccount** | **String** | The artifact storage account of the lab. |  [optional] |
|**createdDate** | **OffsetDateTime** | The creation date of the lab. |  [optional] |
|**defaultStorageAccount** | **String** | The lab&#39;s default storage account. |  [optional] |
|**defaultVirtualNetworkId** | **String** | The default virtual network identifier of the lab. |  [optional] |
|**labStorageType** | [**LabStorageTypeEnum**](#LabStorageTypeEnum) | The type of the lab storage. |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**storageAccounts** | **List&lt;String&gt;** | The storage accounts of the lab. |  [optional] |
|**vaultName** | **String** | The name of the key vault of the lab. |  [optional] |



## Enum: LabStorageTypeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |



