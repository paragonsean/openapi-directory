

# AggregateBucket


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activity** | **Integer** | Available for Bucket.Type.ACTIVITY_TYPE, Bucket.Type.ACTIVITY_SEGMENT |  [optional] |
|**dataset** | [**List&lt;Dataset&gt;**](Dataset.md) | There will be one dataset per AggregateBy in the request. |  [optional] |
|**endTimeMillis** | **String** | The end time for the aggregated data, in milliseconds since epoch, inclusive. |  [optional] |
|**session** | [**Session**](Session.md) |  |  [optional] |
|**startTimeMillis** | **String** | The start time for the aggregated data, in milliseconds since epoch, inclusive. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of a bucket signifies how the data aggregation is performed in the bucket. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| TIME | &quot;time&quot; |
| SESSION | &quot;session&quot; |
| ACTIVITY_TYPE | &quot;activityType&quot; |
| ACTIVITY_SEGMENT | &quot;activitySegment&quot; |



