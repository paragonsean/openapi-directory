

# EventRecordRequest

An event period update resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentTimeMillis** | **String** | The current time when this update was sent, in milliseconds, since 1970 UTC (Unix Epoch). |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#eventRecordRequest&#x60;. |  [optional] |
|**requestId** | **String** | The request ID used to identify this attempt to record events. |  [optional] |
|**timePeriods** | [**List&lt;EventPeriodUpdate&gt;**](EventPeriodUpdate.md) | A list of the time period updates being made in this request. |  [optional] |



