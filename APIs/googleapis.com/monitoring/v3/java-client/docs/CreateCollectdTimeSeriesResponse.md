

# CreateCollectdTimeSeriesResponse

The CreateCollectdTimeSeries response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**payloadErrors** | [**List&lt;CollectdPayloadError&gt;**](CollectdPayloadError.md) | Records the error status for points that were not written due to an error in the request.Failed requests for which nothing is written will return an error response instead. Requests where data points were rejected by the backend will set summary instead. |  [optional] |
|**summary** | [**CreateTimeSeriesSummary**](CreateTimeSeriesSummary.md) |  |  [optional] |



