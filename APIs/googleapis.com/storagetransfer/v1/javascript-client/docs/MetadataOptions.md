# StorageTransferApi.MetadataOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **String** | Specifies how each object&#39;s ACLs should be preserved for transfers between Google Cloud Storage buckets. If unspecified, the default behavior is the same as ACL_DESTINATION_BUCKET_DEFAULT. | [optional] 
**gid** | **String** | Specifies how each file&#39;s POSIX group ID (GID) attribute should be handled by the transfer. By default, GID is not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers. | [optional] 
**kmsKey** | **String** | Specifies how each object&#39;s Cloud KMS customer-managed encryption key (CMEK) is preserved for transfers between Google Cloud Storage buckets. If unspecified, the default behavior is the same as KMS_KEY_DESTINATION_BUCKET_DEFAULT. | [optional] 
**mode** | **String** | Specifies how each file&#39;s mode attribute should be handled by the transfer. By default, mode is not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers. | [optional] 
**storageClass** | **String** | Specifies the storage class to set on objects being transferred to Google Cloud Storage buckets. If unspecified, the default behavior is the same as STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT. | [optional] 
**symlink** | **String** | Specifies how symlinks should be handled by the transfer. By default, symlinks are not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers. | [optional] 
**temporaryHold** | **String** | Specifies how each object&#39;s temporary hold status should be preserved for transfers between Google Cloud Storage buckets. If unspecified, the default behavior is the same as TEMPORARY_HOLD_PRESERVE. | [optional] 
**timeCreated** | **String** | Specifies how each object&#39;s &#x60;timeCreated&#x60; metadata is preserved for transfers. If unspecified, the default behavior is the same as TIME_CREATED_SKIP. | [optional] 
**uid** | **String** | Specifies how each file&#39;s POSIX user ID (UID) attribute should be handled by the transfer. By default, UID is not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers. | [optional] 



## Enum: AclEnum


* `UNSPECIFIED` (value: `"ACL_UNSPECIFIED"`)

* `DESTINATION_BUCKET_DEFAULT` (value: `"ACL_DESTINATION_BUCKET_DEFAULT"`)

* `PRESERVE` (value: `"ACL_PRESERVE"`)





## Enum: GidEnum


* `UNSPECIFIED` (value: `"GID_UNSPECIFIED"`)

* `SKIP` (value: `"GID_SKIP"`)

* `NUMBER` (value: `"GID_NUMBER"`)





## Enum: KmsKeyEnum


* `UNSPECIFIED` (value: `"KMS_KEY_UNSPECIFIED"`)

* `DESTINATION_BUCKET_DEFAULT` (value: `"KMS_KEY_DESTINATION_BUCKET_DEFAULT"`)

* `PRESERVE` (value: `"KMS_KEY_PRESERVE"`)





## Enum: ModeEnum


* `UNSPECIFIED` (value: `"MODE_UNSPECIFIED"`)

* `SKIP` (value: `"MODE_SKIP"`)

* `PRESERVE` (value: `"MODE_PRESERVE"`)





## Enum: StorageClassEnum


* `UNSPECIFIED` (value: `"STORAGE_CLASS_UNSPECIFIED"`)

* `DESTINATION_BUCKET_DEFAULT` (value: `"STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT"`)

* `PRESERVE` (value: `"STORAGE_CLASS_PRESERVE"`)

* `STANDARD` (value: `"STORAGE_CLASS_STANDARD"`)

* `NEARLINE` (value: `"STORAGE_CLASS_NEARLINE"`)

* `COLDLINE` (value: `"STORAGE_CLASS_COLDLINE"`)

* `ARCHIVE` (value: `"STORAGE_CLASS_ARCHIVE"`)





## Enum: SymlinkEnum


* `UNSPECIFIED` (value: `"SYMLINK_UNSPECIFIED"`)

* `SKIP` (value: `"SYMLINK_SKIP"`)

* `PRESERVE` (value: `"SYMLINK_PRESERVE"`)





## Enum: TemporaryHoldEnum


* `UNSPECIFIED` (value: `"TEMPORARY_HOLD_UNSPECIFIED"`)

* `SKIP` (value: `"TEMPORARY_HOLD_SKIP"`)

* `PRESERVE` (value: `"TEMPORARY_HOLD_PRESERVE"`)





## Enum: TimeCreatedEnum


* `UNSPECIFIED` (value: `"TIME_CREATED_UNSPECIFIED"`)

* `SKIP` (value: `"TIME_CREATED_SKIP"`)

* `PRESERVE_AS_CUSTOM_TIME` (value: `"TIME_CREATED_PRESERVE_AS_CUSTOM_TIME"`)





## Enum: UidEnum


* `UNSPECIFIED` (value: `"UID_UNSPECIFIED"`)

* `SKIP` (value: `"UID_SKIP"`)

* `NUMBER` (value: `"UID_NUMBER"`)




