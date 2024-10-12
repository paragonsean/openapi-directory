

# MetricStreamFilter

<p>This structure contains a metric namespace and optionally, a list of metric names, to either include in a metric stream or exclude from a metric stream.</p> <p>A metric stream's filters can include up to 1000 total names. This limit applies to the sum of namespace names and metric names in the filters. For example, this could include 10 metric namespace filters with 99 metrics each, or 20 namespace filters with 49 metrics specified in each filter.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namespace** | [**String**](String.md) |  |  [optional] |
|**metricNames** | [**List**](List.md) |  |  [optional] |



