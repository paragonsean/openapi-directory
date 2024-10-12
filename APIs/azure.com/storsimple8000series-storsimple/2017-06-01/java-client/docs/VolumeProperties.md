

# VolumeProperties

The properties of volume.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessControlRecordIds** | **List&lt;String&gt;** | The IDs of the access control records, associated with the volume. |  |
|**backupPolicyIds** | **List&lt;String&gt;** | The IDs of the backup policies, in which this volume is part of. |  [optional] [readonly] |
|**backupStatus** | [**BackupStatusEnum**](#BackupStatusEnum) | The backup status of the volume. |  [optional] [readonly] |
|**monitoringStatus** | [**MonitoringStatusEnum**](#MonitoringStatusEnum) | The monitoring status of the volume. |  |
|**operationStatus** | [**OperationStatusEnum**](#OperationStatusEnum) | The operation status on the volume. |  [optional] [readonly] |
|**sizeInBytes** | **Long** | The size of the volume in bytes. |  |
|**volumeContainerId** | **String** | The ID of the volume container, in which this volume is created. |  [optional] [readonly] |
|**volumeStatus** | [**VolumeStatusEnum**](#VolumeStatusEnum) | The volume status. |  |
|**volumeType** | [**VolumeTypeEnum**](#VolumeTypeEnum) | The type of the volume. |  |



## Enum: BackupStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: MonitoringStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: OperationStatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| RESTORING | &quot;Restoring&quot; |



## Enum: VolumeStatusEnum

| Name | Value |
|---- | -----|
| ONLINE | &quot;Online&quot; |
| OFFLINE | &quot;Offline&quot; |



## Enum: VolumeTypeEnum

| Name | Value |
|---- | -----|
| TIERED | &quot;Tiered&quot; |
| ARCHIVAL | &quot;Archival&quot; |
| LOCALLY_PINNED | &quot;LocallyPinned&quot; |



