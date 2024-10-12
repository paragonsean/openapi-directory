# CloudHealthcareApi.BlobStorageInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sizeBytes** | **String** | Size in bytes of data stored in Blob Storage. | [optional] 
**storageClass** | **String** | The storage class in which the Blob data is stored. | [optional] 
**storageClassUpdateTime** | **String** | The time at which the storage class was updated. This is used to compute early deletion fees of the resource. | [optional] 



## Enum: StorageClassEnum


* `BLOB_STORAGE_CLASS_UNSPECIFIED` (value: `"BLOB_STORAGE_CLASS_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `NEARLINE` (value: `"NEARLINE"`)

* `COLDLINE` (value: `"COLDLINE"`)

* `ARCHIVE` (value: `"ARCHIVE"`)




