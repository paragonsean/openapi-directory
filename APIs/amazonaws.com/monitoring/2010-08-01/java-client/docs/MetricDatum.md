

# MetricDatum

Encapsulates the information sent to either create a metric or add new values to be aggregated into an existing metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricName** | [**String**](String.md) |  |  |
|**dimensions** | [**List**](List.md) |  |  [optional] |
|**timestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**value** | [**Double**](Double.md) |  |  [optional] |
|**statisticValues** | [**MetricDatumStatisticValues**](MetricDatumStatisticValues.md) |  |  [optional] |
|**values** | [**List**](List.md) |  |  [optional] |
|**counts** | [**List**](List.md) |  |  [optional] |
|**unit** | [**StandardUnit**](StandardUnit.md) |  |  [optional] |
|**storageResolution** | [**Integer**](Integer.md) |  |  [optional] |



