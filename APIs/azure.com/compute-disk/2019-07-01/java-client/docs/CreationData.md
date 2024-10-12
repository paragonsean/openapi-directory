

# CreationData

Data used when creating a disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createOption** | [**CreateOptionEnum**](#CreateOptionEnum) | This enumerates the possible sources of a disk&#39;s creation. |  |
|**imageReference** | [**ImageDiskReference**](ImageDiskReference.md) |  |  [optional] |
|**sourceResourceId** | **String** | If createOption is Copy, this is the ARM id of the source snapshot or disk. |  [optional] |
|**sourceUniqueId** | **String** | If this field is set, this is the unique id identifying the source of this resource. |  [optional] [readonly] |
|**sourceUri** | **String** | If createOption is Import, this is the URI of a blob to be imported into a managed disk. |  [optional] |
|**storageAccountId** | **String** | Required if createOption is Import. The Azure Resource Manager identifier of the storage account containing the blob to import as a disk. |  [optional] |
|**uploadSizeBytes** | **Long** | If createOption is Upload, this is the size of the contents of the upload including the VHD footer. This value should be between 20972032 (20 MiB + 512 bytes for the VHD footer) and 35183298347520 bytes (32 TiB + 512 bytes for the VHD footer). |  [optional] |



## Enum: CreateOptionEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;Empty&quot; |
| ATTACH | &quot;Attach&quot; |
| FROM_IMAGE | &quot;FromImage&quot; |
| IMPORT | &quot;Import&quot; |
| COPY | &quot;Copy&quot; |
| RESTORE | &quot;Restore&quot; |
| UPLOAD | &quot;Upload&quot; |



