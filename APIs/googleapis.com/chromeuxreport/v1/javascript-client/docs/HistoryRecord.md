# ChromeUxReportApi.HistoryRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectionPeriods** | [**[CollectionPeriod]**](CollectionPeriod.md) | The collection periods indicate when each of the data points reflected in the time series data in metrics was collected. Note that all the time series share the same collection periods, and it is enforced in the CrUX pipeline that every time series has the same number of data points. | [optional] 
**key** | [**HistoryKey**](HistoryKey.md) |  | [optional] 
**metrics** | [**{String: MetricTimeseries}**](MetricTimeseries.md) | Metrics is the map of user experience time series data available for the record defined in the key field. Metrics are keyed on the metric name. Allowed key values: [\&quot;first_contentful_paint\&quot;, \&quot;first_input_delay\&quot;, \&quot;largest_contentful_paint\&quot;, \&quot;cumulative_layout_shift\&quot;, \&quot;experimental_time_to_first_byte\&quot;, \&quot;experimental_interaction_to_next_paint\&quot;] | [optional] 


