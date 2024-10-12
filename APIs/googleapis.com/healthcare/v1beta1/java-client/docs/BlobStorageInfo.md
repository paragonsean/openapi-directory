

# BlobStorageInfo

BlobStorageInfo contains details about the data stored in Blob Storage for the referenced resource. Note: Storage class is only valid for DICOM and hence will only be populated for DICOM resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sizeBytes** | **String** | Size in bytes of data stored in Blob Storage. |  [optional] |
|**storageClass** | [**StorageClassEnum**](#StorageClassEnum) | The storage class in which the Blob data is stored. |  [optional] |
|**storageClassUpdateTime** | **String** | The time at which the storage class was updated. This is used to compute early deletion fees of the resource. |  [optional] |



## Enum: StorageClassEnum

| Name | Value |
|---- | -----|
| BLOB_STORAGE_CLASS_UNSPECIFIED | &quot;BLOB_STORAGE_CLASS_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| NEARLINE | &quot;NEARLINE&quot; |
| COLDLINE | &quot;COLDLINE&quot; |
| ARCHIVE | &quot;ARCHIVE&quot; |



