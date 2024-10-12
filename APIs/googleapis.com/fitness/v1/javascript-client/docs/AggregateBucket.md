# FitnessApi.AggregateBucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | **Number** | Available for Bucket.Type.ACTIVITY_TYPE, Bucket.Type.ACTIVITY_SEGMENT | [optional] 
**dataset** | [**[Dataset]**](Dataset.md) | There will be one dataset per AggregateBy in the request. | [optional] 
**endTimeMillis** | **String** | The end time for the aggregated data, in milliseconds since epoch, inclusive. | [optional] 
**session** | [**Session**](Session.md) |  | [optional] 
**startTimeMillis** | **String** | The start time for the aggregated data, in milliseconds since epoch, inclusive. | [optional] 
**type** | **String** | The type of a bucket signifies how the data aggregation is performed in the bucket. | [optional] 



## Enum: TypeEnum


* `unknown` (value: `"unknown"`)

* `time` (value: `"time"`)

* `session` (value: `"session"`)

* `activityType` (value: `"activityType"`)

* `activitySegment` (value: `"activitySegment"`)




