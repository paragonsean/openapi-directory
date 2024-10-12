

# CopyBackupRequest

The request for CopyBackup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupId** | **String** | Required. The id of the backup copy. The &#x60;backup_id&#x60; appended to &#x60;parent&#x60; forms the full backup_uri of the form &#x60;projects//instances//backups/&#x60;. |  [optional] |
|**encryptionConfig** | [**CopyBackupEncryptionConfig**](CopyBackupEncryptionConfig.md) |  |  [optional] |
|**expireTime** | **String** | Required. The expiration time of the backup in microsecond granularity. The expiration time must be at least 6 hours and at most 366 days from the &#x60;create_time&#x60; of the source backup. Once the &#x60;expire_time&#x60; has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup. |  [optional] |
|**sourceBackup** | **String** | Required. The source backup to be copied. The source backup needs to be in READY state for it to be copied. Once CopyBackup is in progress, the source backup cannot be deleted or cleaned up on expiration until CopyBackup is finished. Values are of the form: &#x60;projects//instances//backups/&#x60;. |  [optional] |



