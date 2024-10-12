# CloudSqlAdminApi.BackupRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupKind** | **String** | Specifies the kind of backup, PHYSICAL or DEFAULT_SNAPSHOT. | [optional] 
**description** | **String** | The description of this run, only applicable to on-demand backups. | [optional] 
**diskEncryptionConfiguration** | [**DiskEncryptionConfiguration**](DiskEncryptionConfiguration.md) |  | [optional] 
**diskEncryptionStatus** | [**DiskEncryptionStatus**](DiskEncryptionStatus.md) |  | [optional] 
**endTime** | **String** | The time the backup operation completed in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. | [optional] 
**enqueuedTime** | **String** | The time the run was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. | [optional] 
**error** | [**OperationError**](OperationError.md) |  | [optional] 
**id** | **String** | The identifier for this backup run. Unique only for a specific Cloud SQL instance. | [optional] 
**instance** | **String** | Name of the database instance. | [optional] 
**kind** | **String** | This is always &#x60;sql#backupRun&#x60;. | [optional] 
**location** | **String** | Location of the backups. | [optional] 
**selfLink** | **String** | The URI of this resource. | [optional] 
**startTime** | **String** | The time the backup operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. | [optional] 
**status** | **String** | The status of this run. | [optional] 
**timeZone** | **String** | Backup time zone to prevent restores to an instance with a different time zone. Now relevant only for SQL Server. | [optional] 
**type** | **String** | The type of this run; can be either \&quot;AUTOMATED\&quot; or \&quot;ON_DEMAND\&quot; or \&quot;FINAL\&quot;. This field defaults to \&quot;ON_DEMAND\&quot; and is ignored, when specified for insert requests. | [optional] 
**windowStartTime** | **String** | The start time of the backup window during which this the backup was attempted in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. | [optional] 



## Enum: BackupKindEnum


* `SQL_BACKUP_KIND_UNSPECIFIED` (value: `"SQL_BACKUP_KIND_UNSPECIFIED"`)

* `SNAPSHOT` (value: `"SNAPSHOT"`)

* `PHYSICAL` (value: `"PHYSICAL"`)





## Enum: StatusEnum


* `SQL_BACKUP_RUN_STATUS_UNSPECIFIED` (value: `"SQL_BACKUP_RUN_STATUS_UNSPECIFIED"`)

* `ENQUEUED` (value: `"ENQUEUED"`)

* `OVERDUE` (value: `"OVERDUE"`)

* `RUNNING` (value: `"RUNNING"`)

* `FAILED` (value: `"FAILED"`)

* `SUCCESSFUL` (value: `"SUCCESSFUL"`)

* `SKIPPED` (value: `"SKIPPED"`)

* `DELETION_PENDING` (value: `"DELETION_PENDING"`)

* `DELETION_FAILED` (value: `"DELETION_FAILED"`)

* `DELETED` (value: `"DELETED"`)





## Enum: TypeEnum


* `SQL_BACKUP_RUN_TYPE_UNSPECIFIED` (value: `"SQL_BACKUP_RUN_TYPE_UNSPECIFIED"`)

* `AUTOMATED` (value: `"AUTOMATED"`)

* `ON_DEMAND` (value: `"ON_DEMAND"`)




