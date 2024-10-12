

# MetricSpecification

Specifications of the Metrics for Azure Monitoring.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationType** | **String** | Only provide one value for this field. Valid values: Average, Minimum, Maximum, Total, Count. |  [optional] |
|**category** | **String** | The name of the metric category that the metric belongs to. A metric can only belong to a single category. |  [optional] |
|**dimensions** | [**List&lt;Dimension&gt;**](Dimension.md) | The dimensions of the metrics. |  [optional] |
|**displayDescription** | **String** | Localized friendly description of the metric. |  [optional] |
|**displayName** | **String** | Localized friendly display name of the metric. |  [optional] |
|**fillGapWithZero** | **String** | Optional. If set to true, then zero will be returned for time duration where no metric is emitted/published.   Ex. a metric that returns the number of times a particular error code was emitted. The error code may not appear   often, instead of the RP publishing 0, Shoebox can auto fill in 0s for time periods where nothing was emitted. |  [optional] |
|**name** | **String** | Name of the metric. |  [optional] |
|**unit** | **String** | The unit that makes sense for the metric. |  [optional] |



