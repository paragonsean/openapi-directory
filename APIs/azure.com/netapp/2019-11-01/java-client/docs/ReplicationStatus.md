

# ReplicationStatus

Replication status

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | Displays error message if the replication is in an error state |  [optional] |
|**healthy** | **Boolean** | Replication health check |  [optional] |
|**mirrorState** | [**MirrorStateEnum**](#MirrorStateEnum) | The status of the replication |  [optional] |
|**relationshipStatus** | [**RelationshipStatusEnum**](#RelationshipStatusEnum) | Status of the mirror relationship |  [optional] |
|**totalProgress** | **String** | The progress of the replication |  [optional] |



## Enum: MirrorStateEnum

| Name | Value |
|---- | -----|
| UNINITIALIZED | &quot;Uninitialized&quot; |
| MIRRORED | &quot;Mirrored&quot; |
| BROKEN | &quot;Broken&quot; |



## Enum: RelationshipStatusEnum

| Name | Value |
|---- | -----|
| IDLE | &quot;Idle&quot; |
| TRANSFERRING | &quot;Transferring&quot; |



