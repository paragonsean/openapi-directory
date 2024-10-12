

# ListTimeSeriesResponse

The ListTimeSeries response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executionErrors** | [**List&lt;Status&gt;**](Status.md) | Query execution errors that may have caused the time series data returned to be incomplete. |  [optional] |
|**nextPageToken** | **String** | If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method. |  [optional] |
|**timeSeries** | [**List&lt;TimeSeries&gt;**](TimeSeries.md) | One or more time series that match the filter included in the request. |  [optional] |
|**unit** | **String** | The unit in which all time_series point values are reported. unit follows the UCUM format for units as seen in https://unitsofmeasure.org/ucum.html. If different time_series have different units (for example, because they come from different metric types, or a unit is absent), then unit will be \&quot;{not_a_unit}\&quot;. |  [optional] |



