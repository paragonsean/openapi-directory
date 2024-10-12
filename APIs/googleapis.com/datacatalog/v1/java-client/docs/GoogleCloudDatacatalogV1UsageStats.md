

# GoogleCloudDatacatalogV1UsageStats

Detailed statistics on the entry's usage. Usage statistics have the following limitations: - Only BigQuery tables have them. - They only include BigQuery query jobs. - They might be underestimated because wildcard table references are not yet counted. For more information, see [Querying multiple tables using a wildcard table] (https://cloud.google.com/bigquery/docs/querying-wildcard-tables)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**totalCancellations** | **Float** | The number of cancelled attempts to use the underlying entry. |  [optional] |
|**totalCompletions** | **Float** | The number of successful uses of the underlying entry. |  [optional] |
|**totalExecutionTimeForCompletionsMillis** | **Float** | Total time spent only on successful uses, in milliseconds. |  [optional] |
|**totalFailures** | **Float** | The number of failed attempts to use the underlying entry. |  [optional] |



