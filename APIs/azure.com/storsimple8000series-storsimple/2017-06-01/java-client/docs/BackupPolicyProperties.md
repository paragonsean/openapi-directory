

# BackupPolicyProperties

The properties of the backup policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupPolicyCreationType** | [**BackupPolicyCreationTypeEnum**](#BackupPolicyCreationTypeEnum) | The backup policy creation type. Indicates whether this was created through SaaS or through StorSimple Snapshot Manager. |  [optional] [readonly] |
|**lastBackupTime** | **OffsetDateTime** | The time of the last backup for the backup policy. |  [optional] [readonly] |
|**nextBackupTime** | **OffsetDateTime** | The time of the next backup for the backup policy. |  [optional] [readonly] |
|**scheduledBackupStatus** | [**ScheduledBackupStatusEnum**](#ScheduledBackupStatusEnum) | Indicates whether at least one of the schedules in the backup policy is active or not. |  [optional] [readonly] |
|**schedulesCount** | **Long** | The count of schedules the backup policy contains. |  [optional] [readonly] |
|**ssmHostName** | **String** | If the backup policy was created by StorSimple Snapshot Manager, then this field indicates the hostname of the StorSimple Snapshot Manager. |  [optional] [readonly] |
|**volumeIds** | **List&lt;String&gt;** | The path IDs of the volumes which are part of the backup policy. |  |



## Enum: BackupPolicyCreationTypeEnum

| Name | Value |
|---- | -----|
| BY_SAA_S | &quot;BySaaS&quot; |
| BY_SSM | &quot;BySSM&quot; |



## Enum: ScheduledBackupStatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



