

# QueryBody

The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applications** | **List&lt;String&gt;** | Application IDs to include in cross-application queries. |  [optional] |
|**query** | **String** | The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/) |  |
|**timespan** | **String** | Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression. |  [optional] |



