

# CreateTimeSeriesSummary

Summary of the result of a failed request to write data to a time series.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | The number of points that failed to be written. Order is not guaranteed. |  [optional] |
|**successPointCount** | **Integer** | The number of points that were successfully written. |  [optional] |
|**totalPointCount** | **Integer** | The number of points in the request. |  [optional] |



