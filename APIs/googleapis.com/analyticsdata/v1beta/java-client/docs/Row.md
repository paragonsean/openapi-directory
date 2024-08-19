

# Row

Report data for each row. For example if RunReportRequest contains: ```none \"dimensions\": [ { \"name\": \"eventName\" }, { \"name\": \"countryId\" } ], \"metrics\": [ { \"name\": \"eventCount\" } ] ``` One row with 'in_app_purchase' as the eventName, 'JP' as the countryId, and 15 as the eventCount, would be: ```none \"dimensionValues\": [ { \"value\": \"in_app_purchase\" }, { \"value\": \"JP\" } ], \"metricValues\": [ { \"value\": \"15\" } ] ```

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensionValues** | [**List&lt;DimensionValue&gt;**](DimensionValue.md) | List of requested dimension values. In a PivotReport, dimension_values are only listed for dimensions included in a pivot. |  [optional] |
|**metricValues** | [**List&lt;MetricValue&gt;**](MetricValue.md) | List of requested visible metric values. |  [optional] |



