

# DatabaseBackupSnapshot

Managed Database request object for snapshot backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**label** | **String** | The label for the Database snapshot backup.  * Must include only ASCII letters or numbers. * Must be unique among other backup labels for this Database.  |  |
|**target** | [**TargetEnum**](#TargetEnum) | The Database cluster target. If the Database is a high availability cluster, choosing &#x60;secondary&#x60; creates a snapshot backup of a replica node.  |  [optional] |



## Enum: TargetEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;primary&quot; |
| SECONDARY | &quot;secondary&quot; |



