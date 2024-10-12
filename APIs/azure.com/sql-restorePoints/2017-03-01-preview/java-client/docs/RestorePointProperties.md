

# RestorePointProperties

Properties of a database restore point

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**earliestRestoreDate** | **OffsetDateTime** | The earliest time to which this database can be restored |  [optional] [readonly] |
|**restorePointCreationDate** | **OffsetDateTime** | The time the backup was taken |  [optional] [readonly] |
|**restorePointLabel** | **String** | The label of restore point for backup request by user |  [optional] [readonly] |
|**restorePointType** | [**RestorePointTypeEnum**](#RestorePointTypeEnum) | The type of restore point |  [optional] [readonly] |



## Enum: RestorePointTypeEnum

| Name | Value |
|---- | -----|
| CONTINUOUS | &quot;CONTINUOUS&quot; |
| DISCRETE | &quot;DISCRETE&quot; |



