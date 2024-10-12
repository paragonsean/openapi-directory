

# CreationData

Data used when creating a disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createOption** | [**CreateOptionEnum**](#CreateOptionEnum) | This enumerates the possible sources of a disk&#39;s creation. |  |
|**imageReference** | [**ImageDiskReference**](ImageDiskReference.md) |  |  [optional] |
|**sourceResourceId** | **String** | If createOption is Copy, this is the ARM id of the source snapshot or disk. |  [optional] |
|**sourceUri** | **String** | If createOption is Import, this is the URI of a blob to be imported into a managed disk. |  [optional] |
|**storageAccountId** | **String** | If createOption is Import, the Azure Resource Manager identifier of the storage account containing the blob to import as a disk. Required only if the blob is in a different subscription |  [optional] |



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



