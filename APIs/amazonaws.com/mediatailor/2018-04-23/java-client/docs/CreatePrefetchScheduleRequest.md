

# CreatePrefetchScheduleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumption** | [**CreatePrefetchScheduleRequestConsumption**](CreatePrefetchScheduleRequestConsumption.md) |  |  |
|**retrieval** | [**CreatePrefetchScheduleRequestRetrieval**](CreatePrefetchScheduleRequestRetrieval.md) |  |  |
|**streamId** | **String** | An optional stream identifier that MediaTailor uses to prefetch ads for multiple streams that use the same playback configuration. If &lt;code&gt;StreamId&lt;/code&gt; is specified, MediaTailor returns all of the prefetch schedules with an exact match on &lt;code&gt;StreamId&lt;/code&gt;. If not specified, MediaTailor returns all of the prefetch schedules for the playback configuration, regardless of &lt;code&gt;StreamId&lt;/code&gt;. |  [optional] |



