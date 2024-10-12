

# GoogleCloudDatacatalogV1beta1UsageStats

Detailed counts on the entry's usage. Caveats: - Only BigQuery tables have usage stats - The usage stats only include BigQuery query jobs - The usage stats might be underestimated, e.g. wildcard table references are not yet counted in usage computation https://cloud.google.com/bigquery/docs/querying-wildcard-tables

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**totalCancellations** | **Float** | The number of times that the underlying entry was attempted to be used but was cancelled by the user. |  [optional] |
|**totalCompletions** | **Float** | The number of times that the underlying entry was successfully used. |  [optional] |
|**totalExecutionTimeForCompletionsMillis** | **Float** | Total time spent (in milliseconds) during uses the resulted in completions. |  [optional] |
|**totalFailures** | **Float** | The number of times that the underlying entry was attempted to be used but failed. |  [optional] |



