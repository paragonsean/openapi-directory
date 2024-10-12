

# Backup

An object representing a Backup or snapshot for a Linode with Backup service enabled. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**available** | **Boolean** | Whether this Backup is available for restoration.  Backups undergoing maintenance are not available for restoration.  |  [optional] [readonly] |
|**configs** | **List&lt;String&gt;** | A list of the labels of the Configuration profiles that are part of the Backup.  |  [optional] [readonly] |
|**created** | **OffsetDateTime** | The date the Backup was taken. |  [optional] [readonly] |
|**disks** | [**List&lt;BackupDisksInner&gt;**](BackupDisksInner.md) | A list of the disks that are part of the Backup.  |  [optional] [readonly] |
|**finished** | **OffsetDateTime** | The date the Backup completed. |  [optional] [readonly] |
|**id** | **Integer** | The unique ID of this Backup. |  [optional] [readonly] |
|**label** | **String** | A label for Backups that are of type &#x60;snapshot&#x60;. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current state of a specific Backup. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | This indicates whether the Backup is an automatic Backup or manual snapshot taken by the User at a specific point in time.  |  [optional] [readonly] |
|**updated** | **OffsetDateTime** | The date the Backup was most recently updated. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PAUSED | &quot;paused&quot; |
| PENDING | &quot;pending&quot; |
| RUNNING | &quot;running&quot; |
| NEEDS_POST_PROCESSING | &quot;needsPostProcessing&quot; |
| SUCCESSFUL | &quot;successful&quot; |
| FAILED | &quot;failed&quot; |
| USER_ABORTED | &quot;userAborted&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| SNAPSHOT | &quot;snapshot&quot; |



