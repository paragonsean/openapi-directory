# AwsXRay.GetTraceSummariesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startTime** | **Date** | The start of the time frame for which to retrieve traces. | 
**endTime** | **Date** | The end of the time frame for which to retrieve traces. | 
**timeRangeType** | **String** | A parameter to indicate whether to query trace summaries by TraceId or Event time. | [optional] 
**sampling** | **Boolean** | Set to &lt;code&gt;true&lt;/code&gt; to get summaries for only a subset of available traces. | [optional] 
**samplingStrategy** | [**GetTraceSummariesRequestSamplingStrategy**](GetTraceSummariesRequestSamplingStrategy.md) |  | [optional] 
**filterExpression** | **String** | Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements. | [optional] 
**nextToken** | **String** | Specify the pagination token returned by a previous request to retrieve the next page of results. | [optional] 



## Enum: TimeRangeTypeEnum


* `TraceId` (value: `"TraceId"`)

* `Event` (value: `"Event"`)




