

# MetricDatum

 <b>Internal only</b>. Collects Apache Airflow metrics. To learn more about the metrics published to Amazon CloudWatch, see <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/cw-metrics.html\">Amazon MWAA performance metrics in Amazon CloudWatch</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensions** | [**List**](List.md) |  |  [optional] |
|**metricName** | [**String**](String.md) |  |  |
|**statisticValues** | [**MetricDatumStatisticValues**](MetricDatumStatisticValues.md) |  |  [optional] |
|**timestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**unit** | [**Unit**](Unit.md) |  |  [optional] |
|**value** | [**Double**](Double.md) |  |  [optional] |



