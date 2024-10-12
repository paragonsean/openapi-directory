

# ConsolidatedReportMetric

A metric that contributes to the consolidated report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricType** | [**MetricType**](MetricType.md) |  |  [optional] |
|**riskCounts** | **Map&lt;String, Integer&gt;** | A map from risk names to the count of how many questions have that rating. |  [optional] |
|**workloadId** | **String** | The ID assigned to the workload. This ID is unique within an Amazon Web Services Region. |  [optional] |
|**workloadName** | **String** | &lt;p&gt;The name of the workload.&lt;/p&gt; &lt;p&gt;The name must be unique within an account within an Amazon Web Services Region. Spaces and capitalization are ignored when checking for uniqueness.&lt;/p&gt; |  [optional] |
|**workloadArn** | **String** | The ARN for the workload. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time recorded. |  [optional] |
|**lenses** | [**List**](List.md) |  |  [optional] |
|**lensesAppliedCount** | [**Integer**](Integer.md) |  |  [optional] |



