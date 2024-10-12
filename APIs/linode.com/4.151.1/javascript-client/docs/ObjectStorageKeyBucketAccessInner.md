# LinodeApi.ObjectStorageKeyBucketAccessInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketName** | **String** | The unique label of the bucket to which the key will grant limited access. | [optional] 
**cluster** | **String** | The Object Storage cluster where a bucket to which the key is granting access is hosted. | [optional] 
**permissions** | **String** | This Limited Access Key&#39;s permissions for the selected bucket. | [optional] 



## Enum: PermissionsEnum


* `write` (value: `"read_write"`)

* `only` (value: `"read_only"`)




