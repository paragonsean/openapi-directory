

# QueryTimeSeriesResponse

The QueryTimeSeries response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method. |  [optional] |
|**partialErrors** | [**List&lt;Status&gt;**](Status.md) | Query execution errors that may have caused the time series data returned to be incomplete. The available data will be available in the response. |  [optional] |
|**timeSeriesData** | [**List&lt;TimeSeriesData&gt;**](TimeSeriesData.md) | The time series data. |  [optional] |
|**timeSeriesDescriptor** | [**TimeSeriesDescriptor**](TimeSeriesDescriptor.md) |  |  [optional] |



