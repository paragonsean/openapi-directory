

# MetadataOptions

Specifies the metadata options for running a transfer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acl** | [**AclEnum**](#AclEnum) | Specifies how each object&#39;s ACLs should be preserved for transfers between Google Cloud Storage buckets. If unspecified, the default behavior is the same as ACL_DESTINATION_BUCKET_DEFAULT. |  [optional] |
|**gid** | [**GidEnum**](#GidEnum) | Specifies how each file&#39;s POSIX group ID (GID) attribute should be handled by the transfer. By default, GID is not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers. |  [optional] |
|**kmsKey** | [**KmsKeyEnum**](#KmsKeyEnum) | Specifies how each object&#39;s Cloud KMS customer-managed encryption key (CMEK) is preserved for transfers between Google Cloud Storage buckets. If unspecified, the default behavior is the same as KMS_KEY_DESTINATION_BUCKET_DEFAULT. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Specifies how each file&#39;s mode attribute should be handled by the transfer. By default, mode is not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers. |  [optional] |
|**storageClass** | [**StorageClassEnum**](#StorageClassEnum) | Specifies the storage class to set on objects being transferred to Google Cloud Storage buckets. If unspecified, the default behavior is the same as STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT. |  [optional] |
|**symlink** | [**SymlinkEnum**](#SymlinkEnum) | Specifies how symlinks should be handled by the transfer. By default, symlinks are not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers. |  [optional] |
|**temporaryHold** | [**TemporaryHoldEnum**](#TemporaryHoldEnum) | Specifies how each object&#39;s temporary hold status should be preserved for transfers between Google Cloud Storage buckets. If unspecified, the default behavior is the same as TEMPORARY_HOLD_PRESERVE. |  [optional] |
|**timeCreated** | [**TimeCreatedEnum**](#TimeCreatedEnum) | Specifies how each object&#39;s &#x60;timeCreated&#x60; metadata is preserved for transfers. If unspecified, the default behavior is the same as TIME_CREATED_SKIP. |  [optional] |
|**uid** | [**UidEnum**](#UidEnum) | Specifies how each file&#39;s POSIX user ID (UID) attribute should be handled by the transfer. By default, UID is not preserved. Only applicable to transfers involving POSIX file systems, and ignored for other transfers. |  [optional] |



## Enum: AclEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ACL_UNSPECIFIED&quot; |
| DESTINATION_BUCKET_DEFAULT | &quot;ACL_DESTINATION_BUCKET_DEFAULT&quot; |
| PRESERVE | &quot;ACL_PRESERVE&quot; |



## Enum: GidEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;GID_UNSPECIFIED&quot; |
| SKIP | &quot;GID_SKIP&quot; |
| NUMBER | &quot;GID_NUMBER&quot; |



## Enum: KmsKeyEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;KMS_KEY_UNSPECIFIED&quot; |
| DESTINATION_BUCKET_DEFAULT | &quot;KMS_KEY_DESTINATION_BUCKET_DEFAULT&quot; |
| PRESERVE | &quot;KMS_KEY_PRESERVE&quot; |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MODE_UNSPECIFIED&quot; |
| SKIP | &quot;MODE_SKIP&quot; |
| PRESERVE | &quot;MODE_PRESERVE&quot; |



## Enum: StorageClassEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;STORAGE_CLASS_UNSPECIFIED&quot; |
| DESTINATION_BUCKET_DEFAULT | &quot;STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT&quot; |
| PRESERVE | &quot;STORAGE_CLASS_PRESERVE&quot; |
| STANDARD | &quot;STORAGE_CLASS_STANDARD&quot; |
| NEARLINE | &quot;STORAGE_CLASS_NEARLINE&quot; |
| COLDLINE | &quot;STORAGE_CLASS_COLDLINE&quot; |
| ARCHIVE | &quot;STORAGE_CLASS_ARCHIVE&quot; |



## Enum: SymlinkEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SYMLINK_UNSPECIFIED&quot; |
| SKIP | &quot;SYMLINK_SKIP&quot; |
| PRESERVE | &quot;SYMLINK_PRESERVE&quot; |



## Enum: TemporaryHoldEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TEMPORARY_HOLD_UNSPECIFIED&quot; |
| SKIP | &quot;TEMPORARY_HOLD_SKIP&quot; |
| PRESERVE | &quot;TEMPORARY_HOLD_PRESERVE&quot; |



## Enum: TimeCreatedEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TIME_CREATED_UNSPECIFIED&quot; |
| SKIP | &quot;TIME_CREATED_SKIP&quot; |
| PRESERVE_AS_CUSTOM_TIME | &quot;TIME_CREATED_PRESERVE_AS_CUSTOM_TIME&quot; |



## Enum: UidEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UID_UNSPECIFIED&quot; |
| SKIP | &quot;UID_SKIP&quot; |
| NUMBER | &quot;UID_NUMBER&quot; |



