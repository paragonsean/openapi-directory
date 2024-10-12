

# BackupProperties

The properties of the backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupJobCreationType** | [**BackupJobCreationTypeEnum**](#BackupJobCreationTypeEnum) | The backup job creation type. |  [optional] |
|**backupPolicyId** | **String** | The path ID of the backup policy. |  [optional] |
|**backupType** | [**BackupTypeEnum**](#BackupTypeEnum) | The type of the backup. |  [optional] |
|**createdOn** | **OffsetDateTime** | The time when the backup was created. |  |
|**elements** | [**List&lt;BackupElement&gt;**](BackupElement.md) | The backup elements. |  |
|**sizeInBytes** | **Long** | The backup size in bytes. |  |
|**ssmHostName** | **String** | The StorSimple Snapshot Manager host name. |  [optional] |



## Enum: BackupJobCreationTypeEnum

| Name | Value |
|---- | -----|
| ADHOC | &quot;Adhoc&quot; |
| BY_SCHEDULE | &quot;BySchedule&quot; |
| BY_SSM | &quot;BySSM&quot; |



## Enum: BackupTypeEnum

| Name | Value |
|---- | -----|
| LOCAL_SNAPSHOT | &quot;LocalSnapshot&quot; |
| CLOUD_SNAPSHOT | &quot;CloudSnapshot&quot; |



