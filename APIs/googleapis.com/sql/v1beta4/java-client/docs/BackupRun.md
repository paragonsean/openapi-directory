

# BackupRun

A BackupRun resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupKind** | [**BackupKindEnum**](#BackupKindEnum) | Specifies the kind of backup, PHYSICAL or DEFAULT_SNAPSHOT. |  [optional] |
|**description** | **String** | The description of this run, only applicable to on-demand backups. |  [optional] |
|**diskEncryptionConfiguration** | [**DiskEncryptionConfiguration**](DiskEncryptionConfiguration.md) |  |  [optional] |
|**diskEncryptionStatus** | [**DiskEncryptionStatus**](DiskEncryptionStatus.md) |  |  [optional] |
|**endTime** | **String** | The time the backup operation completed in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. |  [optional] |
|**enqueuedTime** | **String** | The time the run was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. |  [optional] |
|**error** | [**OperationError**](OperationError.md) |  |  [optional] |
|**id** | **String** | The identifier for this backup run. Unique only for a specific Cloud SQL instance. |  [optional] |
|**instance** | **String** | Name of the database instance. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#backupRun&#x60;. |  [optional] |
|**location** | **String** | Location of the backups. |  [optional] |
|**selfLink** | **String** | The URI of this resource. |  [optional] |
|**startTime** | **String** | The time the backup operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of this run. |  [optional] |
|**timeZone** | **String** | Backup time zone to prevent restores to an instance with a different time zone. Now relevant only for SQL Server. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this run; can be either \&quot;AUTOMATED\&quot; or \&quot;ON_DEMAND\&quot; or \&quot;FINAL\&quot;. This field defaults to \&quot;ON_DEMAND\&quot; and is ignored, when specified for insert requests. |  [optional] |
|**windowStartTime** | **String** | The start time of the backup window during which this the backup was attempted in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. |  [optional] |



## Enum: BackupKindEnum

| Name | Value |
|---- | -----|
| SQL_BACKUP_KIND_UNSPECIFIED | &quot;SQL_BACKUP_KIND_UNSPECIFIED&quot; |
| SNAPSHOT | &quot;SNAPSHOT&quot; |
| PHYSICAL | &quot;PHYSICAL&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SQL_BACKUP_RUN_STATUS_UNSPECIFIED | &quot;SQL_BACKUP_RUN_STATUS_UNSPECIFIED&quot; |
| ENQUEUED | &quot;ENQUEUED&quot; |
| OVERDUE | &quot;OVERDUE&quot; |
| RUNNING | &quot;RUNNING&quot; |
| FAILED | &quot;FAILED&quot; |
| SUCCESSFUL | &quot;SUCCESSFUL&quot; |
| SKIPPED | &quot;SKIPPED&quot; |
| DELETION_PENDING | &quot;DELETION_PENDING&quot; |
| DELETION_FAILED | &quot;DELETION_FAILED&quot; |
| DELETED | &quot;DELETED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SQL_BACKUP_RUN_TYPE_UNSPECIFIED | &quot;SQL_BACKUP_RUN_TYPE_UNSPECIFIED&quot; |
| AUTOMATED | &quot;AUTOMATED&quot; |
| ON_DEMAND | &quot;ON_DEMAND&quot; |



