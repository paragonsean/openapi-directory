

# Scorecard

A widget showing the latest value of a metric, and how this value relates to one or more thresholds.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blankView** | **Object** | A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  |  [optional] |
|**gaugeView** | [**GaugeView**](GaugeView.md) |  |  [optional] |
|**sparkChartView** | [**SparkChartView**](SparkChartView.md) |  |  [optional] |
|**thresholds** | [**List&lt;Threshold&gt;**](Threshold.md) | The thresholds used to determine the state of the scorecard given the time series&#39; current value. For an actual value x, the scorecard is in a danger state if x is less than or equal to a danger threshold that triggers below, or greater than or equal to a danger threshold that triggers above. Similarly, if x is above/below a warning threshold that triggers above/below, then the scorecard is in a warning state - unless x also puts it in a danger state. (Danger trumps warning.)As an example, consider a scorecard with the following four thresholds: { value: 90, category: &#39;DANGER&#39;, trigger: &#39;ABOVE&#39;, }, { value: 70, category: &#39;WARNING&#39;, trigger: &#39;ABOVE&#39;, }, { value: 10, category: &#39;DANGER&#39;, trigger: &#39;BELOW&#39;, }, { value: 20, category: &#39;WARNING&#39;, trigger: &#39;BELOW&#39;, } Then: values less than or equal to 10 would put the scorecard in a DANGER state, values greater than 10 but less than or equal to 20 a WARNING state, values strictly between 20 and 70 an OK state, values greater than or equal to 70 but less than 90 a WARNING state, and values greater than or equal to 90 a DANGER state. |  [optional] |
|**timeSeriesQuery** | [**TimeSeriesQuery**](TimeSeriesQuery.md) |  |  [optional] |



