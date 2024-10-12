

# RegionalReplicationStatus

This is the regional replication status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **String** | The details of the replication status. |  [optional] [readonly] |
|**progress** | **Integer** | It indicates progress of the replication job. |  [optional] [readonly] |
|**region** | **String** | The region to which the gallery Image Version is being replicated to. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | This is the regional replication state. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| REPLICATING | &quot;Replicating&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |



