# ChromeUxReportApi.Record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectionPeriod** | [**CollectionPeriod**](CollectionPeriod.md) |  | [optional] 
**key** | [**Key**](Key.md) |  | [optional] 
**metrics** | [**{String: Metric}**](Metric.md) | Metrics is the map of user experience data available for the record defined in the key field. Metrics are keyed on the metric name. Allowed key values: [\&quot;first_contentful_paint\&quot;, \&quot;first_input_delay\&quot;, \&quot;largest_contentful_paint\&quot;, \&quot;cumulative_layout_shift\&quot;, \&quot;experimental_time_to_first_byte\&quot;, \&quot;experimental_interaction_to_next_paint\&quot;] | [optional] 


