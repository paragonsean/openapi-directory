

# TimeSeriesModelSettings

Time series model settings including model name, Time Series ID properties and default type ID.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultTypeId** | **UUID** | Default type ID of the model that new time series instances will automatically belong to. |  [optional] [readonly] |
|**name** | **String** | Time series model display name which is shown in the UX. Examples: \&quot;Temperature Sensors\&quot;, \&quot;MyDevices\&quot;. |  [optional] [readonly] |
|**timeSeriesIdProperties** | [**List&lt;TimeSeriesIdProperty&gt;**](TimeSeriesIdProperty.md) | Time series ID properties defined during environment creation. |  [optional] |



