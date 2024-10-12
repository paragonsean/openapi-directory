

# RestorePointProperties

Represents the properties of a database restore point.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**earliestRestoreDate** | **OffsetDateTime** | Earliest restore time (ISO8601 format). Populated when restorePointType &#x3D; DISCRETE. Null otherwise. |  [optional] [readonly] |
|**restorePointCreationDate** | **OffsetDateTime** | Restore point creation time (ISO8601 format). Populated when restorePointType &#x3D; CONTINUOUS. Null otherwise. |  [optional] [readonly] |
|**restorePointType** | [**RestorePointTypeEnum**](#RestorePointTypeEnum) | The restore point type of the database restore point. |  [optional] [readonly] |



## Enum: RestorePointTypeEnum

| Name | Value |
|---- | -----|
| DISCRETE | &quot;DISCRETE&quot; |
| CONTINUOUS | &quot;CONTINUOUS&quot; |



