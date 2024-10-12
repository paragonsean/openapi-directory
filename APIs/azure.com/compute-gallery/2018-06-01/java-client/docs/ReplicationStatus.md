

# ReplicationStatus

This is the replication status of the gallery Image Version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregatedState** | [**AggregatedStateEnum**](#AggregatedStateEnum) | This is the aggregated replication status based on all the regional replication status flags. |  [optional] [readonly] |
|**summary** | [**List&lt;RegionalReplicationStatus&gt;**](RegionalReplicationStatus.md) | This is a summary of replication status for each region. |  [optional] [readonly] |



## Enum: AggregatedStateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |



