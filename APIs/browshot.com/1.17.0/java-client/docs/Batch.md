

# Batch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | number of unique URLs in the batch |  [optional] |
|**failed** | **Integer** | number of screenshots failed |  [optional] |
|**finished** | **Integer** | time of batch completed (UNIX timestamp) |  [optional] |
|**id** | **Integer** | batch ID |  [optional] |
|**processed** | **Integer** | number of screenshots finishe |  [optional] |
|**started** | **Integer** | time of processing (UNIX timestamp) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | status of the request - \&quot;in_queue\&quot;, \&quot;processing\&quot;, \&quot;finished\&quot;, \&quot;error\&quot; |  [optional] |
|**urls** | **List&lt;String&gt;** | URLs to download the batch |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| IN_QUEUE | &quot;in_queue&quot; |
| PROCESSING | &quot;processing&quot; |
| FINISHED | &quot;finished&quot; |
| ERROR | &quot;error&quot; |



