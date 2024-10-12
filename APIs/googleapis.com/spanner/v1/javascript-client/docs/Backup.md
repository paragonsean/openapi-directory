# CloudSpannerApi.Backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time the CreateBackup request is received. If the request does not specify &#x60;version_time&#x60;, the &#x60;version_time&#x60; of the backup will be equivalent to the &#x60;create_time&#x60;. | [optional] [readonly] 
**database** | **String** | Required for the CreateBackup operation. Name of the database from which this backup was created. This needs to be in the same instance as the backup. Values are of the form &#x60;projects//instances//databases/&#x60;. | [optional] 
**databaseDialect** | **String** | Output only. The database dialect information for the backup. | [optional] [readonly] 
**encryptionInfo** | [**EncryptionInfo**](EncryptionInfo.md) |  | [optional] 
**expireTime** | **String** | Required for the CreateBackup operation. The expiration time of the backup, with microseconds granularity that must be at least 6 hours and at most 366 days from the time the CreateBackup request is processed. Once the &#x60;expire_time&#x60; has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup. | [optional] 
**maxExpireTime** | **String** | Output only. The max allowed expiration time of the backup, with microseconds granularity. A backup&#39;s expiration time can be configured in multiple APIs: CreateBackup, UpdateBackup, CopyBackup. When updating or copying an existing backup, the expiration time specified must be less than &#x60;Backup.max_expire_time&#x60;. | [optional] [readonly] 
**name** | **String** | Output only for the CreateBackup operation. Required for the UpdateBackup operation. A globally unique identifier for the backup which cannot be changed. Values are of the form &#x60;projects//instances//backups/a-z*[a-z0-9]&#x60; The final segment of the name must be between 2 and 60 characters in length. The backup is stored in the location(s) specified in the instance configuration of the instance containing the backup, identified by the prefix of the backup name of the form &#x60;projects//instances/&#x60;. | [optional] 
**referencingBackups** | **[String]** | Output only. The names of the destination backups being created by copying this source backup. The backup names are of the form &#x60;projects//instances//backups/&#x60;. Referencing backups may exist in different instances. The existence of any referencing backup prevents the backup from being deleted. When the copy operation is done (either successfully completed or cancelled or the destination backup is deleted), the reference to the backup is removed. | [optional] [readonly] 
**referencingDatabases** | **[String]** | Output only. The names of the restored databases that reference the backup. The database names are of the form &#x60;projects//instances//databases/&#x60;. Referencing databases may exist in different instances. The existence of any referencing database prevents the backup from being deleted. When a restored database from the backup enters the &#x60;READY&#x60; state, the reference to the backup is removed. | [optional] [readonly] 
**sizeBytes** | **String** | Output only. Size of the backup in bytes. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the backup. | [optional] [readonly] 
**versionTime** | **String** | The backup will contain an externally consistent copy of the database at the timestamp specified by &#x60;version_time&#x60;. If &#x60;version_time&#x60; is not specified, the system will set &#x60;version_time&#x60; to the &#x60;create_time&#x60; of the backup. | [optional] 



## Enum: DatabaseDialectEnum


* `DATABASE_DIALECT_UNSPECIFIED` (value: `"DATABASE_DIALECT_UNSPECIFIED"`)

* `GOOGLE_STANDARD_SQL` (value: `"GOOGLE_STANDARD_SQL"`)

* `POSTGRESQL` (value: `"POSTGRESQL"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)




