

# ClusterResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusters** | [**List&lt;Cluster&gt;**](Cluster.md) |  |  [optional] |
|**copyrights** | **List&lt;String&gt;** |  |  [optional] |
|**processingTime** | **Double** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Indicates the current status of the job |  [optional] |
|**waitingTimeInQueue** | **Double** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| WAITING_IN_QUEUE | &quot;waiting_in_queue&quot; |
| PROCESSING | &quot;processing&quot; |
| FINISHED | &quot;finished&quot; |



